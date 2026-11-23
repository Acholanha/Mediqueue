 import sqlite3
from flask import Flask, send_file, request, jsonify

app = Flask(__name__)
DB_NAME = 'mediqueue.db'

# Initialize SQLite Database
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_name TEXT NOT NULL,
            department TEXT NOT NULL,
            status TEXT NOT NULL
        )
    ''')
    cursor.execute('SELECT COUNT(*) FROM appointments')
    if cursor.fetchone()[0] == 0:
        cursor.executemany(
            'INSERT INTO appointments (patient_name, department, status) VALUES (?, ?, ?)',
            [
                ('Anha Mahmud', 'Cardiology', 'In Consultation'),
                ('Rabeya Akter', 'Medicine', 'Waiting'),
                ('Tanvir Hasan', 'Orthopedics', 'Waiting')
            ]
        )
    conn.commit()
    conn.close()

init_db()

# Frontend Page Routes
@app.route('/')
def home():
    return send_file('index.html')

@app.route('/about')
def about():
    return send_file('about.html')

@app.route('/dashboard')
def dashboard():
    return send_file('dashboard.html')

@app.route('/register')
def register():
    return send_file('register.html')

@app.route('/tasks')
def tasks():
    return send_file('tasks.html')

# Day 4: REST API Routes (GET, POST, PUT, DELETE)
@app.route('/api/appointments', methods=['GET'])
def get_appointments():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    rows = conn.execute('SELECT * FROM appointments').fetchall()
    conn.close()
    return jsonify([dict(row) for row in rows])

@app.route('/api/appointments', methods=['POST'])
def add_appointment():
    data = request.get_json()
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO appointments (patient_name, department, status) VALUES (?, ?, ?)',
        (data['patient_name'], data['department'], 'Waiting')
    )
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return jsonify({'id': new_id, 'message': 'Appointment added'}), 201

@app.route('/api/appointments/<int:apt_id>', methods=['PUT'])
def update_appointment(apt_id):
    data = request.get_json()
    conn = sqlite3.connect(DB_NAME)
    conn.execute('UPDATE appointments SET status = ? WHERE id = ?', (data['status'], apt_id))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Status updated'})

@app.route('/api/appointments/<int:apt_id>', methods=['DELETE'])
def delete_appointment(apt_id):
    conn = sqlite3.connect(DB_NAME)
    conn.execute('DELETE FROM appointments WHERE id = ?', (apt_id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Appointment deleted'})

if __name__ == '__main__':
    app.run(debug=True)