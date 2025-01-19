import json 
import os

class Database:
    def __init__(self, filepath="passwords.json"):
        
        self.filepath = filepath

        if not os.path.exists(self.filepath):
            with open(self.filepath, 'w') as db:
                json.dump([], db)

    def read_data(self):
        with open(self.filepath, 'r') as db:
            return json.load(db)
    
    def write_data(self,data):
        with open(self.filepath, 'w') as db:
            json.dump(data, db, indent=4)

    def add_password(self, service, userid, encrypted_password):
        data = self.read_data()
        entry = {
            "service": service,
            "userid": userid,
            "encrypted_password": encrypted_password
        }

        data.append(entry)
        self.write_data(data)
    
    def get_passwords(self):
        return self.read_data()