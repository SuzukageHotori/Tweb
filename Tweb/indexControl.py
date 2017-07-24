#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a Web Controler '

__author__ = 'Taburiss'

from flask import Flask,request,render_template,url_for,jsonify
from model import * 
from DbConn import *
import base64


DEBUG = True
app = Flask(__name__,static_url_path='/static', static_folder='static')
app.debug = True;


@app.route('/', methods=['GET', 'POST'])
def home():
    model = homeModel();
    return  render_template('/home/Index.html',model=model);


@app.route('/postTest', methods=['POST'])
def postTest():
    return jsonify({'a':1,'b':['hello','world']});


@app.route('/tool', methods=['GET', 'POST'])
def toolHome():
    model = toolModel();
    return   render_template('/tool/index.html',model=model);


@app.route('/tool/b64', methods=['GET', 'POST'])
def b64():
    model = toolModel();
    return   render_template('/tool/b64.html',model=model);

@app.route('/tool/b64Encode', methods=['POST'])
def b64Encode():
    s = request.form['plain'];
    r = base64.b64encode(s.encode('utf-8'));
    return  jsonify({'cipher':r.decode()});

@app.route('/tool/b64Decode', methods=['POST'])
def b64Decode():
    s = request.form['cipher'];
    r = base64.b64decode(s.encode('utf-8'));
    return  jsonify({'plain':r.decode()});

if __name__ == '__main__':
    app.run(port=8023);