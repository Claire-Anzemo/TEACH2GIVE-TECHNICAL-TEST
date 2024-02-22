# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 11:14:13 2024

@author: stacy
"""


'''Question 2: Fibonacci Sequence
Write a program to generate the Fibonacci sequence up to 100.'''

# Initialize the first two numbers of the sequence
a = 0
b = 1

print(a)

# Loop to generate the Fibonacci sequence up to 100
while b < 100:
    print(b)
    a, b = b, a + b

