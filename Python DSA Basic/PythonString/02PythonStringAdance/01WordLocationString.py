import re

test_str = 'geeksforgeeks is best for geeks'
count = 0
word = 'best'

for i in test_str.split():
    if word==i:
        print(count+1)
    else:
        count+=1

for i in test_str.split():
    if len(re.findall(word,i))>0:
        print(test_str.split().index(i)+1)

print(test_str.split().index(word)+1)