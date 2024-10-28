# Input : test_str = ‘geeksforgeeks 33 best’ 
# Output : 19 
# Explanation : Total characters are 19. 

input = 'geeksforgeeks 33 best'
list = input.split()
print(len(''.join(list)))

def count_without_space(input):
    count =0
    for i in input:
        if i!=' ':
            count+=1
    print(count)
count_without_space(input)