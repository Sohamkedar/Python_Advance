from flask import *
app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('welcome'))

@app.route('/Welcome')
def welcome():
    return "Welcome to Flask"


if __name__ == '__main__':
    app.run(debug=True)