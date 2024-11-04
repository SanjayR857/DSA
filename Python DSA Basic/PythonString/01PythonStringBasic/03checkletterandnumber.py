v  # Input: welcome2ourcountry34
# Output: True

# Input: stringwithoutnum
# Output: False
import  re
letter=False
number=False
input_string = ' welcomeurcountry1'

for i in input_string:
    if letter==True and number==True:
        break
    else:
        if letter==False:
            if i.isalpha():
                letter = True
        if  number==False:
            if i.isdigit():
                letter = True
if letter==True and number==True:
    print('True')
else:
    print('False')

import  re

letters = re.compile('[a-zA-Z]')
number = re.compile(('[0-9]'))

if re.search(letters,input_string) and re.search(number,input_string):
    print(True)
else:
    print(False)