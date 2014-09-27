from flask import Flask
from flask import request
from DB import Database
#setup the app and the db
app = Flask(__name__)
db = Database()


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
        message_coordinates = (message_x, message_y)
        print "(" + str(message_coordinates) + ") " + str(message)
        message_entry = {"coordinates":message_coordinates,
                         "message":message,
                         "userid":user_id,
                         "viewable_by":viewable_by
                        }
        db.insert(message_entry)
        db.get_entries()
        return "Post Successful"
    else:
        return "Invalid argument matching", 400

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.debug = True
    app.run()
