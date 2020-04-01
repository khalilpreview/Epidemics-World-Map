"""
You can use that on local runing for testing and development ,
once you deploy the app we lunch our webserver from app.py .
debug mode = True .

"""
import os
from app import app


if __name__ == '__main__':
    app.debug = True
    host = os.environ.get('IP', '192.168.43.68')
    port = int(os.environ.get('PORT', 8880))
    app.run(host=host, port=port)