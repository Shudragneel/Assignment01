# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 11:18:00 2020

@author: ACER
"""

#program to convert days into years and weeks
#no of days
d=float(input("enter the number of days:"))
#in years
y=(d/365)
w=(d/7)
print("number of years for the given days=%2f" %y)
print("number of weeks for the given days=%2f" %w)