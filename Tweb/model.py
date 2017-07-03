#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a model '

__author__ = 'Taburiss'

class baseModel(object):
    title = 'Taburiss Studio';

class homeModel(baseModel):
    __slots__=('name');
    def __init__(self):
        self.name = 'Taburiss';

class toolModel(baseModel):
    __slots__=('name');
    def __init__(self):
        self.name = 'Taburiss';

