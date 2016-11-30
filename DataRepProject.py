from flask import Flask, render_template
from flask import request
import random
import string
import sqlite3

# https://github.com/data-representation/example-sqlite/blob/master/webapp.py

# http://flask.pocoo.org/docs/0.11/appcontext/#purpose-of-the-application-context --> Help Connect to database

DATABASE = 'emails.db'
app = Flask(__name__)


def get_db():
    db = getattr(Flask.g, '_database', None)
    if db is None:
        db = Flask.g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(Flask.g, '_database', None)
    if db is not None:
        db.close()


# Function y value of 10
def randomisePassword(y=10):
    # concatenate Ascii letters and Numbers
    return ''.join(random.choice(string.ascii_letters + string.digits) for x in range(int(y)))


# routing to index
@app.route('/index')
def home():
    return render_template('index.html')


# Routing to feedback page
@app.route('/feedback')
def feedback():
    return render_template('feedback.html')


# Route to index.html
@app.route('/', methods=['GET', 'POST'])
# https://github.com/jmoswalt/passwordgen/blob/master/app.py --> used to help with function of generator

# Generate Password
def generatePassword():
    # Retrieves the values of form elements
    y = request.form.get('y') or '12'
    createPassword = randomisePassword(y)
    # Password Length Between 7-14 characters
    passwordLength = [str(x) for x in range(7, 15)]
    generate = {'passwordGen': createPassword, 'y': y, 'pass': passwordLength}
    # Render Python To Html Page with generated password
    return render_template('index.html', **generate)


# Route to feedback.html
@app.route('/feedback', methods=['GET', 'POST'])
def submitEmail():
    cur = get_db().cursor()
    cur.execute("SELECT email FROM email_addresses")
    return str(cur.fetchall())


if __name__ == "__main__":
    app.run()
