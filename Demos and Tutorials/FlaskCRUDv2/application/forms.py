from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import Users
from flask_login import current_user


class AddGameForm(FlaskForm):
    name = StringField('Game Name', validators=[DataRequired(), Length(min=2, max=30)])
    submit = SubmitField('Add Game')


class UpdateGameForm(FlaskForm):
    oldname = StringField('Old Game Name', validators=[DataRequired(), Length(min=2, max=30)])
    newname = StringField('New Game Name', validators=[DataRequired(), Length(min=2, max=30)])
    submit = SubmitField('Update Game')

class DeleteGameForm(FlaskForm):
    name = StringField('Game Name', validators=[DataRequired(), Length(min=2, max=30)])
    submit = SubmitField('Delete Game')


class RegistrationForm(FlaskForm):
    first_name = StringField('First Name',
                             validators=[
                                 DataRequired(),
                                 Length(min=4, max=30)
                             ]
                             )

    last_name = StringField('Last Name',
                            validators=[
                                DataRequired(),
                                Length(min=4, max=30)
                            ]
                            )
    email = StringField('Email',
                        validators=[
                            DataRequired(),
                            Email()
                        ]
                        )
    password = PasswordField('Password',
                             validators=[
                                 DataRequired(),
                             ]
                             )
    confirm_password = PasswordField('Confirm Password',
                                     validators=[
                                         DataRequired(),
                                         EqualTo('password')
                                     ]
                                     )
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = Users.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('Email already in use')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[
                            DataRequired(),
                            Email()
                        ])
    password = PasswordField('Password',
                             validators=[
                                 DataRequired(),
                             ])
    remember = BooleanField('Remember Me')

    submit = SubmitField('Login')