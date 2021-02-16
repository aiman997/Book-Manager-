from flask import Flask, redirect, url_for, request, render_template, make_response
from sqlite import DB
import sqlite3 as sql
import sqlite3
app = Flask(__name__)
db=DB()

db.open()
try:
    db.createTable()
except:
    print("Table already created before")

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
            db.close()
        return render_template("result.html", msg = msg)

@app.route('/list')
def list():
    con = sql.connect("datab.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from FlaskBooks")

    rows = cur.fetchall();
    return render_template("list.html",rows = rows)

if __name__ == '__main__':
   app.run(debug = True)
