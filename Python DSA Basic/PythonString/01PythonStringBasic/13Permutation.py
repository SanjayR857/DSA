# Input :  str = 'ABC'
# Output : ABC
#          ACB
#          BAC
#          BCA
#          CAB
#          CBA

from itertools import permutations

def allpermutations(str):

    permlist = permutations(str)

    for perm in list(permlist):
        print(''.join(perm))

allpermutations('ABC')

# using resu

def generate_permutations(string):
    if len(string) == 1:
        return [string]

    permutations = []
    for i in range(len(string)):
        fixed_char = string[i]
        remaining_chars = string[:i] + string[i+1:]
        for perm in generate_permutations(remaining_chars):
            permutations.append(fixed_char + perm)

    return permutations

permutations_list = generate_permutations('GEEK')
print(set(permutations_list))