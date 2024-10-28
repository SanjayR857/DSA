test_list = [[4, 1, 6], [7, 8], [4, 10, 8]]

# for i in test_list:
#     i.sort(reverse=True)
# print(test_list)

for i in test_list:
    for j in range(len(i)-1):
        for k in range(j+1,len(i)):
            if i[j]<i[k]:
                i[j],i[k]=i[k],i[j]
print(test_list)
