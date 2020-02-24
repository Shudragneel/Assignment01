# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 11:21:22 2020

@author: ACER
"""

#program to enter P,T,R and calculate simple intrest
P=float(input("enter the principle amount:"))
T=float(input("enter the number of years:"))
R=float(input("enter the rate of interest:"))
SI=(P*T*R/100)
print("simple interest=%2f" %SI)