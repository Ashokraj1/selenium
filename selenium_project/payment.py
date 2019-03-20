import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def time_space(val):
	return time.sleep(val)

def payment():
	driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')

	driver.get('http://amazon.com')

	driver.maximize_window()

	ele = driver.find_element_by_id('twotabsearchtextbox')

	ele.send_keys('one plus 6t')

	ele.send_keys(Keys.RETURN)

	driver.find_element_by_xpath('//span[contains(text(),"OnePlus 6T A6013 128GB Storage")]').click()
	driver.find_element_by_id('add-to-cart-button').click()
	driver.refresh();
	driver.find_element_by_id('nav-cart-count').click()
	time_space(1)
	driver.find_element_by_xpath('//input[@value="Proceed to checkout"]').click()
	time_space(3)
	driver.find_element_by_id('ap_email').send_keys('rashokmpi@gmail.com') #use your amazon username
	driver.find_element_by_id('ap_password').send_keys('qwer1234')  #use your amazon password
	driver.find_element_by_id('signInSubmit').click()
	time_space(3)
	driver.find_element_by_xpath('//a[contains(text(),"Deliver to this")]').click()
	time_space(2)
	driver.find_element_by_xpath('//div[@class="a-row a-spacing-medium"]//child::input').click()
	time_space(1)
	driver.find_element_by_xpath('//a[@class="a-link-expander a-declarative"]').click()
	time_space(1)
	driver.find_element_by_id('ccName').send_keys('Ashok')
	driver.find_element_by_id('addCreditCardNumber').send_keys('4111111111111111')
	driver.find_element_by_id('ccAddCard').click()
	time_space(5)
	# driver.quit()