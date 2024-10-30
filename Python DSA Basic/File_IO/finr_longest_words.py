file = open('text.txt','r')
words = file.read().split()

lenght = len(max(words,key=len))
max_words = [word for word in words if len(word)==lenght]
print(max_words)