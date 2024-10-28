import random
k=7
number=''

for i in range(0,k):
    binary = random.randint(0,1)
    number+=str(binary)
print(number)