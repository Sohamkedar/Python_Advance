import re
from flask import *
import sqlite3 as sq
from db_config import insert_user

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/reg')
def reg():
    return render_template('reg.html')

@app.route("/formsave", methods=["POST"])
def formsave():
    fullname = request.form.get("fullname", "")
    email = request.form.get("email", "")
    contact = request.form.get("contact", "")
    city = request.form.get("city", "")
    password = request.form.get("password", "")

    if len(password) < 8:
        return "Password must be at least 8 characters"

    if not re.search(r"[A-Z]", password):
        return "Password must contain an uppercase letter"

    if not re.search(r"[a-z]", password):
        return "Password must contain a lowercase letter"

    if not re.search(r"[0-9]", password):
        return "Password must contain a number"

    if not re.search(r"[^A-Za-z0-9]", password):
        return "Password must contain a special character"

    insert_user(fullname, email, contact, city, password)
    return "<script>alert('Registration successful'); window.location.href='/viewdata';</script>" 

@app.route('/login')
def login():
    return render_template('login.html')

@app.route("/viewdata")
def viewdata():
    con=sq.connect("flask.db")
    cur=con.cursor()
    data=cur.execute("select * from reg order by id desc")

    con.commit()
    return render_template("viewdata.html",data=data)

@app.route("/deletestudent/<int:id>")
def deletestudent(id):
    con = sq.connect("flask.db")
    cur = con.cursor()

    cur.execute("DELETE FROM reg WHERE id=?", (id,))
    con.commit()
    con.close()

    return redirect(url_for("viewdata"))

@app.route("/updatestudent/<int:id>")
def updatestudent(id):
    con=sq.connect("flask.db")
    cur=con.cursor()
    data=cur.execute("SELECT * FROM reg where id=?",[id])
    data=cur.fetchone()
    con.commit()

    return render_template("update.html", data=data) 

@app.route("/profileupdate", methods=["GET","POST"])
def profileupdate():
    if request.method=="POST":
        id=request.form["id"]
        fullname = request.form["fullname"]
        email = request.form["email"]
        contact = request.form["contact"]
        city = request.form["city"]
        password = request.form["password"]

        con=sq.connect("flask.db")
        cur=con.cursor()
        cur.execute("update reg set fullname=?,email=?,contact=?,city=?,password=? where id=?", (fullname, email, contact, city, password, id))

        con.commit()

        return "<script>alert('updation successful Completed'); window.location.href='/viewdata';</script>"



if __name__ == '__main__':
    app.run(debug=True, port=9000)