# Input : test_list = [“Gfg”, 3, “is”, 8], key_list = [“name”, “id”]
# Output : [{‘name’: ‘Gfg’, ‘id’: 3}, {‘name’: ‘is’, ‘id’: 8}]

input_list  = ['Gfg',3,"is",8]
key_list = ['name','id']

list_dict = []
for i in range(0,len(input_list),2):
    dict_1 = {}
    dict_1[key_list[0]]=input_list[i]
    dict_1[key_list[1]]=input_list[i+1]

    list_dict.append(dict_1)
print(list_dict)
