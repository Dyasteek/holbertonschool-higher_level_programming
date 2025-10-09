from flask import Flask, jsonify, request


app = Flask(__name__)


users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/status")
def status():
    return "OK"


@app.route("/data")
def get_usernames():
    usernames = list(users.keys())
    return jsonify(usernames)


@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route("/add_user", methods=["POST"])
def add_user():
    payload = request.get_json(silent=True) or {}

    username = payload.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    user_object = {
        "username": username,
        "name": payload.get("name"),
        "age": payload.get("age"),
        "city": payload.get("city"),
    }

    users[username] = user_object

    return jsonify({
        "message": "User added",
        "user": user_object,
    }), 201


if __name__ == "__main__":
    app.run()