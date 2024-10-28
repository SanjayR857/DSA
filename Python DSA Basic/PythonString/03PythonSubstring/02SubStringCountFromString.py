# # Input : test_str = “geksefokesgergeeks”, arg_str = “geeks”
# # Output : 3
#
input_text = 'geksefokesgergeeks'
arg_str = 'geeks'
dict_1 = {}

for i in arg_str:
    dict_1[i]= input_text.count(i)
print(min(dict_1.values()))

import sys
# List comprehension
nums_squared_list = [i * 2 for i in range(1000)]
print(sys.getsizeof("Memory in Bytes:",nums_squared_list))
# Generator Expression
nums_squared_gc = (i ** 2 for i in range(1000))
print(sys.getsizeof("Memory in Bytes:",nums_squared_gc))