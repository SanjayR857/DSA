'''
driver.maximize_window()
driver.minimize_window()
driver.set_window_size()
driver.switch_to.frame(frame_ID or frame_Name or XPath)
driver.switch_to.window(window_handle)
driver.switch_to.default_content()
driver.switch_to.new_window()
driver.switch_to.parent_frame()
'''

from selenium import  webdriver
from selenium.webdriver.common.by import By
from time import  sleep
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get('https://www.geeksforgeeks.org/software-testing-manual-testing/')
driver.maximize_window()
sleep(3)
#driver.minimize_window()
sleep(2)
driver.set_window_size(100,300)
sleep(2)
driver.maximize_window()
driver.get('https://ui.vision/demo/webtest/frames/')
sleep(3)

#frame handles
IFrame = ['/html/frameset/frame[1]','/html/frameset/frameset/frame[1]','/html/frameset/frameset/frame[2]','/html/frameset/frameset/frame[3]']
driver.switch_to.frame(driver.find_element(By.XPATH,IFrame[0]))
driver.find_element(By.NAME,'mytext1').send_keys('Sanjay')
sleep(2)
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element(By.XPATH,IFrame[1]))
driver.find_element(By.NAME,'mytext2').send_keys('Kiran')
sleep(2)
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element(By.XPATH,IFrame[2]))
driver.find_element(By.NAME,'mytext3').send_keys('Vikas')
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element(By.XPATH,IFrame[3]))
driver.find_element(By.NAME,'mytext4').send_keys('Vikas23')
sleep(2)

# WINDOW
driver.get('https://demo.automationtesting.in/Windows.html')
sleep(1)
driver.find_element(By.XPATH,'//*[@id="Tabbed"]/a/button').click()
sleep(5)
window_handle_dict = {}
list_window = driver.window_handles
for i in range(len(list_window)):
    window_handle_dict[i] = list_window[i]
sleep(1)
print(window_handle_dict)
driver.switch_to.window(window_handle_dict[1])
sleep(4)
if driver.current_window_handle==window_handle_dict[1]:
    print('True')
else:
    print('Not')
    print(driver.current_window_handle)
sleep(5)
driver.switch_to.window(window_handle_dict[0])
if driver.current_window_handle==window_handle_dict[0]:
    print('True')
else:
    print('Not')
    print(driver.current_window_handle)
