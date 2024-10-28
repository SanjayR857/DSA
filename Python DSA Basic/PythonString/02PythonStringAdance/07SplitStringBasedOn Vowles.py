input_Text = 'GFGaBstuforigeekse'
vowels = 'aeiou'
word_list = []
word =''
for i in input_Text:
    if i not in vowels:
        word+=i
    else:
        if not word=='':
            word_list.append(word)
        word=''
if word!='':
    word_list.append(word)

print(word_list)

