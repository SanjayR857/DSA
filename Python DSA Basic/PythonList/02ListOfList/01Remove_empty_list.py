
# Python3 code to Demonstrate Remove empty List
# from List using list comprehension

# Initializing list
test_list = [5, 6, [], 3, [], [], 9]

remove_test = list(filter(None,test_list))
print(remove_test)

def remove_list(test_list):
    number =[]
    for i in test_list:
        if i==[]:
            pass
        else:
            number.append(i)
    return number

print(remove_list(test_list))
