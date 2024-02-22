# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 12:22:44 2024

@author: stacy
"""

def reverse_integer(n):
    # Convert the integer to a string, reverse it, and convert it back to an integer
    reversed_str = str(n)[::-1]
    
    if n < 0:
        reversed_str = "-" + reversed_str[:-1]  
    return int(reversed_str)

# Test
input_integer = int(input("Enter an integer: "))
reversed_integer = reverse_integer(input_integer)
print("Reversed integer:", reversed_integer)
