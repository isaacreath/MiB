from DB import Database


class User():

    def __init__(self):
        self.db = Database()

    def login(self, uid):
        response = self.db.find_user({"userid": uid})
        if(response is None):
            return "User is not yet registered"
        else:
            return response["username"]

    def add_user(self, uid, username):
        self.db.add_user({"userid": uid, "username": username})
        return "user added"
