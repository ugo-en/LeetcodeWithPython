"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:
"""

# welcome message
print("This is an application that displays a piece code in zigzag format, then reads them out.")

# accept text from user
text = input("Enter a text to display in zigzag format: ")

# the number of rows for the zigzag format
rows = int(input("Enter the number: "))

# represent the counter that handles allocation of values to the dictionary
counter = 1

# stores the result
result = dict()

# sort out the characters in the text to the dictionary
for char in text:
    char_list = result.get(counter, [])
    char_list.append(char)

    result[counter] = char_list

    if counter == rows:
        counter = 1
    else:
        counter += 1

# print it in zigzag format
for item in result.items():
    key = item[0]
    values = item[1]

    print(" "*key, end="")
    for v in values:
        print(f"{' '*4}{v}", end="")

    print()

# print the resultant text based on what rows they were placed
for value in result.values():
    for v in value:
        print(v, end="")

