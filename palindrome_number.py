"""
Given an integer x, return true if x is a
palindrome, and false otherwise.
"""
x = int(input("Enter the number to check: "))

# convert to string
x = str(abs(x))

# perform the check via list slicing
if x == x[::-1]:
    print("It is a palindrome!")
else:
    print("Not a palindrome!")
