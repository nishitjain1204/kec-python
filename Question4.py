# The alphabetical value is represented from 1-26 for characters A-Z respectively. Using this
# principle generate a crypto decoder that can generate the message for transmitted sequence of
# alphabetical values.
# Example:
# Input : 1,2,3,4,26 Output : ABCDZ

import string

# print(string.ascii_letters[0])

num_list = [int(i) for i in input().split(',')]

result_str = ""

for number in num_list:
    result_str += string.ascii_letters[number-1]
    
print(result_str.upper())
