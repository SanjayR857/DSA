'''
Action = ActionChains(driver)
Action.move_to_element(locator).perform()
Action.drag_and_drop(source_element,traget_element).perform()
Action.context_click()
Action.click()
Action.Action.context_click()
Action.move_by_offset(locator,x,y)
Action.reset_actions()
Action.reset_actions()
Action.release()
Action.perform()
'''

from time import sleep
from selenium import  webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://testautomationpractice.blogspot.com/')
Action = ActionChains(driver)
mouse_over = driver.find_element(By.XPATH,'//*[@id="HTML5"]/div[1]/button')
Action.move_to_element(mouse_over).perform()
sleep(3)
Action.click(driver.find_element(By.XPATH,'//*[@id="HTML10"]/div[1]/button')).perform()
sleep(3)
source_element = driver.find_element(By.XPATH,'//*[@id="draggable"]')
traget_element = driver.find_element(By.XPATH,'//*[@id="droppable"]')
Action.drag_and_drop(source_element,traget_element).perform()
sleep(3)
Action.context_click(driver.find_element(By.XPATH,'//*[@id="HTML10"]/div[1]/button')).perform()
sleep(3)
Action.double_click(driver.find_element(By.XPATH,'//*[@id="HTML10"]/div[1]/button')).perform()
sleep(3)
Action.click_and_hold(driver.find_element(By.XPATH,'//*[@id="slider"]/span')).move_by_offset(100,0).release().perform()
sleep(3)
Action.click_and_hold(driver.find_element(By.XPATH,'//*[@id="resizable"]/div[3]')).move_by_offset(5,5).release().perform()
sleep(3)
Action.reset_actions()
Action.scroll_to_element(driver.find_element(By.XPATH,'//*[@id="HTML5"]/div[1]/button'))
sleep(3)
Action.reset_actions()
