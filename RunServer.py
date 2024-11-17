from flask import *

from DBManager import DBmanager

app = Flask("Kahoot")
db_name = "Site.db"

@app.route("/")
def index():
    db_manager = DBmanager(db_name)
    quizzes = db_manager.get_quizzes()
    return render_template("index.html", quizzes=quizzes)

@app.route("/about_us")
def about_us():
    return render_template("about_us.html")

app.run()