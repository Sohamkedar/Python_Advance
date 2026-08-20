import sqlite3 as sq

def init_db():
    con = sq.connect("flask.db")
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS reg (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fullname VARCHAR(15),
            email VARCHAR(15),
            contact VARCHAR(10),
            city VARCHAR(15),
            password VARCHAR(10)
        )
    """)
    con.commit()
    con.close()

def insert_user(fullname, email, contact, city, password):
    con = sq.connect("flask.db")
    cur = con.cursor()
    cur.execute(
        "INSERT INTO reg (fullname, email, contact, city, password) VALUES (?, ?, ?, ?, ?)",
        (fullname, email, contact, city, password)
    )
    con.commit()
    con.close()

if __name__ == "__main__":
    init_db()
