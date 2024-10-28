# Input: khokho
# Output: 
# The entered string is symmetrical
# The entered string is not palindrome

input = 'khohk'

def palindrome(input):
    if not input==input[::-1]:
        print('symmetrical')
    else:
        print('palindrome')
        
def palindrome1(input):
    string=''
    for i in range(0,len(input)):
        string+=input[i]
    if string==input:
        print('palindrome')
    else:
        print('symmetrical')

palindrome(input)
palindrome1(input)