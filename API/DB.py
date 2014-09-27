from pymongo import MongoClient

class Database():
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client['messages']
        self.friends_database = self.client['friends']
        self.user_database = self.client['users']
        self.collection = self.db['collection']
        self.friend_collection = self.db['friend_collection']
        self.user_collection = self.db['user_collection']
        self.posts = self.db.posts
        self.user_posts = self.user_database.posts
        self.friends_posts = self.friends_database.posts

    def insert(self, entry):
        self.posts.insert(entry)

    def get_entries(self):
        for p in self.posts.find():
            print p

    def add_user(self, user):
        self.user_posts.insert(user)

    def add_friend(self, friend):
        self.friends_posts.insert(friend)

    def list_friend(self, uid):
        return self.friend_collection.find({"userid":uid})