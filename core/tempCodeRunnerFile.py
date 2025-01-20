from encryption import Encryption
from database import Database
import os

# if os.system() == 'Windows':
data_filepath = os.getenv("LOCALAPPDATA")
print(data_filepath)