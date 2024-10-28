# The original list is : ['gfg', '   ', ' ', 'is', '            ', 'best']
list_word = ['gfg','  ',' ','is','','best']

for i in list_word:
    if not i.isspace() and i.isalnum():
        print(i)
