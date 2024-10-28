# Input : test_list = [“geeksforgeeks is best for geeks”], chr_list = [‘e’, ‘b’, ‘g’, ‘f’] 
# Output : {‘g’: 3, ‘e’: 7, ‘b’: 1, ‘f’ : 2} 

def char_freq_string(input_text,char_list):
    dict_1 = {}
    for i in char_list:
        dict_1[i] = input_text.count(i)
    return dict_1

print(char_freq_string('geeksforgeeks is best for geeks',['e', 'b', 'g', 'f']))
dict = {}
char_list = ['e', 'b', 'g', 'f']
for j in char_list:
    count=0
    for i in 'geeksforgeeks is best for geeks':
        if j==i:
            count+=1
    dict[j]=count
print(dict)
