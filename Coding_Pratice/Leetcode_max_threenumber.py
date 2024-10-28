from  random import randint
array = []
for i in range (0,10):
    array.append(randint(0,100))
print(array)

def max3_number(array):
    max1,max2,max3=0,0,0
    for num in (array):
        if num>max1:
            max3=max2
            max2=max1
            max1=num
        elif num>max2:
            max3=max2
            max2=num
        elif num>max3:
            max3=num
            
    return  (max1,max2,max3)

print(max3_number(array))