# Input: 'Geeks123For123Geeks'
# Output: GeeksForGeeks
# Explanation: In This, we have removed the '123' character from a string.
def remove_char_using_repalce(word,letter):
    output = word.replace(letter, '')
    print(output)
    
def remove_char_using_translate(word,letter):
    print(word.translate({ord(i): None for i in '12'}))


word = 'Geeks123For123Ge23eks'
letter='123'
remove_char_using_repalce(word,letter)
remove_char_using_translate(word,letter)


output=''
i=0
letter_num = len(letter)
while i<len(word):
    if word[i:i+letter_num] == letter:
        output+=' '
        i+=letter_num
    else:
        output+=word[i]
        i+=1
print(output)







