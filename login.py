import sqlite3
import hashlib

#connecting to the database or create one if it doesn't exist
connection  = sqlite3.connect("userdata.db")
#cursor is for interaction with the database
cursor = connection.cursor()

#creating a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS userdata (
    id INTEGER PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
)         
""")


username1, password1 = "martina123", hashlib.sha256("yepyupyip".encode()).hexdigest()
username2, password2 = "thatguy", hashlib.sha256("iceymike".encode()).hexdigest()
username3, password3 = "zinkonvit", hashlib.sha256("moneydozer".encode()).hexdigest()
username4, password4 = "gugugaga", hashlib.sha256("oogabooga".encode()).hexdigest()


cursor.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username1, password1))
cursor.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username2, password2))
cursor.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username3, password3))
cursor.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username4, password4))

connection.commit()
