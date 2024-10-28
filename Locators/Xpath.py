from time import sleep
from selenium import  webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
''''
1. XPath expressions can become difficult to write or understand when it is used to locate elements with dynamic attribute values.
2. XPath tends to break if there are changes in the page structure. Though using relative XPath essentially solves this problem, there are still chances that changes in the page structure may cause the XPath to fail.
3. XPath does not support the elements having multi-valued attributes.
'''
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://testautomationpractice.blogspot.com/')

#//tagname[@attribute='value']
xpath_sytax = '//tagname[@attribute="value"]'
Absulate_xpath = '/html/body/div[2]/div/input'
relative_xapth = '//*[@id="name"]'
contains_xpath = '//input[contians(@tagname,"value")'
text_xpath = '//input[text()="value"]'
start_with_xpath = '//input[starts-with(@tagname,"value")]'
ends_with_xpath = '//input[ends-with(@tagname,"value")]'

# logic
OR = '//input[starts-with(@tagname,"value")] or [ends-with(@tagname,"value")]'
AND = '//input[starts-with(@tagname,"value")] and  [ends-with(@tagname,"value")]'

# Axes Xapth

# Following
# It selects all elements in the DOM after the closing tag of the current node.
Following_xpath = ('//input[@tagname="value"]//following::tagname')
following_sibling_Xapth  = ('//input[@tagname="value"]//following-sibling::tagname')

# Preceding
# It selects all elements in the DOM, which come before the opening tag of the current node.
Preceding_xpath = ('//input[@tagname="value"]//Preceding::tagname')
Preceding_sibling_Xapth  = ('//input[@tagname="value"]//Preceding-sibling::tagname')

# Ancestor
# It selects all ancestor elements (parent, grandparent, etc.) of the current node.
Ancestor_xpath = ('//input[@tagname="value"]//ancestor::tagname')

Parent_xpath  = ('//input[@tagname="value"]//parent::tagname')
child_xpath = ('//input[@tagname="value"]//child::tagname')


