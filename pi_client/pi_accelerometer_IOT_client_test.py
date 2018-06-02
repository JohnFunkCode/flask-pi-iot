# Import the ADXL345 module.

import unittest
import pi_accelerometer_IOT_client as piac

class test_PiAccelerometerIOTClient(unittest.TestCase):

    def setUp(self):
        return

    def test_getserial(self):
        '''simple test to make sure the serial number isn't empty'''
        apic = piac.PiAccelerometerIOTClient()
        serial=apic.getserial()
        self.assertTrue(len(serial)>1)

    def test_get_server_destinations(self):
        '''simple test to make sure the list of server destinations isn't empty'''
        apic = piac.PiAccelerometerIOTClient()
        serial=apic.get_server_destinations()
        self.assertTrue(len(serial)>1)

    def test_print_server_destinations(self):
        apic = piac.PiAccelerometerIOTClient()
        apic.print_server_destinations()

    def test_print_valid_server_destinations(self):
        apic = piac.PiAccelerometerIOTClient()
        apic.print_valid_server_destinations()

    def test_get_valid_server_destinations(self):
        apic = piac.PiAccelerometerIOTClient()
        vsd=apic.get_valid_server_destinations()
        self.assertTrue(len(vsd)>0)

    def test_is_server_available(self):
        apic = piac.PiAccelerometerIOTClient()
        self.assertFalse(apic.is_server_available("http://99.99.99.99:99"))
        self.assertTrue(apic.is_server_available("http://jpf-flask-pi-iot/test"))

    def test_print_invalid_server_destinations(self):
        apic = piac.PiAccelerometerIOTClient()
        apic.print_invalid_server_destinations()

    def test_read_accelerometer(self):
        '''simple test to make sure it doesn't throw an exception'''
        apic = piac.PiAccelerometerIOTClient()
        x, y, z = apic._accel.read()

        self.assertTrue(x!=0)
        self.assertTrue(y!=0)
        self.assertTrue(z!=0)

if __name__ == '__main__':
    unittest.main()

