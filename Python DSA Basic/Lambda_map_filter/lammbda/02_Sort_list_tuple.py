# 3. Write a Python program to sort a list of tuples using Lambda.
# Original list of tuples:
# [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# Sorting the List of Tuples:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
list_tuple = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
list_tuple.sort(key=lambda x:x[1],reverse=True)
print(list_tuple)