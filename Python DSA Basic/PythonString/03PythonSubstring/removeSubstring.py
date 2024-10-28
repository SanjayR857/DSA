# Input : test_str = ‘geeksforgeeks is best for geeks’, sub_str = “for”
# Output : geeksforgeeks is best for

input_text = 'geeksforgeeks is best for'
sub = 'for'
list_1 = input_text.split()
num=list_1.index(sub)
print(num)
try:
    list_1.pop(num+1)
except:
    print('Index out of range')
else:
    print('else block')
finally:
    print('executed')
print(' '.join(list_1))
