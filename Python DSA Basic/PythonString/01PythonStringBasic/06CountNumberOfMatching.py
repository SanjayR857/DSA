# Input : str1 = 'abcdef'
#         str2 = 'defghia'
# Output : 4 

str1 = 'aabcddekll12@'
str2 = 'bb2211@55k93'
str3=''
count = 0

# for i in set(str1):
#     if i in str2:
#         count+=1
# print(count)

for i in str1:
    if i not in str3 and i in str2:
        str3+=i
        count+=1

for i in str2:
    if i not in str3 and i in str1:
        str3+=i
        count+=1

print(count)