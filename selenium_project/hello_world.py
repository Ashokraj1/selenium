from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def hello():
	browser = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
	browser.get('http://www.google.com')
	browser.quit()