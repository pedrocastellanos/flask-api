from flask import Flask, jsonify, request
from users import users

app = Flask(__name__)


# Testing Route
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'response': 'pong!'})

# Get Data Routes
@app.route('/users')
def getUsers():
    return jsonify({'users': users})


@app.route('/user/<user_id>')
def getUser(user_id):
    userFound = [user for user in users if user['id'] == int(user_id)]
    if (len(userFound) > 0):
        return jsonify({'user': userFound[0]})
    return jsonify({'message': 'User Not found'})
    

# Create Data Routes
@app.route('/user', methods=['POST'])
def adduser():
    new_user = {
        "id": users[-1]["id"] + 1,
        'name': request.json['name'],
        'username': request.json['username'],
        'email': request.json['email']
    }
    users.append(new_user)
    return jsonify({'users': users})

# Update Data Route
@app.route('/user/<user_id>', methods=['PUT'])
def edituser(user_id):
    usersFound = [user for user in users if user['id'] == int(user_id)]
    if (len(usersFound) > 0):
        usersFound[0]['name'] = request.json['name']
        usersFound[0]['username'] = request.json['username']
        usersFound[0]['email'] = request.json['email']
        return jsonify({
            'message': 'user Updated',
            'user': usersFound[0]
        })
    return jsonify({'message': 'user Not found'})

# DELETE Data Route
@app.route('/user/<user_id>', methods=['DELETE'])
def deleteUser(user_id):
    usersFound = [user for user in users if user['id'] == int(user_id)]
    if len(usersFound) > 0:
        users.remove(usersFound[0])
        return jsonify({
            'message': 'user Deleted',
            'users': users
        })

if __name__ == '__main__':
    app.run(debug=True, port=4000)


