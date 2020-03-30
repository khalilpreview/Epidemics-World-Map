from flask_wtf import FlaskForm
from wtforms import SelectField , SubmitField 
from wtforms.validators import InputRequired


class SelectCountryForm(FlaskForm):
    select_country = SelectField(u'Chose a country:', choices=[('', 'Chose a country') ,('algeria', 'Algeria') ,('italy', 'Italy'),('china', 'China')], validators=[InputRequired()])
    submit = SubmitField('Get')
