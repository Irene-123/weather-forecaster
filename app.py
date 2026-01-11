# from flask import Flask, jsonify

# app = Flask(__name__)

# @app.route('/users', methods=['GET'])
# def get_users():
#     users = ["K", "A", "R", "E", "N"]
#     return jsonify(users)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)


from flask import Flask, jsonify


app = Flask(__name__)

users = {
    1: {"name": "Alice", "age": 30, "role": "admin", "department": "HR", "email": "alice@abc.com"},
    2: {"name": "Bob", "age": 25, "role": "user", "department": "IT", "email": "bob@abc.com"},
    3: {"name": "Charlie", "age": 28, "role": "user", "department": "Finance", "email": "charlie@abc.com"},
    4: {"name": "Diana", "age": 32, "role": "admin", "department": "IT", "email": "diana@abc.com"},
}

@app.route('/users', methods=['GET'])
def get_users():
    names = []
    for key,user_dict in users.items():
        names.append(user_dict["name"])
    
    return jsonify(names)


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)