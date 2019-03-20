import time
import json
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

def time_space(val):
	return time.sleep(val)

def register():
	file = open('signup.json','r')
	json_file = json.load(file)
	for a,b in json_file.items():
		driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
		driver.get('https://learn.dummies.com/ls/register')
		driver.maximize_window()	
		time_space(3)
		driver.find_element_by_name('fname').send_keys(b['name'])
		time_space(1)
		driver.find_element_by_name('email').send_keys(b['email'])
		time_space(1)
		driver.find_element_by_name('password').send_keys(b['password'])
		time_space(1)
		driver.find_element_by_name('passwordConf').send_keys(b['confp'])
		time_space(1)
		driver.find_element_by_xpath('//label[@class="checkbox"]').click()
		driver.find_element_by_xpath('//a[contains(text(),"Select a course")]').click()
		time_space(1)
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time_space(1)
		driver.find_element_by_xpath('//a[contains(text(),"%s")]'%b['course']).click()
		time_space(2)
		driver.find_element_by_id('signupBtn').click()
		time_space(12)
		driver.quit()

	