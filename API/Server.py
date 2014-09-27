from flask import Flask
from pymongo import MongoClient
from flask import request

#setup the app and the db
app = Flask(__name__)
client = MongoClient()
db = client['messages']
collection = db['collection']
posts = db.posts

def validate_post_request(args):
    for arg in args:
        if arg is None:
            return False
    return True


@app.route("/dropMessage", methods=['POST'])
def drop_message():
    message_x = request.form.get('x')
    message_y = request.form.get('y')
    message = request.form.get('message')
    user_id = request.form.get('userId')
    args = [message_x, message_y, message, user_id]
    if validate_post_request(args):
        message_coordinates = (message_x, message_y)
        print "(" + str(message_coordinates) + ") " + str(message)
        message_entry = {"coordinates" : message_coordinates,
                         "message":message
                        }
        posts.insert(message_entry)
        for p in posts.find():
            print p

        return "Post Successful"
    else:
        return "Invalid argument matching", 400

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.debug = True
    app.run()
