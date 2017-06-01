#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a DB Conn '

__author__ = 'Taburiss'

import mysql.connector;
import config

c = config.configs;
host = c['db']['host'];
user = c['db']['user'];
password = c['db']['password'];
database = c['db']['database'];

def connectTest():
    conn = mysql.connector.connect(host=host,user=user, password=password, database=database);
    cursor = conn.cursor();
    cursor.execute('select * from TestSheet');
    values = cursor.fetchall();
    cursor.close();
    conn.close();