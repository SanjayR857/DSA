#Rotate Matrix 90 degree / Image - LeetCode 48
import numpy as np 

array2d =[[1,2,3],[4,5,6],[7,8,9]]

def rotate_matrix(array2d):
    lengh = len(array2d)
    for i in range(lengh):
        for j in range(i,lengh):
            array2d[i][j],array2d[j][i]=array2d[j][i],array2d[i][j]
    for i in array2d:
        i.reverse()
    return  array2d
print(array2d)
print(rotate_matrix(array2d))
