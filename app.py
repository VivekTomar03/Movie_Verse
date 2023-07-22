from flask import Flask, jsonify, request,session
from flask_pymongo import PyMongo
from dotenv import load_dotenv
import os
from pymongo import MongoClient
from bson import ObjectId
from flask_cors import CORS
load_dotenv()
app = Flask(__name__)
CORS(app)
app.config['MONGO_URI'] =os.getenv('MONGO_URI')
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
            'date_of_birth': user['date_of_birth'],
            'password':user['password']
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
        'date_of_birth': user_data['date_of_birth'],
        'password':user_data['password']
    }
    result = mongo.db.users.insert_one(new_user)
    return jsonify({'message': 'User created successfully', 'user_id': str(result.inserted_id)})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"message": "Username and password are required"}), 400

    user =mongo.db.users.find_one({'username': username, 'password': password})
    if not user:
        return jsonify({"message": "Invalid username or password"}), 401

    # Fixed token provided by you
    fixed_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiaWF0IjoxNjI3NTI2MDQ4LCJleHAiOjE2Mjc1MjY2NDh9.zDmq7HLMmHwlgvCmW7tDxx-l6wAeTRTJ_zAxCThsPaI"

    return jsonify({
        "token": fixed_token,
        "username":username
    })

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
client = MongoClient('mongodb+srv://vivek:tomar@cluster0.aylkeza.mongodb.net/movieverse?retryWrites=true&w=majority')
db = client['movieverse']
movies_collection = db['movies']


# Movie schema definition
class Movie:
    def __init__(self, title, description, poster, language):
        self.title = title
        self.description = description
        self.poster = poster
        self.language = language

@app.route('/movies', methods=['GET'])
def get_movies():
    movies = movies_collection.find()
    movie_list = []
    for movie in movies:
        movie_dict = {
            'id': str(movie['_id']),
            'title': movie['title'],
            'description': movie['description'],
            'poster': movie['poster'],
            'language': movie['language']
        }
        movie_list.append(movie_dict)
    return jsonify(movie_list)

@app.route('/movies', methods=['POST'])
def add_movie():
    movie_data = request.get_json()
    new_movie = Movie(
        title=movie_data['title'],
        description=movie_data['description'],
        poster=movie_data['poster'],
        language=movie_data['language']
    )
    movie_id = movies_collection.insert_one(new_movie.__dict__).inserted_id
    return jsonify({'message': 'Movie created successfully', 'movie_id': str(movie_id)})

@app.route('/movies/<movie_id>', methods=['GET'])
def get_movie(movie_id):
    movie = movies_collection.find_one({'_id': ObjectId(movie_id)})
    if movie:
        movie_dict = {
            'id': str(movie['_id']),
            'title': movie['title'],
            'description': movie['description'],
            'poster': movie['poster'],
            'language': movie['language']
        }
        return jsonify(movie_dict)
    else:
        return jsonify({'message': 'Movie not found'}), 404

@app.route('/movies/<movie_id>', methods=['PUT'])
def update_movie(movie_id):
    movie_data = request.get_json()
    updated_movie = {
        'title': movie_data.get('title'),
        'description': movie_data.get('description'),
        'poster': movie_data.get('poster'),
        'language': movie_data.get('language')
    }
    result = movies_collection.update_one({'_id': ObjectId(movie_id)}, {'$set': updated_movie})
    if result.modified_count > 0:
        return jsonify({'message': 'Movie updated successfully'})
    else:
        return jsonify({'message': 'Movie not found'}), 404

@app.route('/movies/<movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    result = movies_collection.delete_one({'_id': ObjectId(movie_id)})
    if result.deleted_count > 0:
        return jsonify({'message': 'Movie deleted successfully'})
    else:
        return jsonify({'message': 'Movie not found'}), 404





# Shows endpoints
class Show:
    def __init__(self, title, description, poster, language, movie_id):
        self.title = title
        self.description = description
        self.poster = poster
        self.language = language
        self.movie_id = movie_id
        
@app.route('/movies/<movie_id>/shows', methods=['GET'])
def get_movie_shows(movie_id):
    shows = db.shows.find({'movie_id': movie_id})
    show_list = []
    for show in shows:
        show_dict = {
            'id': str(show['_id']),
            'title': show['title'],
            'description': show['description'],
            'poster': show['poster'],
            'language': show['language'],
            'movie_id': show['movie_id']
        }
        show_list.append(show_dict)
    return jsonify(show_list)

@app.route('/movies/<movie_id>/shows', methods=['POST'])
def add_movie_show(movie_id):
    data = request.get_json()
    show = Show(**data, movie_id=movie_id)
    result = db.shows.insert_one(show.__dict__)
    return jsonify({'message': 'Show created successfully', 'show_id': str(result.inserted_id)})

@app.route('/shows/<show_id>', methods=['GET'])
def get_show(show_id):
    show = db.shows.find_one({'_id': ObjectId(show_id)})
    if show:
        show_dict = {
            'id': str(show['_id']),
            'title': show['title'],
            'description': show['description'],
            'poster': show['poster'],
            'language': show['language'],
            'movie_id': show['movie_id']
        }
        return jsonify(show_dict)
    else:
        return jsonify({'message': 'Show not found'}), 404

@app.route('/shows/<show_id>', methods=['PUT'])
def update_show(show_id):
    data = request.get_json()
    updated_show = {
        'title': data.get('title'),
        'description': data.get('description'),
        'poster': data.get('poster'),
        'language': data.get('language'),
        'movie_id': data.get('movie_id')
    }
    result = db.shows.update_one({'_id': ObjectId(show_id)}, {'$set': updated_show})
    if result.modified_count > 0:
        return jsonify({'message': 'Show updated successfully'})
    else:
        return jsonify({'message': 'Show not found'}), 404

@app.route('/shows/<show_id>', methods=['DELETE'])
def delete_show(show_id):
    result = db.shows.delete_one({'_id': ObjectId(show_id)})
    if result.deleted_count > 0:
        return jsonify({'message': 'Show deleted successfully'})
    else:
        return jsonify({'message': 'Show not found'}), 404



class Event:
    def __init__(self, title, description, date, time,poster):
        self.title = title
        self.description = description
        self.date = date
        self.time = time
        self.poster = poster

@app.route('/events', methods=['GET'])
def get_events():
    events = db.events.find()
    event_list = []
    for event in events:
        event_dict = {
            'id': str(event['_id']),
            'title': event['title'],
            'description': event['description'],
            'date': event['date'],
            'time': event['time'],
            'poster':event['poster']
        }
        event_list.append(event_dict)
    return jsonify(event_list)

@app.route('/events', methods=['POST'])
def create_event():
    data = request.get_json()
    event = Event(
        title=data['title'],
        description=data['description'],
        date=data['date'],
        time=data['time'],
        poster=data['poster']
    )
    result = db.events.insert_one(event.__dict__)
    return jsonify({'message': 'Event created successfully', 'event_id': str(result.inserted_id)})

@app.route('/events/<event_id>', methods=['GET'])
def get_event(event_id):
    event = db.events.find_one({'_id': ObjectId(event_id)})
    if event:
        event_dict = {
            'id': str(event['_id']),
            'title': event['title'],
            'description': event['description'],
            'date': event['date'],
            'time': event['time'],
            'poster': event.get('poster', '')
        }
        return jsonify(event_dict)
    else:
        return jsonify({'message': 'Event not found'}), 404

@app.route('/events/<event_id>', methods=['PUT'])
def update_event(event_id):
    data = request.get_json()
    updated_event = {
        'title': data.get('title'),
        'description': data.get('description'),
        'date': data.get('date'),
        'time': data.get('time'),
        'poster':data.get('poster')
    }
    result = db.events.update_one({'_id': ObjectId(event_id)}, {'$set': updated_event})
    if result.modified_count > 0:
        return jsonify({'message': 'Event updated successfully'})
    else:
        return jsonify({'message': 'Event not found'}), 404

@app.route('/events/<event_id>', methods=['DELETE'])
def delete_event(event_id):
    result = db.events.delete_one({'_id': ObjectId(event_id)})
    if result.deleted_count > 0:
        return jsonify({'message': 'Event deleted successfully'})
    else:
        return jsonify({'message': 'Event not found'}), 404



class Participant:
    def __init__(self, name, email):
        self.name = name
        self.email = email
db = client['movieverse']
events_collection = db['events']
@app.route('/events/<event_id>/participants', methods=['GET'])
def get_event_participants(event_id):
    event = events_collection.find_one({'_id': ObjectId(event_id)})
    if event:
        participants = event.get('participants', [])
        return jsonify(participants)
    else:
        return jsonify({'message': 'Event not found'}), 404

@app.route('/events/<event_id>/participants', methods=['POST'])
def add_event_participant(event_id):
    data = request.get_json()
    participant = Participant(name=data.get('name'), email=data.get('email'))
    events_collection.update_one({'_id': ObjectId(event_id)}, {'$push': {'participants': participant.__dict__}})
    return jsonify({'message': 'Participant added to the event successfully'})

@app.route('/events/<event_id>/participants', methods=['DELETE'])
def remove_event_participant(event_id):
    data = request.get_json()
    if 'email' not in data:
        return jsonify({'message': 'Participant email not provided'}), 400

    event = events_collection.find_one({'_id': ObjectId(event_id)})
    if event:
        participants = event.get('participants', [])
        for participant in participants:
            if participant.get('email') == data['email']:
                participants.remove(participant)
                events_collection.update_one({'_id': ObjectId(event_id)}, {'$set': {'participants': participants}})
                return jsonify({'message': 'Participant removed from the event successfully'})
        return jsonify({'message': 'Participant not found in the event'}), 404
    else:
        return jsonify({'message': 'Event not found'}), 404



if __name__ == '__main__':
    app.run(debug=True)
