import os
from library.flask_pi_iot_app import app

if __name__ == '__main__':
    app.debug = True
#    host = os.environ.get('IP','127.0.0.1')
    host = os.environ.get('IP', '192.168.137.179')
    port = int( os.environ.get('Port', 8080))
    app.run(host=host, port=port)
