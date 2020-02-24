# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 11:20:59 2020

@author: ACER
"""

#program to enter  marks of 5 subjects and find total average and percentage of the marks
sub1=int(input("Enter marks of the first subject: "))
sub2=int(input("Enter marks of the second subject: "))
sub3=int(input("Enter marks of the third subject: "))
sub4=int(input("Enter marks of the fourth subject: "))
sub5=int(input("Enter marks of the fifth subject: "))
total=(sub1+sub2+sub3+sub4+sub5)
avg=(total/5)
percent=((total/500)*100)
print("total marks= %2f" %total)
print("averagemarks=%2f" %avg)
print("percentage =%2f" %percent)