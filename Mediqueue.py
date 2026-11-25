from flask import Flask, render_template, request, jsonify
import sqlite3
import os

app = Flask(__name__, template_folder='.')
DB_NAME = 'mediqueue.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_name TEXT NOT NULL,
            department TEXT NOT NULL,
            priority TEXT DEFAULT 'Normal',
            status TEXT DEFAULT 'Waiting'
        )
    ''')
    # পুরোনো টেবিলে priority কলাম না থাকলে স্বয়ংক্রিয়ভাবে যোগ করবে
    try:
        cursor.execute("ALTER TABLE appointments ADD COLUMN priority TEXT DEFAULT 'Normal'")
    except sqlite3.OperationalError:
        pass

    count = cursor.execute('SELECT COUNT(*) FROM appointments').fetchone()[0]
    if count == 0:
        sample_data = [
            ('Anha Mahmud', 'Cardiology', 'Emergency', 'In Consultation'),
            ('Rabeya Akter', 'Medicine', 'Normal', 'Waiting'),
            ('Tanvir Hasan', 'Orthopedics', 'Normal', 'Waiting')
        ]
        cursor.executemany(
            'INSERT INTO appointments (patient_name, department, priority, status) VALUES (?, ?, ?, ?)',
            sample_data
        )
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/tasks')
def tasks():
    return render_template('tasks.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/tv')
def tv_display():
    return render_template('tv.html')

# CRUD APIs
@app.route('/api/appointments', methods=['GET'])
def get_appointments():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    # Emergency রোগীরা সবার ওপরে দেখাবে
    rows = conn.execute('''
        SELECT * FROM appointments 
        ORDER BY CASE WHEN status = 'Completed' THEN 2 ELSE 1 END,
                 CASE WHEN priority = 'Emergency' THEN 1 ELSE 2 END,
                 id ASC
    ''').fetchall()
    conn.close()
    return jsonify([dict(row) for row in rows])

@app.route('/api/appointments', methods=['POST'])
def add_appointment():
    data = request.get_json()
    priority = data.get('priority', 'Normal')
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO appointments (patient_name, department, priority, status) VALUES (?, ?, ?, ?)',
        (data['patient_name'], data['department'], priority, 'Waiting')
    )
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return jsonify({'id': new_id, 'message': 'Appointment added'}), 201

@app.route('/api/appointments/<int:id>/call', methods=['PUT'])
def call_appointment(id):
    conn = sqlite3.connect(DB_NAME)
    conn.execute("UPDATE appointments SET status = 'In Consultation' WHERE status = 'In Consultation'")
    conn.execute("UPDATE appointments SET status = 'In Consultation' WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Patient called'})

@app.route('/api/appointments/<int:id>', methods=['PUT'])
def update_appointment(id):
    conn = sqlite3.connect(DB_NAME)
    conn.execute("UPDATE appointments SET status = 'Completed' WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Appointment completed'})

@app.route('/api/appointments/<int:id>', methods=['DELETE'])
def delete_appointment(id):
    conn = sqlite3.connect(DB_NAME)
    conn.execute('DELETE FROM appointments WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Appointment deleted'})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)