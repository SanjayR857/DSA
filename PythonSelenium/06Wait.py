'''
WebDriverWait(driver,timout).until(EC.element_to_be_selected((locator')))
driver.implicitly_wait(10)

title_is
title_contains
presence_of_element_located
visibility_of_element_located
visibility_of
presence_of_all_elements_located
text_to_be_present_in_element
text_to_be_present_in_element_value
frame_to_be_available_and_switch_to_it
invisibility_of_element_located
element_to_be_clickable
staleness_of
element_to_be_selected
element_located_to_be_selected
element_selection_state_to_be
element_located_selection_state_to_be
alert_is_presen
'''
from time import sleep
from selenium import  webdriver
from  selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.support.

driver = webdriver.Chrome()
driver.get('https://testautomationpractice.blogspot.com/')
driver.implicitly_wait(10)
driver.find_element(By.ID,'name').send_keys('Sanjay')
sleep(10)
WebDriverWait(driver,10).until(EC.element_to_be_selected((By.XPATH,'//*[@id="sunday"]')))
WebDriverWait(driver,10).until(EC.text_to_be_present_in_element(('locater','value')))
WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="sunday"]')))







