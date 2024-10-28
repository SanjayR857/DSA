# Input : geeksforgeeks
# Output : Not Accepted
# All vowels except 'a','i','u' are not present

import operator as op
import re
input_text = 'geeksforgeeksia'
vowles='aioue'


def using_set(input_text,vowles):
    return ('accepted' if len(set(vowles).intersection(input_text))==5  else 'not accepted')

def using_string(input_text,vowles):
    count1 = 0
    for i in set(input_text):
        if i in vowles:
            count1=count1+1
    return ('accepted' if count1==5  else 'not accepted')

def using_regex(input_text):
    c= re.compile('[^aieouAEIOU]')
    #rint(c.search(input_text))
    if len(c.findall(input_text)):
        return 'accepted'
    else:
        return 'not accepted'
    
    
print(using_set(input_text,vowles))
print(using_string(input_text,vowles))
print(using_regex(input_text))


