from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

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
