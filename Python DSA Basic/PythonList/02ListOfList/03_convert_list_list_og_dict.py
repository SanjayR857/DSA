# The original list is : [['a', 'b', 1, 2], ['c', 'd', 3, 4], ['e', 'f', 5, 6]]
# The mapped Dictionary : {('a', 'b'): (1, 2), ('c', 'd'): (3, 4), ('e', 'f'): (5, 6)}
list_original =  [['a', 'b', 1, 2], ['c', 'd', 3, 4], ['e', 'f', 5, 6]]
dict_1 = {}
dict_2 = {}
for sub in list_original:
    dict_1[(tuple(sub[:2]))] = tuple(sub[2:])
print(dict_1)

for sub in list_original:
    key = tuple(sub[:2])
    value = tuple(sub[2:])
    dict_2[key] = value
print(dict_2)
