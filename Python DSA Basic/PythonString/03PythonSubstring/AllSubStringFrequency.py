# Input : test_str = “ababa”
# Output : {‘a’: 3, ‘ab’: 2, ‘aba’: 2, ‘abab’: 1, ‘ababa’: 1, ‘b’: 2, ‘ba’: 2, ‘bab’: 1, ‘baba’: 1}

input_text = 'ababa11'
dict_1 = {}
for i in range(0,len(input_text)):
    for j in range(0,len(input_text)+1):
        print(input_text[i:j],end=' ')
        if input_text[i:j]!='':
            dict_1[input_text[i:j]] = input_text.count(input_text[i:j])
print(dict_1)

dict_2= {}
for i in range(0,len(input_text)):
    for j in range(0,len(input_text)+1):
        if input_text[i:j]!='':
            dict_2[input_text[i:j]] = input_text.count(input_text[i:j])
print(dict_2)