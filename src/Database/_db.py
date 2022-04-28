import sqlite3
import sys
from _const import connections
try:
    cursor = connections.cursor()

    cursor.execute("""DROP TABLE userPassword;""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS userPassword (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        userName TEXT NOT NULL,
        firstName TEXT NOT NULL,
        lastName TEXT NULL,
        savedPassword TEXT NOT NULL,
        email TEXT NOT NULL,
        website TEXT NOT NULL,
        application TEXT NOT NULL,
        date TEXT NOT NULL
    );""")
    connections.commit()
    connections.close()

except sqlite3.Error as E:
    sys.stdout.write(f"Error: {E}")
    sys.stdout.flush()
    sys.exit(1)

finally:
    sys.stdout.write('\nSuccessfully completed the process...')
    sys.exit(1)
