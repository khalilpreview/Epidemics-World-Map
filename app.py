import os
import urllib
import requests
import json
#from googletrans import Translator
from flask import Flask , render_template , redirect , url_for , request , make_response
from flask_sqlalchemy import SQLAlchemy
from forms import *


# Flask app initialisation
app = Flask(__name__)
db = SQLAlchemy(app)

from models import *

# App configuration
app.config['SECRET_KEY'] = 'V7lyCbdHp1lKc24QbEhMexbnUsKHNxYi'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

# create an object of translater class
# google translator integrated
# translator = Translator()

# routes and views start here.
# ...

# home  route and view
@app.route('/' , methods=['GET','POST'])
def gen_home_page():
    title = 'Welcome to E-W-M'
    form = SelectCountryForm()

    # get the link + country nameafter submited
    if form.validate_on_submit():
        country = '/mapping/' + form.select_country.data 
        return redirect(country)

    return render_template('home.html' , form=form ,title=title)



# the home of map
@app.route('/mapping/<country_name>', methods=['GET' , 'POST'])
def home_page(country_name):
    title = 'E-W-M'
    country_info = CountriesBase.query.filter_by(country_names = country_name ).first()
    co = country_info.country_map_cordinate
    cordinate = co.split()

    url_world = 'https://covid2019-api.herokuapp.com/v2/total'
    url_country = 'https://covid2019-api.herokuapp.com/v2/country/' + country_name
    url_country_that_infected = 'https://covid2019-api.herokuapp.com/countries'


    world_data = requests.get(url_world)
    world = world_data.json()['data']
    world_confirmed_cases = world['confirmed']
    world_confirmed_deaths = world['deaths']
    world_confirmed_recovers = world['recovered']
    world_confirmed_active = world['active']

    country_data = requests.get(url_country)
    country = country_data.json()['data']
    counrty_location = country['location']
    country_confirmed_cases = country['confirmed']
    country_confirmed_deaths = country['deaths']
    country_confirmed_recovers = country['recovered']
    country_confirmed_active = country['active'] 
    country_date_of_update = country_data.json()['dt']
    
    inf_country = requests.get(url_country_that_infected)
    infected_country = inf_country.json()['countries']
    infected_country_number = len(infected_country)

   
    

    return render_template('index.html' , world_confirmed_cases = world_confirmed_cases ,
                                          world_confirmed_deaths = world_confirmed_deaths ,  
                                          world_confirmed_recovers = world_confirmed_recovers ,
                                          world_confirmed_active =world_confirmed_active ,
                                          country_confirmed_cases =  country_confirmed_cases ,
                                          country_confirmed_active = country_confirmed_active ,
                                          country_confirmed_deaths = country_confirmed_deaths ,
                                          country_confirmed_recovers = country_confirmed_recovers ,
                                          infected_country_number = infected_country_number ,
                                          counrty_location = counrty_location ,
                                          country_date_of_update = country_date_of_update ,
                                          country_name = country_name ,
                                          country_info = country_info ,
                                          cordinate = cordinate ,
                                          title=title)


# login route and view
@app.route('/login')
def registeration_page():
    title = 'Login E-W-M'
    return render_template('login.html' , title=title)

# dashboard route and view
@app.route('/dashboard')
def dashboard_page():
    title = 'Dashboard E-W-M'
    return render_template('dashboard.html' , title=title)

"""
# registration  route and view
@app.route('/webhook' , methods=['POST'])
def webhook():
    title = 'webhook'

    if request.method == "POST":
        req = request.get_json(silent=True , force=True)
        res = processRequest(req)
        res = json.dumps(res, indent=4)
        r = make_response(res)
        r.headers['Content-Type'] = 'application/json'
        return r

def processRequest(req):

    # Get all the Query Parameter
    query_response = req["queryResult"]
    print(query_response)
    text = query_response.get('queryText', None)
    parameters = query_response.get('parameters', None)

    res = get_data()

    return res


def get_data():

    speech = ""

    return {
        "fulfillmentText": speech,
    }

"""



if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
