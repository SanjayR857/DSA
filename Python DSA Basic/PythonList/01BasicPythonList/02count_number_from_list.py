# Input: lst = [15, 6, 7, 10, 12, 20, 10, 28, 10], x = 10
# Output: 3
Input_list = [15, 6, 7, 10, 12, 20, 10, 28, 10]
x = 10
count = 0
for i in Input_list:
    if i==x:
        count+=1
print(f'x {x} number of count {count}')