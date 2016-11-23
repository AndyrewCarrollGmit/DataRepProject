import random
import string
from flask import Flask, request,render_template

app = Flask(__name__)

#Function with parameter x value of 10
def generatePassword(x = 8):
    #concatenate Ascii letters and Numbers
    return ''.join(random.choice( string.ascii_letters + string.digits) for x in range(int(x)))
#Get Data From index.html
@app.route('/', methods=['GET', 'POST'])
#https://github.com/jmoswalt/passwordgen/blob/master/app.py --> used to help with function of generator
#Generate Password And Post From HTML Page
def passGen():
    x = request.form.get('x')
    createPassword = generatePassword()
    generate = {'passwordGen': createPassword, '': x}
    return render_template('index.html', **generate)


if __name__ == "__main__":
    app.run()




