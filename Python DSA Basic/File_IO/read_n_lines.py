from itertools import  islice

def read_n_lines (file_name,nlines):
    with open(file_name) as file:
        for line in islice(file,nlines):
            print(line)

read_n_lines('text.txt',6)
