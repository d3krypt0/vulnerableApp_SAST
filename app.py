from flask import Flask, request, render_template
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Hardcoded credentials
USERNAME = 'admin'
PASSWORD = 'password123'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    # Vulnerable to SQL Injection
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    return f"Executed query: {query}"

@app.route('/xss', methods=['POST'])
def xss():
    comment = request.form.get('comment')
    # Vulnerable to XSS
    return f"Your comment: {comment}"

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)
    return f"File uploaded to {filepath}"

if __name__ == '__main__':
    app.run(debug=True)
