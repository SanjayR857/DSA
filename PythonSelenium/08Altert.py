'''
alert = driver.switch_to.alert
alert.accept()
alert.dismiss()
alert.send_keys()
'''

from time import sleep
from selenium import  webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://testautomationpractice.blogspot.com/')
WebDriverWait(driver,30).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="alertBtn"]')))
driver.find_element(By.XPATH,'//*[@id="alertBtn"]').click()

alert = driver.switch_to.alert
alert.accept()
sleep(4)
driver.find_element(By.ID,'confirmBtn').click()
alert.dismiss()
sleep(4)
driver.find_element(By.ID,'promptBtn').click()
sleep(2)
alert.send_keys('sanjay')
alert.accept()
sleep(4)