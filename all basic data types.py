# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 11:22:33 2020

@author: ACER
"""

#string- text type data type
x="Hello World"
print(x)
#integer - number type data type
x=6
print(x)
#float
x=9.5
print(x)
#complex
x=2j
print(x)

#list sequence type data types
x=[5,8,3]
print(x)
#tuple
x=("red'","blue","white")
print(x)
#range
x = range(6)
print(x)
y =range(2,24,5)
print(y)

#mapping type
x={"name":"john","age":24}
print(x)
 
#set type
x={"red","green","white"}
print(x)
print(type(x))
#frozen set
x=frozenset({"red","green","white"})
print(x)
print(type(x))
#boolean
x = True
print(x)
#byte
x = b"Hello"
print(x)
print(type(x))
#bytearray type
x = bytearray(5)
print(x)
#memory view type
x = memoryview(bytes(5))
print(x)