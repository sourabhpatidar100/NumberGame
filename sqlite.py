import sqlite3

#
connection_obj = sqlite3.connect('registration.db')

import sqlite3


connection_obj = sqlite3.connect('game_database.db')
cursor_obj = connection_obj.cursor()


cursor_obj.execute("DROP TABLE IF EXISTS users")

table = """ 
CREATE TABLE users (
    username VARCHAR(255) NOT NULL,
    First_Name CHAR(25) NOT NULL,
    Score INT DEFAULT 100,
    UNIQUE(username)
);
"""
cursor_obj.execute(table)
connection_obj.commit()
print("Table is ready.")
