from DB import Database


class Message():

    def __init__(self):
        self.db = Database()

    def drop_message(self, message_x, message_y, message, user_id, viewable_by):
        message_coordinates = (message_x, message_y)
        print "(" + str(message_coordinates) + ") " + str(message)
        message_entry = {"coordinates":message_coordinates,
                         "message":message,
                         "userid":user_id,
                         "viewable_by":viewable_by
                        }
        self.db.insert(message_entry)
        self.db.get_entries()

    def pickup_message(self, user_x, user_y, user_id):
        #p = self.db.posts.find({"coordinates":{(user_x,user_y)},"userid":user_id})
        print "ASDFADGADSF"
        p = self.db.posts.find()
        print p
        print "fsadfasdf"

