from flask import *
app = Flask(__name__)

@app.route('/login/<val>')
def login(val):
   if val == "stud_dash":
       return redirect(url_for("stud"))  

   elif val == "hr_dash":
       return redirect(url_for("hr"))
   else:
       return "page not found"

@app.route('/stud_dash')
def stud():
   return "This is Student dashboard"

@app.route('/hr_dash')
def hr():
   return "This is HR dashboard"
  
if __name__ == '__main__':
    app.run(debug=True)