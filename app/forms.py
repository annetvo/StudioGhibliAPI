from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DecimalField, PasswordField
from wtforms import validators
from wtforms.validators import DataRequired, Email, EqualTo


class submitMovie(FlaskForm):
    movie = StringField('Movie', validators=[DataRequired()])
    protagonist = StringField('Protagonist', validators=[DataRequired()])
    antagonist = StringField('Antagonist', validators=[DataRequired()])
    other_characters = StringField('Other Characters')
    movie_released = IntegerField('Movie Released', validators=[DataRequired()])
    actor = IntegerField("Number of Actors/Actresses")
    submit_button = SubmitField('Submit')


class signInForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField()


class signUpForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('E-Mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    submit = SubmitField()


class updateUser(FlaskForm):
    newusername = StringField('New Username')
    currentpassword = StringField('Current Password', validators=[DataRequired()])
    newpassword = StringField('New Password')
    confirm_newpassword = StringField('Confirm New Password', validators=[EqualTo('newpassword')])
    submit = SubmitField()