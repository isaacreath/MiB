from flask import Flask
from flask import request
from DB import Database
from messages import Message
from friends import Friend
from users import User

#setup the app and the db
app = Flask(__name__)
db = Database()
messages = Message()
friends = Friend()
users = User()
def validate_post_request(args):
    for arg in args:
        if arg is None:
            return False
    return True





@app.route("/login", methods=['POST'])
def login():
    uid = int(request.form.get('uid'))
    print uid
    return users.login(uid)


@app.route("/addUser", methods=['POST'])
def add_user():
    username = request.form.get('username')
    uid = int(request.form.get('uid'))
    users.add_user(uid, username)
    return "user added"

@app.route("/addFriend", methods=['POST'])
def add_friend():
    uid = int(request.form.get('uid'))
    friend_name = request.form.get('friend')
    friends.add_friend(uid, friend_name)
    return "friend added successfully"

@app.route("/listFriends", methods=['POST'])
def list_friends():
    uid = int(request.form.get('uid'))
    return str(friends.list_friends(uid))

'''
Endpoint for adding a new bottle to the database. Requires 5 arguments
x: the x coordinate where the bottle is dropped (float)
y: the y coordinate where the bottle is dropped (float)
message: the content of the message  (plain text, or matrix representation of picture/video)
userId: the unique user id of the user who dropped the message (int)
viewable_by: a string containing who can view the message (friend or public)

'''

@app.route("/dropMessage", methods=['POST'])
def drop_message():
    message_x = request.form.get('x')
    message_y = request.form.get('y')
    message = request.form.get('message')
    user_id = request.form.get('userId')
    viewable_by = request.form.get('viewableBy')
    args = [message_x, message_y, message, user_id, viewable_by]
    if validate_post_request(args):
        messages.drop_message(message_x, message_y, message, user_id, viewable_by)
        return "Post Successful"
    else:
        return "Invalid argument matching", 400

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.debug = True
    app.run()
