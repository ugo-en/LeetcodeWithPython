"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
"""
import math

array1 = [1,2,3,4,5]
array2 = [10,6,2,11,14]

# merge and sort the arrays
merged_array = array1 + array2
merged_array.sort()

# find the median
if len(merged_array) % 2 == 0:
    index1 = math.floor((len(merged_array) - 1) / 2)
    index2 = math.ceil((len(merged_array) - 1) / 2)

    median = (merged_array[index1] + merged_array[index2]) / 2
else:
    index = (len(merged_array) - 1) // 2
    median = merged_array[index]

# print the result
print(f"Merged array: {merged_array} and median is {median}")

