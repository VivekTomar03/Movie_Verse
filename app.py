from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

app = Flask(__name__)
app.config['MONGO_URI'] = os.getenv('MONGO_URI')
mongo = PyMongo(app)

@app.route('/users', methods=['GET'])
def get_users():
    users = mongo.db.users.find()
    user_list = []
    for user in users:
        user_dict = {
            'username': user['username'],
            'user_status': user['user_status'],
            'gender': user['gender'],
            'membership_type': user['membership_type'],
            'bio': user['bio'],
            'date_of_birth': user['date_of_birth']
        }
        user_list.append(user_dict)
    return jsonify(user_list)

@app.route('/users', methods=['POST'])
def create_user():
    user_data = request.get_json()
    new_user = {
        'username': user_data['username'],
        'user_status': user_data['user_status'],
        'gender': user_data['gender'],
        'membership_type': user_data['membership_type'],
        'bio': user_data['bio'],
        'date_of_birth': user_data['date_of_birth']
    }
    result = mongo.db.users.insert_one(new_user)
    return jsonify({'message': 'User created successfully', 'user_id': str(result.inserted_id)})

# Add other routes and functions for updating, deleting, and retrieving users by ID

if __name__ == '__main__':
    app.run(debug=True)
