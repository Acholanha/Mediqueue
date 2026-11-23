 from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def home():
    return send_file('index.html')

@app.route('/register')
def register():
    return send_file('register.html')

@app.route('/tasks')
def tasks():
    return send_file('tasks.html')

if __name__ == '__main__':
    app.run(debug=True)