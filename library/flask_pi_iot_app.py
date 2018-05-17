from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
import requests

app = Flask(__name__)

@app.route('/test', methods=['POST','GET'])
def my_test():
    print("/test")
    print(request)
    print(request.form)
    return("hello")

@app.route('/yaml')
def my_yaml_microservice():
    pass
    #return ymlify({'Hello':'World'})


@app.route('/')
@app.route('/index.html')
def main_page():
    return render_template('index.html')

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
    return render_template('katiepi.html')