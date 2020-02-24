# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 11:19:44 2020

@author: ACER
"""

#program to find the third angle of a triangle when other 2 angles are known
a=int(input("enter the first angle of a triangle:"))
b=int(input("enter the second angle of a triangle:"))
#sum of three angles in a triangle =180
c=(180-a-b)
print("the third angle of triangle=%i" %c)