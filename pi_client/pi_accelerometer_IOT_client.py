# Import the ADXL345 module.
import Adafruit_ADXL345
import requests
import time
import datetime

class PiAccelerometerIOTClient:
    '''A class to represent the accelerometer circuit board we built for the raspberry pi'''

    #_accel = Adafruit_ADXL345.ADXL345()
    #_serial = ''
    #_server_destinations = ['http://jpf-flask-pi-iot.cfapps.io/test','http://10.10.10.14:8080/test']

    def getserial(self):
      # Extract serial from cpuinfo file
      cpuserial = "0000000000000000"
      try:
        f = open('/proc/cpuinfo','r')
        for line in f:
          if line[0:6]=='Serial':
            cpuserial = line[10:26]
        f.close()
      except:
        cpuserial = "ERROR000000000"
      return cpuserial

    def get_server_destinations(self):
        return self._server_destinations

    def test_servers(self):
        print("Testing reaching the following servers:")
        # send a simple get to the list of servers
        for server in self._server_destinations:
            print("Posting to {0}".format(server))
            r = requests.get(server)

    def post_data(self):
        while True:
            # get the data
            x,y,z=self._accel.read()
            print('X={0}, Y={1}, Z={2}'.format(x, y, z))

            #format it to send to server
            ts=datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
            aData={'serial-no':self._serial,'timestamp':ts,'x':x,'y':y,'z':z}

            #send it to the list of servers
            for server in self._server_destinations:
                print("Posting to {0}".format(server))
                r=requests.post(server,data=aData)

    def __init__(self):
        print("Initializing")
        self._serial = self.getserial()
        self._accel = Adafruit_ADXL345.ADXL345()
        self._server_destinations = ['http://jpf-flask-pi-iot.cfapps.io/test','http://10.10.10.14:8080/test']


if __name__ == "__main__":
    PiAccererometer=PiAccelerometerIOTClient()

    print('My serial number is {0}'.format(PiAccererometer.getserial()))

    PiAccererometer.test_servers()

    PiAccererometer.post_data()
