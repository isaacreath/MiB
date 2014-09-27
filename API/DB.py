from pymongo import MongoClient

class Database():
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client['messages']
        self.collection = self.db['collection']
        self.posts = self.db.posts

    def insert(self, entry):
        self.posts.insert(entry)

    def get_entries(self):
        for p in self.posts.find():
            print p


