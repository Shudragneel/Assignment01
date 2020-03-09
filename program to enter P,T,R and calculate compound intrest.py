# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 11:21:50 2020

@author: ACER
"""

#program to enter P,T,R and calculate compound intrest
P=float(input("enter the principle amount:"))
T=float(input("enter the number of years:"))
R=float(input("enter the rate of interest:"))
N=float(input("no of times interest is compounded per year:"))
CI=P*(pow(1+R/100),T)
print("compound interest=%2f" %CI)
