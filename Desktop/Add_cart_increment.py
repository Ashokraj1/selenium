import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

driver.get('http://amazon.com')
driver.implicitly_wait(30)
ele = driver.find_element_by_id('twotabsearchtextbox')
ele.send_keys('sony mobiles')
ele.send_keys(Keys.RETURN)


ele = driver.find_elements_by_xpath('//span[@class="a-price-whole"]') #based on price

val = [float(driver.execute_script("return arguments[0].textContent", a).replace(',','')) for a in ele]
for a in ele:
	x = float(driver.execute_script("return arguments[0].textContent", a).replace(',',''))
	if x == min(val):
		a.click()
		driver.find_element_by_id('add-to-cart-button').click()

		for tim in range(3):
			try:
				if driver.find_element_by_class_name('is-open'):
					cond = driver.find_element_by_class_name('is-open')
			except:
				cond = ''		
			if cond:
				driver.find_element_by_class_name('uss-o-close-icon-medium').click()
			else:
				driver.back()
			time.sleep(1)	
			driver.find_element_by_id('add-to-cart-button').click()
		driver.refresh()	
		driver.find_element_by_id('nav-cart-count').click()
		