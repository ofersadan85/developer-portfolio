import sqlite3

def create_db():
    db = sqlite3.connect("data.db")
    cursor = db.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY NOT NULL,
                username TEXT UNIQUE NOT NULL
    )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY NOT NULL,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                created TEXT,
                user_id INTEGER
    )""")

    cursor.execute("INSERT INTO users (username) VALUES ('abc')")
    cursor.execute("INSERT INTO users (username) VALUES ('def')")

    cursor.execute("INSERT INTO posts (title, content, user_id) VALUES ('i love python', 'very much', 1)")
    cursor.execute("INSERT INTO posts (title, content, user_id) VALUES ('title2', 'content2', 1)")
    cursor.execute("INSERT INTO posts (title, content, user_id) VALUES ('title3', 'content3', 1)")
    cursor.execute("INSERT INTO posts (title, content, user_id) VALUES ('title4', 'content4', 2)")
    cursor.execute("INSERT INTO posts (title, content, user_id) VALUES ('title5', 'content5', 2)")

    db.commit()

