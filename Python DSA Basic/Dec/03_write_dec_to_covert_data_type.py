# Write a Python program to create a decorator to convert the return value of a function to a specified data type.

def convert_data_type(data_type):
    def decorator(func):
        def wrapper(*args,**kwargs):
            result = func(*args,**kwargs)
            value = None
            try:
                value = data_type(result)
            except Exception as e:
                print(e)
            return value
        return wrapper
    return decorator

@convert_data_type(int)
def concate(x,y):
    return  x+y

@convert_data_type(str)
def concate_string(x,y):
    return x+y

result = concate(2,3)
print(result,'data type',type(result))
result_strin = concate_string('pyton','java')
print(result_strin,'data type',type(result_strin))