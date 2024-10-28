# The original list 1 : [[1, 2], [3, 4], [5, 6]]
# The original list 2 : [[3, 4], [5, 7], [1, 2]]
# The uncommon of two lists is : [[5, 6], [5, 7]]

list_1 =  [[1, 2], [3, 4], [5, 6]]
list_2 =  [[3, 4], [5, 7], [1, 2]]
list_3 = []

for i in range(len(list_1)):
    if list_1[i] not in list_2 and list_1[i] not in list_3:
        list_3.append(list_1[i])
    if list_2[i] not in list_1 and list_2[i] not in list_3:
        list_3.append(list_2[i])
print(list_3)
