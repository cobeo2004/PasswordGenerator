# Module
import sqlite3

# Database constants
# Change this everytime
DATABASE_PATH = '/Users/cobeo/Desktop/Codes/SideShits/PasswordGenerator/src/Saves/usr.sqlite'
connections = sqlite3.connect(DATABASE_PATH)

cursor = connections.cursor()
