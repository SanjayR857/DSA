# Input : test_list = [“geekforgeekss”, “is”, “bessst”, “for”, “geeks”], K = ‘s’
# Output : [‘bessst’, ‘geekforgeekss’, ‘geeks’, ‘is’, ‘for’]

test_list =['geekforgeekss','is','bessst','for','geeks']
k='s'
dict_1 ={}
for i in range(len(test_list)):
    flag = False
    for j in range(i+1,len(test_list)):
        if test_list[i].count(k)<test_list[j].count(k):
            test_list[i],test_list[j] =  test_list[j],test_list[i]
            flag = True
    if flag == False:
        break

print(test_list)

input_text = 'gfg, is, (best, for), geeks'

for i in input_text.split():



