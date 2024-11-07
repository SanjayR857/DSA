def prime_numbers(list_limit):

    def is_prime(n):
        if n<1:
            return False
        for i in range(2,n):
            if n%2==0:
                return  False
        return True

    list_num = []
    i=2
    while list_limit ==len(list_num):
        i.is

