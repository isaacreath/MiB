from flask import Flask
from flask import request
from DB import Database
from Messages import Message
from Friends import Friend

#setup the app and the db
app = Flask(__name__)
db = Database()
messages = Message()
friends = Friend()

def validate_post_request(args):
    for arg in args:
        if arg is None:
            return False
    return True



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
        return "Post Successful\n"
    else:
        return "Invalid argument matching\n", 400

@app.route("/pickupMessage", methods=['POST'])
def pickup_message():
    user_x = request.form.get('x')
    user_y = request.form.get('y')
    user_id = request.form.get('userId')
    args = [user_x, user_y, user_id]
    if validate_post_request(args):
        messages.pickup_message(user_x, user_y, user_id)
        return "Post Successful\n"
    else:
        return "Invalid argument matching\n", 400


@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.debug = True
    app.run()
