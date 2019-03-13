
# import os
# import time
# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
 
# driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")  #//option[@value='volvo']

 
# driver.maximize_window()
 
# driver.implicitly_wait(30)
# driver.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_select')

# time.sleep()
# ele = driver.find_element_by_xpath('//option[@value="saab"]')

# Select(ele)

# ele.select_by_visible_text('Saab')
 
# driver.quit()

import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
 
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
 
driver.maximize_window()

driver.get('http://www.amazon.com')
search = driver.find_element_by_id('twotabsearchtextbox')
# file = open('test.txt','r')	
search.send_keys('oneplus 6t')
time.sleep(2)
search.send_keys(Keys.RETURN)
rev = driver.find_elements_by_xpath('//span[@class="a-declarative"]//span[@class="a-icon-alt"]') #based on review
val = [float(driver.execute_script("return arguments[0].textContent", a).replace(',','')[:3]) for a in rev]
print(val)
for a in rev:
	xx = float(driver.execute_script("return arguments[0].textContent", a).replace(',','')[:3])
	if xx == max(val):
		value = a.find_element_by_xpath("parent::div")
		# ff = a.find_element_by_xpath('..')
		print(value)
		print(driver.execute_script("return arguments[0].textContent", value))
		# a.find_element_by_xpath("../../../../..").click()
		