import sqlite3 as sq
con=sq.connect("flask.db")
cur=con.cursor()

cur.execute("create table reg(id INTEGER PRIMARY KEY AUTOINCREMENT,fullname varchar(15),email varchar(15),contact varchar(10), city varchar(15),password varchar(10))")

con.commit()
con.close()