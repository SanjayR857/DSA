list_origin = ['allx','lovex', 'gfg', 'xit', 'is', 'bestx']
suff = 'x'
list1=[]
for i in list_origin:
    if i[-1]!='x':
       list1.append(i)
print(list1)

input_text = 'geeksforgeeeks'
duplicate=set()

for i in input_text:
    if i not in duplicate:
        if input_text.count(i)>1:
            duplicate.add(i)
print(list(duplicate))
