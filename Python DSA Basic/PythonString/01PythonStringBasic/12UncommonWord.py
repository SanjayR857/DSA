# Input : A = “Geeks for Geeks”,  B = “Learning from Geeks for Geeks”
# Output : [‘Learning’, ‘from’]

input_a = 'Geeks for Geeks' 
input_b = 'Learning from Geeks for Geeks'
# using list comprehension
list_1 = [word for word in input_a.split() if word not in input_b.split()]+[word for word in input_b.split() if word not in input_a.split()]
print(list_1)

# using set 
set_1 = list(set(input_a.split()).symmetric_difference(input_b.split()))
print(set_1)

