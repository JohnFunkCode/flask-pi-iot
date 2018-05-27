#!/usr/bin/env bash
echo pi_accelerometer_IOT_client_test
curl -OL https://raw.githubusercontent.com/JohnFunkCode/flask-pi-iot/development/pi_client/pi_accelerometer_IOT_client_test.py > pi_accelerometer_IOT_client_test.py
echo pi_accelerometer_IOT_client
curl -OL https://raw.githubusercontent.com/JohnFunkCode/flask-pi-iot/development/pi_client/pi_accelerometer_IOT_client.py > pi_accelerometer_IOT_client.py
python pi_accelerometer_IOT_client_test.py -v