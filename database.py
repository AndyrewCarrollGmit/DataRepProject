import sqlite3

# https://github.com/data-representation/example-sqlite/blob/master/webapp.py --> Used to Help create database

DATABASE = 'emails.db'


def setup_db():
    #Connect to database
    db = sqlite3.connect(DATABASE)
    cur = db.cursor()
    # Create The Table
    cur.execute("CREATE TABLE IF NOT EXISTS email_addresses ( email TEXT );")
    db.commit()

    # Insert some dummy data if the table is empty.
    cur.execute("SELECT COUNT(*) FROM email_addresses")
    if cur.fetchall()[0][0] == 0:
        cur.execute('INSERT INTO email_addresses(name) VALUES("123@gmail.com")')
        db.commit()


if __name__ == "__main__":
    setup_db()
