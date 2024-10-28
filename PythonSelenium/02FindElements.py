'''
driver.find_element(By.ID,'value')
driver.find_elements(By.ID,'value')
driver.find_elements(By.ID,'value').text
'''


from time import sleep
from selenium import  webdriver
from selenium.webdriver.common.by import By
try:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://www.python.org')
    driver.find_element(By.XPATH,'//*[@id="documentation"]/a')
    sleep(3)
    driver.find_element(By.ID,'id-search-field').send_keys('Sanjay')
    sleep(2)
    text=driver.find_element(By.NAME,'q').text
    print(text)
    driver.find_element(By.CLASS_NAME,'search-field').clear()
    value = driver.find_element(By.CLASS_NAME,'search-field').text
    AssertionError(value=='','Error')
    sleep(3)
    driver.find_element(By.LINK_TEXT,'Donate')
    sleep(3)
    driver.back()
    sleep(3)
    driver.close()


except Exception as e:
    print(e)
else:
    print('execution is done')
finally:
    print('done finally')
