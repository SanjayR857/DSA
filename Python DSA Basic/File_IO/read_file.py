with open('text.txt','r') as file:
    texts = file.read()
    print(texts)

def text_open(file):
    file_read = open(file)
    print(file_read.readlines())

text_open('text.txt')