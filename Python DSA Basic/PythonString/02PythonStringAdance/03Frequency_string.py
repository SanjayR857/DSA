# Input : test_str = 'Gfg is best'
# Output : {'Gfg': 1, 'is': 1, 'best': 1}
text_str = 'Gfg is best is best Gfg'
dict_1={}

for i in text_str.split():
    if i not in dict_1.keys():
        dict_1[i]=text_str.count(i)
print(dict_1)