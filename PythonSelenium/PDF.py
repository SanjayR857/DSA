# from PyPDF2 import PdfReader
#
#
# # Open the PDF file
# reader = PdfReader("C://Users//SANJAYR//Downloads//pdf-sample.pdf")
# number_of_pages = len(reader.pages)
#
# print(number_of_pages)
#
# text = reader.pages[0].extract_text()
# print(text)
#
# string='''
#
# Compact PDF files are smaller than their source files and download a
# page at a time for fast display on the Web.
#
# '''
#
# if string in text:
#     print('True')
# else:
#     print('False')
import os

import pdfplumber

with pdfplumber.open("C://Users//SANJAYR//Downloads//pdf-sample.pdf") as pdf:
    all_text = ""
    for page in pdf.pages:
        all_text += page.extract_text() + "\n"

    print(all_text)

    # Optionally, write to a text file
    with open("extracted_text.txt", "w", encoding="utf-8") as output_file:
        output_file.write(all_text)

