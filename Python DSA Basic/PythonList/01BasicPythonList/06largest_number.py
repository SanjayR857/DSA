# Input : list1 = [10, 20, 4]
# Output : 20

number = [10,20,30,40,50,60,5,10,34,200,200]
max1=number[0]
max2=number[0]

for i in range(len(number)):
    if max1<number[i]:
        max2=max1
        max1=number[i]
    elif max2<number[i] and number[i]!=max1:
        max2=number[i]
print(max1,max2)
