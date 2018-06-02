from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
import requests
#from pi_client import pi_accelerometer_IOT_client as pac
from library.pi_iot_data import pi_iot_data as IOTdata


app = Flask(__name__)
_pi_readings = IOTdata.PiIOTData()


@app.route('/test', methods=['POST','GET'])
def my_test():
    if request.method == 'GET':
        return("hello")
    else:
        #print("/test")
        #print(request)
        #print(request.form)
        d=request.form
        #print(d['serial-no'])
        _pi_readings.add_reading(d)
        return("thanks")

@app.route('/yaml')
def my_yaml_microservice():
    pass
    #return ymlify({'Hello':'World'})


@app.route('/')
@app.route('/index.html')
def main_page():
    return render_template('index.html')

@app.route('/alldata.html')
def alldata_page():
    d=_pi_readings.get_all_readings()
    print("/alldata:d".format(d))
    return render_template('alldata.html',data=d)
    #return render_template('alldata.html',data=_pi_readings)

@app.route('/johnpi.html',methods=['POST','GET'])
def john_page():
    if request.method == 'POST':
        print("JohnPi got a post")
        print(request.form)
    return render_template('johnpi.html')

@app.route('/meganpi.html',methods=['POST','GET'])
def megan_page():
    if request.method == 'POST':
        print("MeganPi got a post")
        print(request.form)
    return render_template('meganpi.html')


@app.route('/katiepi.html',methods=['POST','GET'])
def katie_page():
    if request.method == 'POST':
        print("KatiePi got a post")
        print(request.form)
    return render_template('katiepi.html')

@app.route('/davidpi.html',methods=['POST','GET'])
def david_page():
    if request.method == 'POST':
        print("DavidPi got a post")
        print(request.form)
    return render_template('davidpi.html')