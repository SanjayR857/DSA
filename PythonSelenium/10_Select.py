'''
country = Select(driver.find_element(By.ID,'country'))

country.select_by_visible_text('text')
country.select_by_visible_index(index_number)
country.select_by_visible_value('value')
country.deselect_by_visible_text('text')
country.all_selected_options
country.options
country.first_selected_option
'''
from time import sleep
from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://testautomationpractice.blogspot.com/')

country = Select(driver.find_element(By.ID,'country'))

country.select_by_visible_text('Canada')
sleep(3)
country.select_by_index(2)
sleep(3)
country.select_by_value('usa')
sleep(3)

colors = Select(driver.find_element(By.ID,'colors'))

colors.select_by_value('red')
sleep(3)
print(colors.all_selected_options)
for i in colors.all_selected_options:
    print(i.text,end=' ')
colors.deselect_by_value('red')
sleep(3)
colors_drop_down = colors.options

for i in colors_drop_down:
    print(i.text)
