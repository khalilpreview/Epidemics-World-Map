import requests
import json
from googletrans import Translator
from flask import Flask , render_template , redirect , url_for , request

# Flask app initialisation
app = Flask(__name__)
# create an object of translater class
translator = Translator()

# routes and views start here.
# ...
# home the index route and view
# registration  route and view

@app.route('/')
def gen_home_page():
    title = 'Welcome to E-W-M'
    return render_template('home.html' , title=title)




@app.route('/<country_name>', methods=['GET' , 'POST'])
def home_page(country_name):
    title = 'E-W-M'

    url_world = 'https://covid2019-api.herokuapp.com/v2/total'
    url_country = 'https://covid2019-api.herokuapp.com/v2/country/' + country_name

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
    country_date_of_update = country_data.json()['dt']
    

    

    
    print(world)
    print(country)

    return render_template('index.html' , world_confirmed_cases = world_confirmed_cases ,
                                          world_confirmed_deaths = world_confirmed_deaths ,  
                                          world_confirmed_recovers = world_confirmed_recovers ,
                                          world_confirmed_active =world_confirmed_active ,
                                          country_confirmed_cases =  country_confirmed_cases ,
                                          country_confirmed_deaths = country_confirmed_deaths ,
                                          country_confirmed_recovers = country_confirmed_recovers ,
                                          counrty_location = counrty_location ,
                                          country_date_of_update = country_date_of_update ,
                                          country_name = country_name ,
                                          translator = translator ,
                                          title=title)



# registration  route and view
@app.route('/register')
def register_page():
    title = 'Registration E-W-M'
    return render_template('registration.html' , title=title)

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



if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)