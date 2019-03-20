import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def time_space(val):
	return time.sleep(val)

def name():			
	driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
	driver.get('http://amazon.com')
	driver.implicitly_wait(30)
	ele = driver.find_element_by_id('twotabsearchtextbox')
	file = open('test.txt','r')	
	ele.send_keys(file.read())
	time_space(4)
	driver.quit()
