from flask import Flask
from flask import render_template
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
    # message_coordinates = "50,20"
    # message = "fuck me"
    print "(" + str(message_coordinates) + ") " + str(message)
    message_entry = {"coordinates" : message_coordinates,
                     "message":message
                    }
    posts.insert(message_entry)
    for p in posts.find():
        print p

    return "Post Successful"


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/pg1.html")
def pg1():
    return render_template("pg1.html")

@app.route("/pg2.html")
def pg2():
    return render_template("pg2.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
