# 1. Write a Python program to create a decorator that logs the arguments and return value of a function.



def decorator(func):
    def wrap(*args,**kwargs):
        print(func.__name__,f'args {args}  kwargs {kwargs}')

        result = func(*args,**kwargs)

        print(func.__name__,f'result {result}')
        return result
    return  wrap


@decorator
def sum(x,y):
    return x+y

print(sum(3,4))



