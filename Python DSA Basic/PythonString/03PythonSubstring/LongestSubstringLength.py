# test_str = ‘abcaaaacbbaa’, K = b
test_str = 'abcaaaacbbaabbbaaa'
k='b'
count=0
res=0
for i in range(0,len(test_str)):
    if test_str[i]==k:
        count+=1
    else:
        count=0
    #res =max(res,count)
    if res<count:
        res = count
print(res)

test_str = "gfggfggfggfggfggfggfggfg"
list_word=[]
str1=''
for i in range(0,len(test_str)-1):
        str1+=test_str[i]
        if test_str[i] == test_str[i+1]:
            list_word.append(str1)
        else:
            str1 = ''
print(list_word)

count = 0
res =0
for i  in 'abcaaaacbbaabbbaaa':
    if i=='b':
        count+=1
    else:
        if count!=0:
            res = min(res,count)
        count=0
print(res)

