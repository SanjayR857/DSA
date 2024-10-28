'''
driver.find_element(By.ID,'sunday').is_selected()
driver.find_element(By.ID,'sunday').is_enabled()
driver.find_element(By.ID,'sunday').is_displayed()
driver.find_element(By.ID,'sunday').get_attribute('attribute name')
'''

from time import  sleep
from selenium import  webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://testautomationpractice.blogspot.com/')
Check_box_sunday = driver.find_element(By.ID,'sunday')

if Check_box_sunday.is_selected():
    print('checkbox selected')
else:
    Check_box_sunday.click()
    print('selected')
print('checking its working are not',driver.find_element(By.ID,'droppable').is_enabled())
print('is displayed',driver.find_element(By.XPATH,'//*[@id="Blog1"]/div[1]/div/div/div/div/h3/a').is_displayed())
attr =  driver.find_element(By.ID,'droppable').get_attribute('ID')
print(attr)