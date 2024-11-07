a = [1, 2, 3, 4, 5]
b=[]
c=[]
d=[]
e=[]


seen = set()
seen.add(2)
seen.add(3)
seen.add(2)
print(seen)

for i in a:
    b=list(reversed(a))
print(b)
c = a[::-1]
print(c)

for i in range(len(a)-1,-1,-1):
    d.append(a[i])
print(d)

e = a
e.sort(reverse=True)
print(e)