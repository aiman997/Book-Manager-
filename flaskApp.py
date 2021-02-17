from flask import Flask, redirect, url_for, request, render_template, make_response
from sqlite import DB


app = Flask(__name__)
db=DB()

db.open()
try:
    db.createTable()
except:
    print("Table already created before")

@app.route('/')
def base():
    return render_template('base.html')

@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/addnew')
def new_book():
    return render_template('newbook.html')


@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            id = request.form['id']
            name = request.form['name']
            place = request.form['place']
            authname = request.form['authname']
            publish = request.form['publish']
            msg = db.addBook(id, name, place, authname, publish)
            print(msg)
        except:
             msg = "[flask][addrec] Major failure"
        finally:
            db.printTable()
        return render_template("result.html", msg = msg)

@app.route('/list')
def list():
    rows = db.getRows()
    return render_template("list.html",rows = rows)


if __name__ == '__main__':
    app.run(debug = True)
    db.close()
