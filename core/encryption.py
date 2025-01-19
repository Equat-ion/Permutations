from cryptography.fernet import Fernet

class Encryption:
    
    def __init__(self,key=None):
        if key:
            self.cipher = Fernet(key)
        else:
            raise ValueError("A Valid key must be provided")
        
    def encrypt(self, data: str) -> str:
        data_bytes = data.encode()
        encrypted_data = self.cipher.encrypt(data_bytes)

        return encrypted_data.decode()
    
    def decrypt(self, data: str) -> str:
        encrypted_data_bytes = data.encode()
        decrypted_data = self.cipher.decrypt(encrypted_data_bytes)

        return decrypted_data.decode()
    
    @staticmethod
    def keygen():
        key = Fernet.generate_key()
        return key.decode()
    

"""Class test"""

# key = Encryption.keygen()
# print("Generated Key:", key)
# encryption = Encryption(key)
# encrypted = encryption.encrypt("myPassword123")
# print("Encrypted:", encrypted)
# decrypted = encryption.decrypt(encrypted)
# print("Decrypted:", decrypted)

print(Encryption(key="lol"))