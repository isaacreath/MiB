from pymongo import MongoClient

class Database():

    def __init__(self):
        self.client = MongoClient()
        self.db = self.client['messages']
        self.friends_database = self.client['friends']
        self.user_database = self.client['users']
        print self.client.database_names()
        self.collection = self.db['collection']
        self.friend_collection = self.friends_database['collection']
        self.user_collection = self.user_database['collection']
        self.posts = self.db.posts
        self.user_posts = self.user_database.posts
        self.friends_posts = self.friends_database.posts

    def insert(self, entry):
        self.posts.insert(entry)

    def get_entries(self):
        for p in self.posts.find():
            print p

    def add_user(self, user):
        uid = user["userid"]
        self.user_collection.insert(user)
        self.friend_collection.insert({"userid": uid, "friend_list": []})

    def add_friend(self, uid, friend):
        print "what"
        print self.friend_collection.find({"userid": uid})[0]["friend_list"]
        friend_list = self.friend_collection.find({"userid": uid})[0]["friend_list"]
        friend_list.append(friend)
        self.friend_collection.update(
            {"userid": uid},
            {
                "userid": uid,
                "friend_list": friend_list
            }
        )
        print self.friend_collection.find({"userid": uid})[0]["friend_list"]
        return "friend added successfully"


    def list_friends(self, uid):
        return self.friend_collection.find({"userid": uid})[0]["friend_list"]

    def find_user(self, uid):
        try:
            return self.user_collection.find(uid)[0]
        except:
            return None


