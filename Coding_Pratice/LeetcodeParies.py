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

print(sum_of_paries([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7))