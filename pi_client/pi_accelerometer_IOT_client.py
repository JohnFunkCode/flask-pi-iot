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
        return self._defined_server_destinations

    def print_server_destinations(self):
        print("Here is the list of defined server destinations:")
        for server in self._defined_server_destinations:
            print(" {0}".format(server))

    def print_valid_server_destinations(self):
        print("Here is the list of valid server destinations:")
        for server in self._valid_server_destinations:
            print(" {0}".format(server))

    def print_invalid_server_destinations(self):
        print("Here is the list of invalid server destinations:")
        for server in self._invalid_server_destinations:
            print(" {0}".format(server))

    def get_valid_server_destinations(self):
        self._invalid_server_destinations=list()
        valid_server_list = self.get_server_destinations()[:]
        print("Testing connections to server destinations...")
        for server in valid_server_list:
            if(self.is_server_available(server)==False):
                #print("*** adding {0} to the list of servers to be removed".format(server))
                self._invalid_server_destinations.append(server)
        # remove invalid servers - we didn't do it in the previous for loop because it messes up the iterator
        #print("Removing the following servers that returned errors:")
        for server in self._invalid_server_destinations:
            valid_server_list.remove(server)
            #print("** removing {0}".format(server))
        self._valid_server_destinations=valid_server_list[:]
        return valid_server_list

    def is_server_available(self,server):
        #print("Testing connection to the following server: {0}".format(server))
        # send a simple get to the list of servers
        try:
            r = requests.get(server)
            if (r.status_code != 200):
                print("   Server: {0} returned an status code of {1} and will be removed from the list".format(server,r.status_code))
                return False
        except requests.exceptions.RequestException:
            print("   Server: {0} raises an exception and will be removed from the list".format(server))
            return False
        #print("Connection to {0} works".format(server))
        return True

    def post_data(self):
        keep_posting=True
        number_of_readings=0
        while(keep_posting==True):
            # get the data
            number_of_readings+=1
            if(number_of_readings > 99):
                print("Refreshing server list. One Moment..")
                keep_posting=False
            x,y,z=self._accel.read()
            #format it to send to server
            ts=datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

            print('{0}: X={1}, Y={1}, Z={1}'.format(ts,x, y, z))

            #format it to send to server
            ts=datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
            aData={'serial-no':self._serial,'timestamp':ts,'x':x,'y':y,'z':z}

            #send it to the list of servers
            r=None
            for server in self._valid_server_destinations:
                try:
                    print("  Posting to {0}".format(server))
                    r=requests.post(server,data=aData)
                    if (r.status_code != 200):
                        keep_posting = False
                except requests.exceptions.RequestException:
                    print("   Server: {0} raises an exception".format(server))
                    keep_posting = False

    def __init__(self):
        print("Initializing")
        self._serial = self.getserial()
        self._accel = Adafruit_ADXL345.ADXL345()
        self._defined_server_destinations = ['http://10.10.10.14:8080/test',
                                     'http://jpf-flask-pi-iot.cfapps.io/test',
                                     'http://katie-flask-pi-iot.cfapps.io/test',
                                     'http://megan-flask-pi-iot.cfapps.io/test',
                                     'http://david-flask-pi-iot.cfapps.io/test',
                                     'http://shane-flask-pi-iot.cfapps.io/test']
        self.print_server_destinations()
        self._invalid_server_destinations=list()

        self._valid_server_destinations = self.get_valid_server_destinations()
        self.print_server_destinations()
        self.print_invalid_server_destinations()
        self.print_valid_server_destinations()


if __name__ == "__main__":
    '''gets called if you run it from the command line'''
    PiAccererometer=PiAccelerometerIOTClient()

    print('My serial number is {0}'.format(PiAccererometer.getserial()))
    print("beginning to post data...")
    while True:
        PiAccererometer.post_data()
        print("Re-evaluating servers...")
        PiAccererometer.print_server_destinations()
        PiAccererometer.get_valid_server_destinations()
        PiAccererometer.print_valid_server_destinations()
