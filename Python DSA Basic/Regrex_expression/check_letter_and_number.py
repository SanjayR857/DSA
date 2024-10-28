import  re

# Input: stringwithoutnum
# Output: False

def check_letter_regrex(letter):
    char = bool(re.search('[^a-zA-Z]',letter))
    number = bool(re.search('[^0-9]',letter))

    if char and number:
        print(True)
    else:
        print(False)
letter = 'stringwithout1num'
check_letter_regrex(letter)
