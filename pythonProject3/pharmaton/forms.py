from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, SubmitField, PasswordField, FloatField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from pharmaton.models import User


class RegistrationForm(FlaskForm):
    medname = StringField('Medicine Name', validators=[DataRequired()])
    efficiency = IntegerField('Efficiency', validators=[DataRequired()])
    sideeffect = StringField('Sideeffect', validators=[DataRequired()])
    typemed = StringField('Medicine Type', validators=[DataRequired()])
    cmpname = StringField('Company Name', validators=[DataRequired()])
    disease = StringField('Disease', validators=[DataRequired()])
    expdate = DateField('Expiry Date', format='%m-%Y', validators=[DataRequired()])
    mfgdate = DateField('Manufacturing Date', format='%m-%Y', validators=[DataRequired()])
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit  = SubmitField('Submit')


class AdminForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[EqualTo('password')])
    submit = SubmitField('Submit')

    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('That email is taken.Please choose a different one.')


class SalesForm(FlaskForm):
    price = FloatField('Price', validators=[DataRequired()])
    does_available = IntegerField('Does Available', validators=[DataRequired()])
    dose_sale = IntegerField('Does Sale', validators=[DataRequired()])
    medname = StringField('Medicine Name', validators=[DataRequired()])
    profit = IntegerField('Profit', validators=[DataRequired()])
    submit = SubmitField('Submit')


class DepartureForm(FlaskForm):
    ref_no = IntegerField('Ref No', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    medname = StringField('Medicine Name', validators=[DataRequired()])
    depid = IntegerField('Departure Id', validators=[DataRequired()])
    vehicleno = StringField('Vehicle No', validators=[DataRequired()])
    submit = SubmitField('Submit')


class DiseaseForm(FlaskForm):
    disease = StringField('Disease', validators=[DataRequired()])
    submit = SubmitField('Add Disease')