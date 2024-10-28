'''
driver.get_cookies()
driver.add_cookie('san')
driver.delete_cookie()
driver.delete_all_cookies()
'''


from selenium import  webdriver
import pickle
driver = webdriver.Chrome()

driver.get("http://www.google.com")
Cookies = pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
driver.get_cookies()
driver.add_cookie('san')
driver.delete_cookie()
driver.delete_all_cookies()
print(Cookies)