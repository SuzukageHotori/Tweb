#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a Test Lab '

__author__ = 'Taburiss'


import timeit  

def dengcha1(start,end):
    return (start+end)*((end-(start-1))>>1);   

def dengcha2(start,end):
    i = start;
    count = 0;
    while i<=end:
        count = count +i;
        i = i + 1;
    return count;


if __name__ == '__main__':
    print(dengcha1(1,100));
    print(dengcha2(1,100));
    t1 = timeit.Timer(stmt='dengcha1(1,100)',setup='from testlab import dengcha1');
    print(t1.timeit(number=1));  
    t2 = timeit.Timer(stmt='dengcha2(1,100)',setup='from testlab import dengcha2');
    print(t2.timeit(number=1));  
