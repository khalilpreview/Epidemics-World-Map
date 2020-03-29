import os
from app import app


if __name__ == '__main__':
    app.debug = True
    host = os.environ.get('IP', '192.168.1.9')
    port = int(os.environ.get('PORT', 8880))
    app.run(host=host, port=port)