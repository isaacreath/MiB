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
        self.user_collection.insert(user)

    def add_friend(self, friend):
        self.friends_posts.insert(friend)

    def list_friend(self, uid):
        return self.friend_collection.find({"userid": uid})

    def find_user(self, uid):
        try:
            return self.user_collection.find(uid)[0]
        except:
            return None


