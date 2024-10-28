test_list = [12, 67, 98, 34]
sum_list = []

for i in range(len(test_list)):
    sum=0
    if len(str(test_list[i]))>0:
        for j in (str(test_list[i])):
            sum+=int(j)
    sum_list.append(sum)
print(sum_list)