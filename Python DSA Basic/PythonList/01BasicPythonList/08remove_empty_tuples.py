# Driver Code
tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'),
          ('krishna', 'akbar', '45'), ('',''),()]

# for i in tuples:
#     if len(i)==0:
#         index = tuples.index(i)
#         tuples.pop(index)
# print(tuples)

number = list(filter(None,tuples))
print(number)
