from typing import  List
def plusOne(digits) -> List[int]:
        for i in range(len(digits)-1,-1,-1):
            if digits[i]+1 != 10:
                digits[i]+=1
                return digits
            digits[i] = 0
            if i==0:
                return [1]+digits
        # string = ''
        # for x in digits:
        #     string+=str(x)
        # digit = int(string)+1
        # int_digit = [int(x) for x in str(digit)]
        # return int_digit

print(plusOne(digits=[9,8,9,9]))