from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_mail import Mail, Message

import jwt, datetime

import backend.database.databaseAccess as dt
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234567890'
CORS(app)

# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com' # Use Gmail's SMTP server
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('EMAIL_USER' or 'kidistMegersa21@gmail.com') # Your Gmail address
app.config['MAIL_PASSWORD'] = os.getenv('212121Enate#') # Your Gmail App Password
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('yisakdemelash7@gmail.com') # Sender email

mail = Mail(app)

@app.route('/')
def home():
    return "welcome to the backend part!"

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()  # Get JSON data from the frontend
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({"status": "error", "message": "Username and password are required"}), 400

    user = dt.get_user_by_id(username)


    if not user or not user['password'] == password:  # Plaintext comparison
        return jsonify({"status": "error", "message": "Invalid credentials"}), 401

    token = jwt.encode(
        {
            'username': username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        },
        app.config['SECRET_KEY'],
        algorithm='HS256'
    )
    return jsonify({'token': token})

@app.route('/api/user/<int:user_id>/username', methods=['PUT'])
def update_username(user_id):
    data = request.get_json()
    new_username = data.get('new_username')

    if not new_username:
        return jsonify({"status": "error", "message": "New username is required"}), 400

    if dt.update_user_username(user_id, new_username):
        return jsonify({"status": "success", "message": "Username updated successfully"}), 200
    else:
        return jsonify({"status": "error", "message": "Failed to update username or user not found"}), 404

@app.route('/api/support', methods=['POST'])
def send_support_email():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    if not all([name, email, message]):
        return jsonify({"status": "error", "message": "All fields are required."}), 400

    try:
        msg = Message(
            subject="Digital Bank Support Request",
            recipients=["kidistmegersa21@gmail.com"],
            body=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        )
        mail.send(msg)
        return jsonify({"status": "success", "message": "Your message has been sent successfully!"}), 200
    except Exception as e:
        print(f"Error sending email: {e}")
        return jsonify({"status": "error", "message": "Failed to send message. Please try again later."}), 500


if __name__ == '__main__':
    app.run(debug=True)