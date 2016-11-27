import flask
from flask import Flask, request,render_template
import random
import string
import sqlite3

DATABASE = 'DataRepProject/emails.db'


app = Flask(__name__)

def get_db():
  db = getattr(flask.g, 'database', None)
  if db is None:
    db = flask.g._database = sqlite3.connect(DATABASE)
  return db

@app.teardown_appcontext
def close_connection(exception):
  db = getattr(flask.g, 'database', None)
  if db is not None:
    db.close()

@app.route("/")
def emailAddress():
    cur = get_db().cursor()
    cur.execute("SELECT email FROM email_addresses")
    return str(cur.fetchall())

#Function with parameter x value of 10
def randomisePassword(y = 10):
    #concatenate Ascii letters and Numbers
    return ''.join(random.choice( string.ascii_letters + string.digits) for x in range(int(y)))


#Get Data From index.html
@app.route('/', methods=['GET', 'POST'])


# https://github.com/jmoswalt/passwordgen/blob/master/app.py --> used to help with function of generator
# Generate Password And Post From HTML Page
def generatePassword():
    y = request.form.get('y') or '10'
    createPassword = randomisePassword(y)
    passwordLength = [str(x) for x in range(7, 15)]
    generate = {'passwordGen': createPassword,'y': y, 'pass': passwordLength}
    return render_template('index.html', **generate)

if __name__ == "__main__":
    app.run()




