# check if element in range or not
test_list = [4, 5, 6, 7, 3, 9]
i,j = 3,10
res = True
for k in test_list:
    if k<i or  k>=j:
        res = False
        break
print(res)

res = any(map(lambda x: i <= x < j, test_list))
print(res)

