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



# import time
#
# from selenium import webdriver
#
# # Setup ChromeOptions
#
# driver = webdriver.Chrome()
# # Open a webpage
# driver.get("https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf")
# time.sleep(10)
# # Try triggering menu actions using JS Executor
# driver.execute_script("chrome.send('openSettings');")  # Opens Settings page directly
#
# driver.quit()


import time
import pyautogui
import pyperclip


def pdf_download_using_python():
    time.sleep(2)
    pyautogui.hotkey('ctrl', 's')
    time.sleep(2)

    # if want to store in project value you have to make the pdf file name unquie or it will pop of duplicate update pdf fill with latest pdf name
    # send text arg to this method make it as unique

    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    #current_text = pyperclip.paste()
    #new_text = (f'C:\\Users\\shash\\PycharmProjects\\DSA\\PDF_download\\{current_text}')
    #pyautogui.typewrite(new_text)

    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)

