from flask import *
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/name/<n>')
def name(n):
    return "Welcome, %s" % n

@app.route('/roll_no/<int:num>')
def roll_no(num):
    return "Your Roll Number is %d" % num

if __name__ == '__main__':
    app.run(debug=True)