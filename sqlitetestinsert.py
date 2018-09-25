import sqlite3

# Connecting to the database file
conn = sqlite3.connect('data.db')
c = conn.cursor()
# Insert user 1
c.execute('''INSERT INTO users(userid, username, active)
                  VALUES(?,?,?)''', (3,'warren', True))
print('First user inserted')
 
# Insert user 2
c.execute('''INSERT INTO users(userid, username, active)
                  VALUES(?,?,?)''', (4,'addison', True))
print('Second user inserted')


# users = [(name1,phone1, email1, password1),
#          (name2,phone2, email2, password2),
#          (name3,phone3, email3, password3)]
# cursor.executemany(''' INSERT INTO users(name, phone, email, password) VALUES(?,?,?,?)''', users)
conn.commit()
conn.close()