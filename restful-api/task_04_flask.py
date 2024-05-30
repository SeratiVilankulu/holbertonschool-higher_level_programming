from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for users
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

# Define the route for the root URL
@app.route('/')
def home():
    return "Welcome to the Flask API!"

# Define the route for /data to serve JSON data
@app.route('/data')
def get_data():
    return jsonify(list(users.keys()))

# Define the route for /status to return API status
@app.route('/status')
def status():
    return "OK"

# Define the route to get user information by username
@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return "User not found", 404

# Define the route to add a new user using POST request
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data.get('username')
    if not username or username in users:
        return jsonify({"message": "Invalid username or user already exists"}), 400
    
    user = {
        "username": username,
        "name": data.get('name'),
        "age": data.get('age'),
        "city": data.get('city')
    }
    users[username] = user
    return jsonify({"message": "User added", "user": user})

# Run the Flask development server
if __name__ == "__main__":
    app.run(debug=True)
