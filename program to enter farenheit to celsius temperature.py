# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 11:17:46 2020

@author: ACER
"""

#program to enter farenheit to celsius temperature
#temp in farenheit
tf=float(input("enter the farenheit temperature:"))
#temp in celcius
tc=((tf-32)*(5/9))
print("temperature in celsius=%2f" %tc)