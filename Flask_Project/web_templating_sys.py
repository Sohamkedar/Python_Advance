from flask import *
app = Flask(__name__)

@app.route('/')
def index():
    return "Home of Web"

@app.route('/test1')
def task1():
    name="PYTHON"
    return render_template('test1.html', a=name)

@app.route('/test2')
def task2():
    num=120
    return render_template('test2.html', num=num)

@app.route('/test3')
def task3():
    stu_list=[1,"Hello",3.5]
    return render_template('test3.html', stu_list=stu_list)

@app.route('/test4')
def task4():
    stu_list1={"id":"101","name":"python","City":"Pune"}
    return render_template('test4.html', stu_list1=stu_list1)

if __name__ == '__main__':
    app.run(debug=True)