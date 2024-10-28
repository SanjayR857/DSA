'''
driver.get('url')
driver.back()
driver.forward()
driver.refresh()
driver.refresh()
driver.close()
driver.quit()
'''
from selenium import  webdriver
from selenium.webdriver.common.by import  By
#NoSuchElementException

#driver = webdriver.Chrome(executable_path='C:\\bin\\chromedriver.exe')
driver = webdriver.Chrome()
driver.get('http://www.python.org')
driver.find_element(By.XPATH,'//*[@id="downloads"]/a').click()
driver.back()
driver.forward()
driver.refresh()
driver.close()
print('execution is done')