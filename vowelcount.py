
"""

@author: stacy
"""

'''Question 6: Count Vowels
Write a program that counts the number of vowels in a sentence.'''

def count_vowels(sentence):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    # Initialize a counter for vowels
    vowel_count = 0
    
    for char in sentence:
        if char.lower() in vowels:
            vowel_count += 1
    return vowel_count

# Test
input_sentence = input("Enter a sentence: ")
vowel_count = count_vowels(input_sentence)
print("Number of vowels:", vowel_count)
