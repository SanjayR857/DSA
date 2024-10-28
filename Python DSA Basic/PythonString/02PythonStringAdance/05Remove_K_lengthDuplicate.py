test_str = 'geeksforfreeksf0'
K = 3
print(len(test_str))
memo = set()
res = []
for i in range(len(test_str)-3):
    sub= test_str[i:i+K]
    if sub not in memo:
        memo.add(sub)
        res.append(sub)
print(res)
# res = ''.join(res[ele]+' ' for ele in range(0,len(res),K))
# print(res)

res = ''.join(res[ele] for ele in range(0,len(res),K))
print(res)