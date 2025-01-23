import json 
import os

class Database:
    def __init__(self, filepath="passwords.json"):
        
        self.filepath = filepath

        if not os.path.exists(self.filepath) or os.path.getsize(self.filepath) == 0:
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
        for entry in data:
            if entry["service"] == service and entry["userid"] == userid:
                raise ValueError(f"Entry for {service} and Username {userid} already exists!")
            
        entry = {
            "service": service,
            "userid": userid,
            "password": encrypted_password
        }

        data.append(entry)
        self.write_data(data)
    
    def get_passwords(self):
        return self.read_data()
    
    def delete_password(self, service, userid):
        data = self.read_data()
        updated_data = [entry for entry in data if not (entry["service"] == service and entry["userid"] == userid)]
        self.write_data(updated_data)

    def update_password(self, service, userid, new_enc_passwd):
        data = self.read_data()
        for entry in data:
            if entry["service"] == service and entry["userid"] == userid:
                entry["password"] = new_enc_passwd

                break

        self.write_data(data)
        print(f"Password for {service} updated successfully!")
        