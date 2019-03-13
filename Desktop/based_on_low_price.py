
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
 
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
 
driver.maximize_window()

driver.get('http://www.amazon.com')
search = driver.find_element_by_id('twotabsearchtextbox')
file = open('test.txt','r')	
search.send_keys(file.read())
time.sleep(2)
ele = driver.find_elements_by_xpath('//span[@class="a-price-whole"]') #based on price
rev = driver.find_elements_by_xpath('//span[@class="a-declarative"]//span[@class="a-icon-alt"]') #based on review

val = [float(driver.execute_script("return arguments[0].textContent", a).replace(',','')) for a in ele]

for a in ele:
	print(a)
	x = float(driver.execute_script("return arguments[0].textContent", a).replace(',',''))
	print(x)
	if x == min(val):
		a.click()
		driver.find_element_by_id('add-to-cart-button').click()
		driver.refresh();
		driver.find_element_by_id('nav-cart-count').click()

driver.quit()