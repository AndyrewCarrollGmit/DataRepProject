import sqlite3

#https://github.com/data-representation/example-sqlite/blob/master/webapp.py --> used to help with database connection
#http://opentechschool.github.io/python-flask/extras/databases.html --> also used for database connection

DATABASE = 'DataRepProject/emails.db'

def setup_db():
    #Creates Databse
  db = sqlite3.connect(DATABASE)
  cur = db.cursor()

  # Create the table if it doesn't exist.
  cur.execute("CREATE TABLE IF NOT EXISTS email_addresses( email TEXT)")
  db.commit()

if __name__ == "__main__":
  setup_db()

