# Import the ADXL345 module.

import unittest
import import pi_accelerometer_IOT_client as piac

class test_PiAccelerometerIOTClient(unittest.TestCase):

    def setUp(self):
        return

    def test_getserial(self):
        apic = piac.PiAccelerometerIOTClient()
        serial=apic.getserial()
        self.assertTrue(len(serial)>1)

if __name__ == '__main__':
    unittest.main()

