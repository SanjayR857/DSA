# Python Program to print all Possible Combinations from the three Digits
#
# Input: [1, 2, 3]
# Output:
# 1 2 3
# 1 3 2
# 2 1 3
# 2 3 1
# 3 1 2
# 3 2 1
def  all_possible_comb(list_2):
    list_1 = ''
    for i in list_2:
        list_1+=str(i)
    if len(list_1)<1:
        return [list_1]
    comb = []
    for i in range(len(list_1)):
        first_num = list_1[i]
        remainig_num = list_1[:i] + list_1[i+1:]
        for perm in all_possible_comb(remainig_num):
            comb.append(first_num+perm)
    return comb

from itertools import permutations
from itertools import permutations

num = permutations([1, 2, 3], 3)
for i in num:
    print(i)


def num_comb(numbers):
    len_num = len(numbers)
    num_comb = []
    for i in range(len_num):
        for j in range(len_num):
            for k in range(len_num):
                if i != j and j != k and i != k:
                    num_comb.append([numbers[i], numbers[j], numbers[k]])
    print(num_comb)


num_comb([1, 2, 3])

res = all_possible_comb([1,2,3])
for i in res:
    print(i)