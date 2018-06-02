
class PiIOTData:
    '''A class to represent the data we collect from the raspberry Pis'''

    _pi_readings = list()

    def get_all_readings(self):
      return self._pi_readings

    def add_reading(self, d):
        #Check the input to make sure it makes sense
        self._pi_readings.append(d)

    def get_number_of_readings(self):
        return len(self._pi_readings)

    def __init__(self):
        _pi_readings = list()

if __name__ == "__main__":
    aPD=PiIOTData()
    l = aPD.get_all_readings()
    for reading in l:
        serial = reading['serial-no']
        timestamp = reading['timestamp']
        x = reading['x']
        y = reading['y']
        z = reading['y']
        print("Serial Number:{0}\tTimeStamp:{1}\tX{2}\tY{3}\tX{4}".format(serial, timestamp, x, y, z))

