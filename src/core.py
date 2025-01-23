from encryption import Encryption
from database import Database
from pathlib import Path
import os
import platform
import hashlib
import base64

def derive_key(master_password):
    key = hashlib.sha256(master_password.encode()).digest()
    key = base64.urlsafe_b64encode(key)

    return key

if os.name == 'nt':  # Windows
    data_filepath = Path(os.getenv("APPDATA")) / "permutations"
elif os.name == 'posix':
    import platform
    system = platform.system()
    if system == 'Darwin':  # macOS
        data_filepath = Path.home() /"Library"/"Application"/"Support"/"permutations"
    elif system == 'Linux':  # Linux
        data_filepath = Path.home() /".local"/"share"/"permutations"
    else:
        raise ValueError(f"Unsupported POSIX OS: {system}")
else:
    raise ValueError(f"Unsupported OS: {os.name}")

os.makedirs(data_filepath, exist_ok=True)


class PassMan:
    def __init__(self, encryption_key, db_filepath=data_filepath/"passwords.json"):
        self.encryption = Encryption(encryption_key)
        self.database = Database(db_filepath)
    
    def add_passwd(self, service, userid, password):
        encrypted_passwd = self.encryption.encrypt(password)
        self.database.add_password(service, userid, encrypted_passwd)
    
    def view_passwd(self):
        entries = self.database.get_passwords()
        if not entries:
            print("No Passwords found")
            return
        
        print("\nSaved Passwords: ")
        for entry in entries:
            decrypted_passwd = self.encryption.decrypt(entry["password"])
            print(f"Service: {entry["service"]}, Username: {entry["userid"]}, Password: {decrypted_passwd}")

    def update_passwd(self, service, userid, new_password):
        encrypted_passwd = self.encryption.encrypt(new_password)
        self.database.update_password(service, userid, new_enc_passwd=encrypted_passwd)

        print(f"Password for {service} updated successfully!")

    def delete_passwd(self, service, userid):
        self.database.delete_password(service,userid)
        print(f"Password for {service} has been deleted successfully!")

if __name__ == "__main__":

    masterkey = derive_key(input("Enter your Master Password: "))
    manager = PassMan(encryption_key=masterkey)

    while True:
        print("\nPassword Manager\n")
        print("1. Add Password")
        print("2. View Passwords")
        print("3. Update Password")
        print("4. Delete Password")
        print("5. Exit")

        print("\nEnter the operation number [1-5]\n")

        choice = int(input("==> "))


        if choice == 1:

            service = input("Service: ")
            userid = input("Username: ")
            password = input("Password: ")

            manager.add_passwd(service, userid, password)
        
        elif choice == 2:

            manager.view_passwd()

        elif choice == 3:

            service = input("Service: ")
            userid = input("Username: ")
            new_password = input("New Password: ")

            manager.update_passwd(service, userid, new_password)

        elif choice == 4:
            service = input("Service: ")
            userid = input("Username: ")

            manager.delete_passwd(service,userid)

        elif choice == 5:
            print("Exiting Permutations")
            break
        
        else:
            print("INVALID CHOICE: Please try again.")