import random
import string
from flask import Flask

app = Flask(__name__)

#Function with value of 10
def generatePassword(x = 10):
    #concatenate Ascii letters and Numbers
    return ''.join(random.sample( string.ascii_letters + string.digits) for x in range(int(x)))
#Get Data From index.html
@app.route('/', methods=['GET', 'POST'])

#Generate Password And Post From Index Page
def passGen():
    x = request.form.get('x')
    createPassword = generatePassword()
    generate = {'passwordGen': createPassword, '': x}
    return render_template('index.html', **generate)


if __name__ == "__main__":
    app.run()