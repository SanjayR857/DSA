# 7. Write a Python program to find if a given string starts with a given character using Lambda.
# Sample Output:
# True
# False

string = 'automation'
a = lambda  x: True if  x.startswith('u') else False
print(a(string))

