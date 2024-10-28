# 1. Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and prints the result.
# Sample Output:
# 25
# 48

# Double the number of 15 = 30
# Triple the number of 15 = 45
# Quadruple the number of 15 = 60
# Quintuple the number 15 = 75


sum = lambda  x,y:min(x+y,x-y)
muti = lambda  x,y:x*y
double = lambda  x:2*x
triple = lambda x:3*x
Quadruple = lambda  x:x//4
Quitntuple = lambda x:x//8

print(sum(1,2))
print(muti(4,5))
print(double(3))
print(triple(4))
print(Quitntuple(60))
print(Quadruple(100))