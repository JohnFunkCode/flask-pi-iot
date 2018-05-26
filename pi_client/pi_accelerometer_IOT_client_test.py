# Import the ADXL345 module.

import unittest
import pi_accelerometer_IOT_client as piac

class test_PiAccelerometerIOTClient(unittest.TestCase):

    def setUp(self):
        return

    def test_getserial(self):
        apic = piac.PiAccelerometerIOTClient()
        serial=apic.getserial()
        self.assertTrue(len(serial)>1)

    def test_read_accelerometer(self):
        x, y, z = self._accel.read()
        self.assertTrue(x!=0)
        self.assertTrue(y!=0)
        self.assertTrue(z!=0)

if __name__ == '__main__':
    unittest.main()

