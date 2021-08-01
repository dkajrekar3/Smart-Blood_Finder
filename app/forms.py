from app.models import Donor
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField, RadioField, DateField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length


class RegistrationForm(FlaskForm):
    username = StringField('Full Name ', validators=[
                           DataRequired(), Length(min=2, max=30)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[
                                     DataRequired(), EqualTo('password')])
    contact = StringField('Contact', validators=[
                          DataRequired(), Length(min=10, max=13)])
    state = StringField('State', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    pincode = StringField('Pincode', validators=[DataRequired()])
    bloodgroup = SelectField('Blood Group', choices=[('a+', 'A+'), ('b+', 'B+'), ('o+', 'O+'), (
        'ab+', 'AB+'), ('a-', 'A-'), ('o-', 'O-'), ('b-', 'B-'), ('ab-', 'AB-')], validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    weight = IntegerField('Weight', validators=[DataRequired()])
    gender = RadioField('Gender', choices=[
                        ('m', 'MALE'), ('f', 'FEMALE')], validators=[DataRequired()])
    lastdonation = StringField(
        'Last donation date', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = Donor.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(
                'The username is taken, Please choose different Username.')

    def validate_email(self, email):
        user = Donor.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(
                'The email is taken, Please choose different Email.')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class UpdateForm(FlaskForm):
    username = StringField('Full Name ', validators=[
                           DataRequired(), Length(min=2, max=30)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    contact = StringField('Contact', validators=[
                          DataRequired(), Length(min=10, max=13)])
    state = StringField('State', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    pincode = StringField('Pincode', validators=[DataRequired()])
    bloodgroup = SelectField('Blood Group', choices=[('a+', 'A+'), ('b+', 'B+'), ('o+', 'O+'), (
        'ab+', 'AB+'), ('a-', 'A-'), ('o-', 'O-'), ('b-', 'B-'), ('ab-', 'AB-')], validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    weight = IntegerField('Weight', validators=[DataRequired()])
    gender = RadioField('Gender', choices=[
                        ('m', 'MALE'), ('f', 'FEMALE')], validators=[DataRequired()])
    lastdonation = StringField(
        'Last donation date', validators=[DataRequired()])
    submit = SubmitField('Update')

    def validate_username(self, username):
        user = Donor.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(
                'The username is taken, Please choose different Username.')

    def validate_email(self, email):
        user = Donor.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(
                'The email is taken, Please choose different Email.')

class SearchForm(FlaskForm):
    blood = SelectField('Blood Group', choices=[('#' , 'Select Blood Group'),('a+', 'A+'), ('b+', 'B+'), ('o+', 'O+'), (
        'ab+', 'AB+'), ('a-', 'A-'), ('o-', 'O-'), ('b-', 'B-'), ('ab-', 'AB-')], validators=[DataRequired()])
    city = StringField('city' , validators=[DataRequired()])
    submit=SubmitField('Search')