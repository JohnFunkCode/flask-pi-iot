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
def individual_page():
    if request.method == 'POST':
        print("group got a post")
        print(request.form)
    return render_template('johnpi.html')

@app.route('/meganpi.html',methods=['POST','GET'])
def group_page():
    if request.method == 'POST':
        print("group got a post")
        print(request.form)
    return render_template('meganpi.html')


@app.route('/katiepi.html',methods=['POST','GET'])
def patterns_page():
    if request.method == 'POST':
        print("patterns got a post")
        print(request.form)

    return render_template('katiepi.html')
