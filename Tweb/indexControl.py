#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a Web Controler '

__author__ = 'Taburiss'

from flask import Flask,request,render_template,url_for,jsonify
#DEBUG = True
app = Flask(__name__,static_url_path='/static', static_folder='static')


class homeModel(object):
    __slots__=('name','dict');
    def __init__(self):
        self.name = 'Taburiss';
        self.dict = {'name':self.name}



@app.route('/', methods=['GET', 'POST'])
def home():
    model = homeModel();
    #a = url_for("static",filename="img/timg.jpg") ;
    return  render_template('/home/Index.html',model=model);


if __name__ == '__main__':
    app.run(port=8023);