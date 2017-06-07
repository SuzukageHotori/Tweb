#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a Web Controler '

__author__ = 'Taburiss'

def test():
    import base64 
    s = '300MBM-086';
    a = base64.b64encode(bytes(bytes(s, 'utf-8')));
    k = base64.b64decode('MzAwTUJNLTA4Ng==');
    print (k)
