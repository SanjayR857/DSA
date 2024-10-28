import random

test_list = [[4, 5, 5], [2, 7, 4], [8, 6, 3]]
number = [x for sub in test_list for x in sub]
res = random.choice(number)
print(res)

res = random.choice(test_list[random.choice([0,1,2])])
print(res)