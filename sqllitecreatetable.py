import sqlite3

# Connecting to the database file
conn = sqlite3.connect('data.db')
c = conn.cursor()

# Creating a new SQLite table with 1 column
c.execute('CREATE TABLE users (userid int PRIMARY KEY, username text, active bool)')

conn.commit()
conn.close()