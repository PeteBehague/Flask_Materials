from flask import Flask
from flask import request
from flask import redirect
from flask import url_for

app = Flask(__name__)


@app.route('/')
def hello_internet():
    return "Hello Internet!"

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return 'This is a POST request'
    else:
        return 'This is a GET request'

@app.route('/makeUppercase/<word>')
def makeUppercase(word):
    return word.upper()

@app.route('/addTen/<int:number>')
def addTen(number):
    number += 10
    return str(number)

def user_logged_in(word):
    if word == 'Beth Mead':
        return True
    else:
        return False

@app.route('/loginAndRedirect/<word>')
def loginAndRedirect(word):
    if user_logged_in(word) == True:
        return redirect('http://localhost:5000/account')
    else:
        return 'This is a home page'

@app.route('/account')
def account():
    return 'Log in successful. Welcome to the account page'

@app.route('/loginAndRedirectUsingUrlFor/<word>')
def loginAndRedirectUsingUrlFor(word):
    if user_logged_in(word) == True:
        return redirect(url_for('namedAccount', name=word))
    else:
        return 'This is a home page'

@app.route('/namedAccount/<name>')
def namedAccount(name):
    return f'Log in for {name} successful. Welcome to the account page'

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)