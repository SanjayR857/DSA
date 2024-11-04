numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Elements to remove
to_remove = [3, 5, 7]


#print([num for num in numbers if num not in to_remove])


print(numbers)

def remove_element(numbers,to_remove):
    for i in to_remove:
        numbers.remove(i)
    return numbers

def filter_remvoe_element(numbers,to_remove):
    number = list(map(lambda x: x  not in to_remove,numbers))
    return  number

# print(remove_element(numbers,to_remove))
print(filter_remvoe_element(numbers,to_remove))


