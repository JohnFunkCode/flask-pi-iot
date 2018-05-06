import os
from library.flask_rest_test_app import app

if __name__ == '__main__':
    app.debug = True
#    host = os.environ.get('IP','127.0.0.1')
    host = os.environ.get('IP','10.10.10.14')
    port = int( os.environ.get('Port',8080))
    app.run(host=host, port=port)
