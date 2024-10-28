'''
driver.find_element(By.NAME,'username').click()
driver.find_element(By.NAME,'username').clear()
driver.find_element(By.NAME,'username').send_keys('Admin')
driver.find_element(By.NAME,'username').submit()
'''

from time import sleep
from selenium import  webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
sleep(3)

driver.find_element(By.NAME,'username').send_keys('Admin')

driver.find_element(By.NAME,'username').click()


driver.find_element(By.NAME,'password').send_keys('admin123')

driver.find_element(By.NAME,'password').clear()
sleep(3)
driver.find_element(By.NAME,'password').send_keys('admin123')

driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').submit()

