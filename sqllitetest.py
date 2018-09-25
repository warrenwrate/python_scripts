import sqlite3

# Connecting to the database file
conn = sqlite3.connect('data.db')
c = conn.cursor()


c.execute("UPDATE {tn} SET {cn}='Maximus' WHERE {idf}=3".format(tn='users', cn='username', idf='userid'))

c.execute('''SELECT * FROM users''')
user1 = c.fetchone() #retrieve the first row
print(user1[0], user1[1]) #Print the first column retrieved(user's name)

user2 = c.fetchone() #retrieve the first row
print(user2[0], user2[1]) #Print the first column retrieved(user's name)

all_rows = c.fetchall()
for row in all_rows:
    # row[0] returns the first column in the query (name), row[1] returns email column.
    print('userid:{0} username:{1}, active:{2}'.format(row[0], row[1], row[2]))

# C) Updates the newly inserted or pre-existing entry            
c.execute("UPDATE {tn} SET {cn}='Maximus' WHERE {idf}=3".format(tn='users', cn='username', idf='userid'))

# Committing changes and closing the connection to the database file


c.execute('SELECT * FROM {tn} WHERE {cn}="Maximus"'.
format(tn='users', cn='username'))
all_rows = c.fetchall()

conn.close()