'''Write a function to find all pairs of an integer array whose sum is equal to a given number. Do not consider commutative pairs.

Example

pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7)
Output : ['2+5', '4+3', '3+4', '-2+9']
'''
def sum_of_paries(num_list,sum):
    output=[]
    for i in range(len(num_list)):
        for j in range(i+1,len(num_list)):
            if num_list[i]+num_list[j] == sum:
                output.append(f'{num_list[i]}+{num_list[j]}')
    return output


def sum_of_pairs(num_list, target_sum):
    seen = set()
    output = []

    for num in num_list:
        complement = target_sum - num
        if complement in seen:
            output.append(f'{complement}+{num}')
        seen.add(num)

    return output


def sanjay(list_1,targt):
    seen = set()
    output = []
    for num in list_1:
        comp = targt - num
        if comp in seen:
            return comp,num
        seen.add(num)


print(sum_of_paries([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7))
print(sum_of_pairs([2, 4, 3, 5, 6, -2, 4, 7, 8, 9,1,6], 7))
print(sanjay([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7))