""" Database """
from app import db


class CountriesBase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country_names = db.Column(db.String(50), unique=True)
    country_label_name = db.Column(db.String(50), unique=True)
    country_map_cordinate = db.Column(db.Integer)
    country_green_number = db.Column(db.Integer)


