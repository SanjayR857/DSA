num = [1,1,2,2,3,3,4,5,6,7,7,8,9,5]
duplicate = []
non_duplicate = []

for i in num:
    count = 0
    for j in num:
        if i==j:
            count+=1
    if count>1:
        if i not in duplicate:
            duplicate.append(i)
    else:
        non_duplicate.append(i)
print(duplicate)
print(non_duplicate)