num1 = int(input("Enter the integer you want to reverse: "))

# get the absolute value and convert to string
reversed_num = str(abs(num1))

# reverse it
reversed_num = reversed_num[::-1]

# return the negative sign if it was there
if num1 < 0:
    reversed_num = "-"+reversed_num

# convert back to integer
reversed_num = int(reversed_num)

# print result
print(reversed_num)
