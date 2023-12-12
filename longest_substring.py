"""
Given a string 'text', find the length of the longest
substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""
text = input("Enter the text: ")
resultant_text = ""


for char in text:
    if char in resultant_text:
        break
    else:
        resultant_text += char

print(f"Explanation: The answer is '{resultant_text}', with the length of '{len(resultant_text)}'")

