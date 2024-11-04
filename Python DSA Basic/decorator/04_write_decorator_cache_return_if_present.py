# Write a Python program that implements a decorator to cache the result of a function.

def cache_value(func):
    cache = {}
    def wrap(*args,**kwargs):
        key = (*args,*kwargs.items())
        print(key)

        if key in cache:
            print('result from the cache')
            return cache[key]

        result = func(*args,**kwargs)
        cache[key] = result
        return  result
    return  wrap

@cache_value
def mutiplication(x,y):
    return x*y

print(mutiplication(4,5))
print(mutiplication(3,4))
print(mutiplication(4,5))


