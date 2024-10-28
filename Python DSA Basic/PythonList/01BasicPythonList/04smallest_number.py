# Input : list2 = [20, 10, 20, 1, 100]
# Output : 1

numbers = [20,10,11,21,3,5,3,7]
# print(min(numbers))
min1 = numbers[0]
min2 = numbers[0]
min3 = numbers[0]

for i in numbers:
    if min1>i:
        min2=min1
        min1=i
    elif min2>i and i!=min1:
        min3 = min2
        min2=i
    elif min3>i and i!=min1 and i!=min2:
        min3=i
print(min1,min2,min3)
def min_number(numbers,num):
    for i in range(len(numbers)-1):
        for j in range(i+1,len(numbers)):
            if numbers[i]>numbers[j]:
                numbers[i],numbers[j]=numbers[j],numbers[i]
    unquie_list = []
    for i in numbers:
        if i not in unquie_list:
            unquie_list.append(i)
    numbers=unquie_list
    if num<=len(numbers):
        return (numbers[:num])
    else:
        return 'Out Of Bound '

print(min_number(numbers,3))

