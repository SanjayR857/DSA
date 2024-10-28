string = '10001111100101110010111010111110011'
str1=''
for i in range(0,len(string),7):
    bin = (string[i:i+7])
    convert = int(bin,2)
    print(chr(convert))
