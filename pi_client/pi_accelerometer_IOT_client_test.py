# Import the ADXL345 module.

import unittest
import pi_accelerometer_IOT_client

class test_PiAccelerometerIOTClient(unittest.TestCase):

    def setUp(self):
        return

    def test_getserial(self):
        PiAccererometer = PiAccelerometerIOTClient()
        serial=PiAccererometer.getserial()
        self.assertTrue(len(serial)>1)

if __name__ == '__main__':
    unittest.main()