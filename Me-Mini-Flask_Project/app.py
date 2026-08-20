import re
from flask import *
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
    return "<script>alert('Registration successful'); window.location.href='/reg';</script>"

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True, port=9000)