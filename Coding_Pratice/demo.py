def findSecondLargest(sequenceOfNumbers):
    # Write your code here.
    max1,max2=0,0
    for i in sequenceOfNumbers:
        if i>max1:
            max2=max1
            max1=i
        elif i>max2 and i<max1:
            max2=i
    if max2==0:
        return-1    
    return max2
list=[6,6,6,6,7]
print(findSecondLargest(list))