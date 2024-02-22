# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 12:11:38 2024

@author: stacy
"""

'''Question 4: Capitalize Words
Write a program that accepts a string as input, capitalizes the first letter of each word in the
string, and then returns the result string.'''

def capitalize_words(sentence):
    # Split the sentence into words
    words = sentence.split()
    capitalized_sentence = ' '.join(word.capitalize() for word in words)
    return capitalized_sentence

# Test
input_string = input("Enter a string: ")
result = capitalize_words(input_string)
print("Result:", result)
