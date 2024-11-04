
def count_element(list_numbers):
    count =0
    list_num = []
    for i in range(len(list_numbers)):
        if list_numbers[i] not in list_num:
            count+=1
            list_num.append(list_numbers[i])
    return  count
input_list = [1, 2, 2, 5, 8, 4, 4, 8]
res = count_element(input_list)
print(f'number of unqiue element is {res}')