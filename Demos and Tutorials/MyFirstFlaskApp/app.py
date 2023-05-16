from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route('/secret_page/<code_number>')
def secret_page(code_number):
    if code_number != "1234":
        return redirect(url_for('not_secret_page'))
    else:
        return 'Welcome to the secret page'

@app.route('/not_secret_page')
def not_secret_page():
    return "Some not secret stuff"

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return 'This is a POST request'
    else:
        return 'This is a GET request'

@app.route('/Upper/<word>')
def get_upper(word):
    return word.title()

@app.route('/factorial/<int:number>')
def get_factorial(number):
    result = do_calc(number)
    return str(result)

def do_calc(number):
    i = int(number)
    result = 1
    while i > 0:
        result = result * i
        i -= 1
    return result


@app.route('/Capitalize/<phrase>')
def get_capitalize_phrase(phrase):
    phrase = phrase.capitalize()
    return phrase

@app.route('/IsItCoffeeTime')
def coffee_time_decider():

    return "Yes of course, it is coffee time"

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)