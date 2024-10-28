# Input : s = "GeeksforGeeks"
#         d = 2
# Output : Left Rotation  : "eksforGeeksGe"
#          Right Rotation : "ksGeeksforGee"

text_str= 'GeeksforGeeks'
d=2
print(f'Left Roataion: ',text_str[d:-1]+text_str[:d])
print(f'Right Roataion: ',text_str[-d:]+text_str[:-d])