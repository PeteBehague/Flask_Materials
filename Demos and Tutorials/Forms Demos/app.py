from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, DecimalField, SelectField
from decimal import ROUND_HALF_UP

app = Flask(__name__)
app.config['SECRET_KEY']='cd79428cf8aba6e07c61475993aa5818' #Configure a secret key for CSRF protection.

class BasicForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    dob = DateField('Date of Birth')
    # the parameters only applied to values supplied to be used as starting values (_values function),
    # and not for input (_process_formdata function).
    # So you'll have to roll your own validator. YUCK!
    # see: https://stackoverflow.com/questions/27781926/decimal-field-rounding-in-wtforms
    favourite_number = DecimalField(places = 2, rounding=ROUND_HALF_UP)
    favourite_food = SelectField('Favourite Food', choices = [('US','fried-chicken'), ('Italian', 'spaghetti'), ('Mexican', 'chilli')])
    submit = SubmitField('Add Name')

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def register():
    message = ""
    form = BasicForm()

    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        dob = form.dob.data
        favourite_number = form.favourite_number.data
        favourite_food = form.favourite_food.data

        if len(first_name) == 0 or len(last_name) == 0:
            message = "Please supply both first and last name"
        else:
            message = f'Thank you, {first_name} {last_name}. You were born on {dob}, your favourite number is {favourite_number} and your favourite food is {favourite_food}'

    return render_template('userform.html', form=form, message=message)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5020)