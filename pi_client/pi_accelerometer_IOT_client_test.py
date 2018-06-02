# Import the ADXL345 module.

import unittest
import pi_accelerometer_IOT_client as piac

class test_PiAccelerometerIOTClient(unittest.TestCase):

    def setUp(self):
        return

    def test_getserial(self):
        '''simple test to make sure the serial number isn't empty'''
        print("**test_getserial")
        apic = piac.PiAccelerometerIOTClient()
        serial=apic.getserial()
        self.assertTrue(len(serial)>1)

    def test_get_server_destinations(self):
        '''simple test to make sure the list of server destinations isn't empty'''
        print("**test_get_server_destinations")
        apic = piac.PiAccelerometerIOTClient()
        serial=apic.get_server_destinations()
        self.assertTrue(len(serial)>1)

    def test_print_server_destinations(self):
        print("**test_print_server_destinations")
        apic = piac.PiAccelerometerIOTClient()
        apic.print_server_destinations()

    def test_print_valid_server_destinations(self):
        print("**test_print_valid_server_destinations")
        apic = piac.PiAccelerometerIOTClient()
        apic.print_valid_server_destinations()

    def test_get_valid_server_destinations(self):
        print("**test_get_valid_server_destinations")
        apic = piac.PiAccelerometerIOTClient()
        vsd=apic.get_valid_server_destinations()
        self.assertTrue(len(vsd)>0)

    def test_is_server_available(self):
        print("**test_is_server_available")
        apic = piac.PiAccelerometerIOTClient()
        #self.assertFalse(apic.is_server_available("http://10.2.2.2:2"))
        self.assertTrue(apic.is_server_available("http://jpf-flask-pi-iot.cfapps.io/test"))

    def test_print_invalid_server_destinations(self):
        print("**test_print_invalid_server_destinations")
        apic = piac.PiAccelerometerIOTClient()
        apic.print_invalid_server_destinations()

    def test_read_accelerometer(self):
        print("**test_read_accelerometer")
        '''simple test to make sure it doesn't throw an exception'''
        apic = piac.PiAccelerometerIOTClient()
        x, y, z = apic._accel.read()

        self.assertTrue(x!=0)
        self.assertTrue(y!=0)
        self.assertTrue(z!=0)

if __name__ == '__main__':
    unittest.main()

