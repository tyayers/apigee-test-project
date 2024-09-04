from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def get_users():
    """
    Get a list of all users.
    """
    return jsonify([
        {
            "firstName": "John",
            "lastName": "Doe",
            "email": "john.doe@example.com",
            "address": "123 Main St",
            "userGroups": ["admin", "users"]
        },
        {
            "firstName": "Jane",
            "lastName": "Smith",
            "email": "jane.smith@example.com",
            "address": "456 Oak Ave",
            "userGroups": ["users"]
        }
    ])

@app.route('/users', methods=['POST'])
def create_user():
    """
    Create a new user.
    """
    data = request.get_json()
    return jsonify(data), 201

@app.route('/users/<userId>', methods=['GET'])
def get_user(userId):
    """
    Get the details of a specific user.
    """
    return jsonify({
        "firstName": "John",
        "lastName": "Doe",
        "email": "john.doe@example.com",
        "address": "123 Main St",
        "userGroups": ["admin", "users"]
    })

@app.route('/users/<userId>', methods=['DELETE'])
def delete_user(userId):
    """
    Delete a specific user.
    """
    return '', 200

@app.route('/users/<userId>', methods=['PUT'])
def update_user(userId):
    """
    Update the details of a specific user.
    """
    data = request.get_json()
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(debug=True)
