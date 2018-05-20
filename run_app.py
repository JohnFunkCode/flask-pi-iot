import os
from library.flask_pi_iot_app import app

if __name__ == '__main__':
    app.debug = True
#    host = os.environ.get('IP','127.0.0.1')
#    host = os.environ.get('IP','10.10.10.14')
    host = os.environ.get('IP','0.0.0.0') #cloud foundry uses 0.0.0.0 to listen to all IPs
    port = int( os.environ.get('Port',8080))
    app.run(host=host, port=port)
