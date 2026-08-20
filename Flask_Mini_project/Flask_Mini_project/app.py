from flask import *
app=Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/reg")
def registration():
    return render_template("reg.html")

@app.route("/formsave")
def formsave():
    return "Registration Completed Successfully"


if __name__=="__main__":
    app.run(debug=True, port=9900)