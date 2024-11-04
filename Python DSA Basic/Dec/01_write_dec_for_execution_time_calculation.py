# 2. Write a Python program to create a decorator function to measure the execution time of a function.

import time

def measure_time(func):
    def wrap(*args,**kwargs):
        start_time = time.time()
        result = func(*args,**kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print('execution time',func.__name__,f'{execution_time:.20f}')
        return result
    return wrap

@measure_time
def mutiple(x):
    total = 1
    for i in x:
        total*=i
    return total

print(mutiple([1,2,3,4,5,6]))

