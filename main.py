from flask import Flask, render_template, g
import httpx  # pip install httpx    OR     pip install -r requirements.txt
import sqlite3

app = Flask(__name__)

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect("data.db")
        g.db.row_factory = sqlite3.Row
    return g.db


def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

app.teardown_appcontext(close_db)


@app.route("/")
def index():
    username = "yourusername"
    user_details = httpx.get(f"https://api.github.com/users/{username}").json()
    user_repos = httpx.get(user_details["repos_url"]).json()
    user_languages = ", ".join({repo["language"] for repo in user_repos if repo["language"]})
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT posts.title, posts.content FROM users INNER JOIN posts ON users.id = posts.user_id WHERE users.username = ?", [username])
    blog_posts = cursor.fetchall()
    return render_template(
        "index.html",
        age=365,
        blog_posts=blog_posts,
        user_details=user_details,
        user_repos=user_repos,
        user_languages=user_languages
    )


app.run(debug=True)
