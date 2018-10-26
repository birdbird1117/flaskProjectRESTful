import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

# use integer primary key instead of int, to auto increament id
create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"

cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items (name text, price real)"

cursor.execute(create_table)

connection.commit()

connection.close()
