import random 
import string
text = 'GFG'
possibleCharacters = string.ascii_lowercase + string.digits +string.ascii_uppercase +' ., !?;:'
count =0
for i in text:
    while True:
        rand = random.choice(possibleCharacters)
        if rand==i:
            break
        else:
            count += 1
            print('None')
print(f'it took {count} times to generate {text}')