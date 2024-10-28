str1 = "Jan, Feb, March"
str2 = "January | February | March"
str1 = str1.split(',')
str2 = str2.replace(' ','').split('|')
dict_1 = {}

for i in range(len(str1)):
    dict_1[str1[i]]=str2[i]

print(dict_1)

# using Zip folder

print(dict(zip(str1,str2)))