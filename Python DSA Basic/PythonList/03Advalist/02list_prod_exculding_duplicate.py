# The original list is : [1, 3, 5, 6, 3, 5, 6, 1]
# Duplication removal list product : 90

list_number = [1, 3, 5, 6, 3, 5, 6, 1]
list=[]
prod=1
for i in list_number:
    if i not in list:
        list.append(i)
        prod*=i
print(prod)