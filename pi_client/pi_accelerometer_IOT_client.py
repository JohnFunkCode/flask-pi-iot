# Import the ADXL345 module.
import Adafruit_ADXL345
import requests
import time
import datetime

class PiAccelerometerIOTClient:
    '''A class to represent the accelerometer circuit board we built for the raspberry pi'''

    _accel = Adafruit_ADXL345.ADXL345()
    _serial = ''
    _server_destinations = ['http://jpf-flask-pi-iot.cfapps.io']

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

    def post_data(self):
        while True:
            x,y,z=self._accel.read()
            print('X={0}, Y={1}, Z={2}'.format(x, y, z))
            ts=datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
            aData={'serial-no':self._serial,'timestamp':ts,'x':x,'y':y,'z':z}
            r=requests.post('http://192.168.137.179/test',data=aData)

    def __init__(self):
        _serial = self.getserial()
        _accel = Adafruit_ADXL345.ADXL345()


if __name__ == "__main__":
    PiAccererometer=PiAccelerometerIOTClient()

    print('My serial number is {0}'.format(PiAccererometer.getserial()))
    PiAccererometer.post_data()
