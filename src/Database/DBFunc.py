#Module
import sqlite3
from src.Database._const import connections,cursor
# from _const import connections,cursor
from datetime import datetime

#A function that add informations to the sqlite database
def addDataToDatabase(__userName: str, __savedPassword: str, __email: str, __firstName: str, __website: str , __application: str, __lastName: str = ""):
    try:
        cursor.execute("""INSERT INTO userPassword (userName, savedPassword, firstName, lastName, email, website, application, date) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", (str(__userName), str(__savedPassword), str(__firstName), str(__lastName), str(__email), str(__website), str(__application), str(datetime.now())))
        connections.commit()
        connections.close()
        return True
    except sqlite3.Error as E:
        print(f"Error: {E}")
        return False

#A function that get informations from the sqlite database
def getFromDatabase(__userName: str, __firstName: str, __email:str, __website: str, __application:str ):
    try:
        cursor.execute("""
        SELECT userName, firstName, lastName, savedPassword, email, website, application 
        FROM userPassword
        WHERE userName=? AND firstName=? AND email=? AND website=? AND application=?;     
        """, (str(__userName), str(__firstName), str(__email), str(__website), str(__application)))
        connections.commit()
        return [d for d in cursor.fetchone()]
    except sqlite3.Error as E:
        print(f"Error: {E}")
        return None
