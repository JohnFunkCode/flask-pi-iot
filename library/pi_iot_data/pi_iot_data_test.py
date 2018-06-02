import unittest
import pi_iot_data as pd
import time
import datetime
import random

class test_pi_iot_data(unittest.TestCase):

    def setUp(self):
        return

    def test_add_reading(self):
        '''simple test to make sure the serial number isn't empty'''
        aPD = pd.PiIOTData()

        #create a dummy reading and add it
        ts = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        x=random.random()
        y=random.random()
        z=random.random()
        d = {'serial-no': '12345', 'timestamp': ts, 'x': x, 'y': y, 'z': z}
        aPD.add_reading(d)
        self.assertTrue(aPD.get_number_of_readings()==1)

        #create another dummy reading and add it
        ts = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        x=random.random()
        y=random.random()
        z=random.random()
        d = {'serial-no': '23456', 'timestamp': ts, 'x': x, 'y': y, 'z': z}
        aPD.add_reading(d)
        self.assertTrue(aPD.get_number_of_readings()==2)


    def test_get_all_readings(self):
        '''simple test to make sure the serial number isn't empty'''
        aPD = pd.PiIOTData()
        l=aPD.get_all_readings()
        for reading in l:
            serial=reading['serial-no']
            timestamp=reading['timestamp']
            x=reading['x']
            y=reading['y']
            z=reading['y']
            print("Serial Number:{0}\tTimeStamp:{1}\tX:{2}\tY:{3}\tZ:{4}".format(serial,timestamp,x,y,z))

if __name__ == '__main__':
    unittest.main()

