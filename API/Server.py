from flask import Flask
from pymongo import MongoClient
from flask import request

#setup the app and the db
app = Flask(__name__)
client = MongoClient()
db = client['messages']
collection = db['collection']
posts = db.posts


@app.route("/dropMessage", methods=['POST'])
def drop_message():
    print "ASDFA"
    message_coordinates = request.form.get('coords')
    message = request.form.get('message')
    print "(" + str(message_coordinates) + ") " + str(message)
    message_entry = {"coordinates" : message_coordinates,
                     "message":message
                    }
    posts.insert(message_entry)
    for p in posts.find():
        print p

    return "Post Successful"

git@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.debug = True
    app.run()
