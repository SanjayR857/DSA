# The original list is : ['Gfg', 'is', 'best', 'for', 'Geeks']

input_text = ['Gfg', 'is', 'best', 'for', 'Geeks']

def without_using_replace(input_text):
    for i in range(len(input_text)):
        text = ''
        for j in input_text[i]:
            if j=='G':
                j='e'
            elif j=='e':
                j='G'
            text+=j
        input_text[i]=text
    print(input_text)

def with_using_replace(input_text):
    for i in range(len(input_text)):
        input_text[i] = input_text[i].replace('e','G')
        input_text[i] = input_text[i].replace('G', 'e')
    print(input_text)

without_using_replace(input_text)
with_using_replace(input_text)

del input_text
try:
    print(input_text)
except Exception as e:
    print(e)