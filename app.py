from flask import Flask, jsonify, request,session
from flask_pymongo import PyMongo
from dotenv import load_dotenv
import os
from bson import ObjectId
from flask_cors import CORS
load_dotenv()
app = Flask(__name__)
CORS(app)
app.config['MONGO_URI'] = os.getenv('MONGO_URI')
mongo = PyMongo(app)

@app.route('/users', methods=['GET'])
def get_users():
    users = mongo.db.users.find()
    user_list = []
    for user in users:
        user_dict = {
            'id': str(user['_id']),
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

 ### get user by user_id
@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = mongo.db.users.find_one({'_id': ObjectId(user_id)})
    if user:
        user_dict = {
            'username': user['username'],
            'user_status': user['user_status'],
            'gender': user['gender'],
            'membership_type': user['membership_type'],
            'bio': user['bio'],
            'date_of_birth': user['date_of_birth']
        }
        return jsonify(user_dict)
    else:
        return jsonify({'message': 'User not found'}), 404
    
from bson import ObjectId

@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    user_data = request.get_json()
    updated_user = {
        'username': user_data.get('username'),
        'user_status': user_data.get('user_status'),
        'gender': user_data.get('gender'),
        'membership_type': user_data.get('membership_type'),
        'bio': user_data.get('bio'),
        'date_of_birth': user_data.get('date_of_birth')
    }
    result = mongo.db.users.update_one({'_id': ObjectId(user_id)}, {'$set': updated_user})
    if result.modified_count > 0:
        return jsonify({'message': 'User updated successfully'})
    else:
        return jsonify({'message': 'User not found'}), 404

#### delete user by user_id    
@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    result = mongo.db.users.delete_one({'_id': ObjectId(user_id)})
    if result.deleted_count > 0:
        return jsonify({'message': 'User deleted successfully'})
    else:
        return jsonify({'message': 'User not found'}), 404    

#### admin login 
# Admin credentials
ADMIN_EMAIL = "admin@example.com"
ADMIN_PASSWORD = "admin123"

# Route for admin login
@app.route('/admin/login', methods=['POST'])
def admin_login():
    # Get the login details from the request body
    login_data = request.get_json()
    email = login_data.get('email')
    password = login_data.get('password')

    # Check if the provided credentials match the admin credentials
    if email == ADMIN_EMAIL and password == ADMIN_PASSWORD:
        # Set the admin authentication flag in the session
      
        return jsonify({
            'message': 'Admin login successful',
            'token':"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiaWF0IjoxNjI3NTI2MDQ4LCJleHAiOjE2Mjc1MjY2NDh9.zDmq7HLMmHwlgvCmW7tDxx-l6wAeTRTJ_zAxCThsPaI"
        })
    else:
        return jsonify({'message': 'Invalid email or password'})


    

if __name__ == '__main__':
    app.run(debug=True)
