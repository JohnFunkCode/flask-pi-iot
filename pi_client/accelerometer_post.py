# Import the ADXL345 module.
import Adafruit_ADXL345
import requests
import time
import datetime

accel = Adafruit_ADXL345.ADXL345()

while True:
    x,y,z=accel.read()
    print('X={0}, Y={1}, Z={2}'.format(x, y, z))
    ts=datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    aData={'timestamp':ts,'x':x,'y':y,'z':z}
    r=requests.post('http://10.10.10.14:8080/test',data=aData)