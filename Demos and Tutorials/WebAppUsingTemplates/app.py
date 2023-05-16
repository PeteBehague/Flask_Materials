from flask import Flask, request, redirect, url_for, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, DecimalField, SelectField, SubmitField
from decimal import ROUND_HALF_UP
from wtforms.validators import DataRequired, Length, ValidationError

app = Flask(__name__)
app.config['SECRET_KEY'] = 'EZnGuIDI91sVBQkbOb-uzg'


@app.route('/')
@app.route('/home')
def home():
    return render_template('layout.html')


def begins_with_b(name):
    if name[0] == 'B':
        return True
    else:
        return False


@app.route('/page1/<user_names>')
def page1(user_names):
    list_of_users = user_names.title().split(',')
    b_list_of_users = list(filter(lambda user: user[0] == 'B', list_of_users))
    b_string_of_users = ', '.join(b_list_of_users)
    return render_template('page1.html', users=list_of_users, b_users=b_string_of_users)


@app.route('/page2/<name>')
def page2(name):
    return render_template('page2.html', username=name)


class UserCheck:
    def __init__(self, banned, message=None):
        self.banned = banned
        if not message:
            message = "Please enter another user name"
        self.message = message

    def __call__(self, form, field):
        if field.data.lower() in (word.lower() for word in self.banned):
            raise ValidationError(self.message)


class UserInfo(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(),
                                                       UserCheck(message="The username is not allowed",
                                                                 banned=['root', 'admin', 'sys']),
                                                       Length(min=2, max=15)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=5, max=20)])
    dob = DateField('Date of Birth')
    favourite_number = DecimalField('Favourite Number', places=2, rounding=ROUND_HALF_UP)
    favourite_food = SelectField('Favourite Food',
                                 choices=[('USA', 'fried-chicken'), ('ITY', 'spaghetti'), ('MEX', 'Chilli')])
    submit = SubmitField('Add User')


@app.route('/adduser', methods=['GET', 'POST'])
def add_user():
    message = ""
    add_user_form = UserInfo()

    if request.method == 'POST':
        if add_user_form.validate_on_submit():
            first_name = add_user_form.first_name.data
            last_name = add_user_form.last_name.data
            dob = add_user_form.dob.data
            favourite_number = add_user_form.favourite_number.data
            favourite_food = add_user_form.favourite_food.data

            message = f"Welcome {first_name} {last_name}. You were born on {dob}, " \
                      f"your favourite number is {favourite_number} and your favourite food is {favourite_food}."
        else:
            message = ""
    else:
        message = ""
        add_user_form.first_name.data = ""
        add_user_form.last_name.data = ""
        add_user_form.favourite_number.data = 0

    return render_template('adduser.html', form=add_user_form, message=message)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5020)
