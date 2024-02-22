
"""
@author: stacy
"""


''' Question 3: Power of Two
Write a program that takes an integer as input and returns 
true if the input is a power of two.'''

def is_power_of_two(n):
    # Check if the number is positive and non-zero
    if n <= 0:
        return False
    return n & (n - 1) == 0

# Taking user input
num = int(input("Enter an integer: "))

# Check if the input is a power of two
if is_power_of_two(num):
    print(num, "is True:power of 2")
else:
    print(num, "is False:not power of 2")



