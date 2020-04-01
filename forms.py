from flask_wtf import FlaskForm
from wtforms import SelectField , SubmitField 
from wtforms.validators import InputRequired


class SelectCountryForm(FlaskForm):
    select_country = SelectField(u'Chose a country:', choices=[('', 'Chose a country') ,('algeria', 'Algeria') ,('morocco', 'Morocco'),('tunisia', 'Tunisia'),('us', 'United States'),('italy', 'Italy'),('spain', 'Spain'),('china', 'China'),('germany', 'Germany'),('france', 'France'),('iran', 'Iran'),('united kingdom', 'United Kingdom'),('switzerland', 'Switzerland'),('belgium', 'Belgium'),('indonesia', 'Indonesia')], validators=[InputRequired()])
    submit = SubmitField('Get')
