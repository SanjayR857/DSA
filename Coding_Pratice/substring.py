string = 'substringlenghtfromthestring'
sub_string = ''
seen = set()
res = ''
for i in string:
    if i not in seen:
        sub_string+=i
        seen.add(i)
    else:
        if len(res)<len(sub_string):
            res = sub_string
            sub_string = i
            seen = set()

print(sub_string)



