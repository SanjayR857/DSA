list_string = 'geekforgeeks'
list_string = sorted(list_string)
print(''.join(list_string[::-1]))


list_string = [x for x in list_string]
for i in range(len(list_string)-1):
    for j in range(i+1,len(list_string)):
        if ord(list_string[i])<ord(list_string[j]):
            list_string[i],list_string[j] = list_string[j],list_string[i]
print(''.join(list_string))
