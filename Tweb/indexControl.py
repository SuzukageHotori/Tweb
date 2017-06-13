#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a Web Controler '

__author__ = 'Taburiss'

from flask import Flask,request,render_template,url_for,jsonify
from model import * 
from DbConn import *


#DEBUG = True
app = Flask(__name__,static_url_path='/static', static_folder='static')
app.debug = True;


@app.route('/', methods=['GET', 'POST'])
def home():
    model = homeModel();
    #a = url_for("static",filename="img/timg.jpg") ;
    return  render_template('/home/Index.html',model=model);


@app.route('/postTest', methods=['POST'])
def postTest():
    return jsonify({'a':1,'b':['hello','world']});


@app.route('/tool', methods=['GET', 'POST'])
def toolHome():
    return   render_template('/tool/index.html');




if __name__ == '__main__':
    app.run(port=8023);