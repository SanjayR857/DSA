from time import sleep
from selenium import  webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
''''
1. CSS (Cascading Style Sheets) Selector is a locator that uses character sequence patterns to identify the elements based on the HTML structur

'''
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://testautomationpractice.blogspot.com/')

css_selector = 'tagname[attrubite="value"]'   # input[ID='sanjay']   #(input#sanjay)
id_with_diff_atrri = By.CSS_SELECTOR('input#id-[type="text"]')  # (input.classname-[type="text"])


#: How to write the best locator expressions?
'''
Avoid the absolute locator expressions
Use relative locator expressions
Always try to keep the locator expressions as short as possible
'''
