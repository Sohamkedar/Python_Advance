from flask import Flask
app = Flask(__name__) 

@app.route('/')
def home():
    return "Flask Home Page"

@app.route('/about')
def about():
    return "I am Flask About Page"

@app.route('/contact')
def contact():
    return "Contact Page"

@app.route('/Login')
def login():
    return "<h1>Login Page</h1>"

if __name__ == '__main__':
    app.run(debug=True)