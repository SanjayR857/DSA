# Input : str = "hello geeks for geeks 
#           is computer science portal" 
#         k = 4

str1 = "hello geeks for geeks is computer science portal"
k = 4

list1 = [word  for word in str1.split() if len(word) > k]
print(' '.join(list1))
str2=''

for word in str1.split():
    if len(word) > k:
        str2+=word
print(str2)