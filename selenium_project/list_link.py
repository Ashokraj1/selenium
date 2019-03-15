import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def link():
	browser = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
	browser.get('http://www.google.com')
	search = browser.find_element_by_name('q')
	search.send_keys('Python')
	search.send_keys(Keys.RETURN)
	time.sleep(2)
	link_list = []
	elems = browser.find_elements_by_xpath("//a[@href]")
	for a in elems[:10]:
		val = a.get_attribute('href')
		print(val)
		link_list.append(val)
	return link_list
	browser.quit()