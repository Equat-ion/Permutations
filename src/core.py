from encryption import Encryption
from database import Database
import hashlib
import base64

def derive_key(master_password):
    """Create encryption key from master password"""
    key = hashlib.sha256(master_password.encode()).digest()
    return base64.urlsafe_b64encode(key)

class PassMan:
    def __init__(self, encryption_key):
        self.encryption = Encryption(encryption_key)
        self.db = Database()

    def add_password(self):
        print("\n--- Add New Password ---")
        service = input("Website/App: ")
        username = input("Username: ")
        password = input("Password: ")

        encrypted = self.encryption.encrypt(password)
        self.db.add_password(service, username, encrypted)
        print("✓ Password saved!")

    def view_passwords(self):
        entries = self.db.get_passwords()

        if not entries:
            print("No passwords saved.")
            return

        print("\n=== Your Passwords ===")
        for entry in entries:
            decrypted = self.encryption.decrypt(entry["password"])
            print(f"Service: {entry['service']}")
            print(f"Username: {entry['userid']}")
            print(f"Password: {decrypted}")
            print("-" * 30)

    def update_password(self):
        print("\n--- Update Password ---")
        service = input("Website/App: ")
        username = input("Username: ")
        new_pass = input("New Password: ")

        encrypted = self.encryption.encrypt(new_pass)
        self.db.update_password(service, username, encrypted)
        print("✓ Password updated!")

    def delete_password(self):
        print("\n--- Delete Password ---")
        service = input("Website/App: ")
        username = input("Username: ")

        self.db.delete_password(service, username)
        print("✓ Password deleted!")

# Main Program
if __name__ == "__main__":
    print("🔐 PERMUTATIONS - Password Manager")
    print("===================================\n")

    # Master Password
    master_key = input("Enter your Master Password: ")
    key = derive_key(master_key)

    # Create manager
    manager = PassMan(key)

    # Menu
    while True:
        print("\n===== MAIN MENU =====")
        print("1. Add Password")
        print("2. View All Passwords")
        print("3. Update Password")
        print("4. Delete Password")
        print("5. Exit")

        choice = input("\nChoose (1-5): ")

        if choice == "1":
            manager.add_password()
        elif choice == "2":
            manager.view_passwords()
        elif choice == "3":
            manager.update_password()
        elif choice == "4":
            manager.delete_password()
        elif choice == "5":
            print("\nGoodbye! Your data is saved in 'passwords.db'")
            manager.db.close()
            break
        else:
            print("❌ Invalid choice! Try again.")
