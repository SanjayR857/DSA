# Input : geeksforgeeks 
# Output : geksfor

text =  'geeksforgeeks'
str1 =''

print(set(text))
for i in text:
    if i not in str1:
        str1+=i
print(str1)
    
    