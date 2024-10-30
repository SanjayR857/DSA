with open('text.txt','+a') as file:
    file.write('sanjay R \n')
    file.write('vikas   \n')

file = open('text.txt')

print('#############')
print('##############')

for i in file.readlines():
    print(i)
