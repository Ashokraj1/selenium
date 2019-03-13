import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
browser.get('http://www.google.com')
time.sleep(1)
search = browser.find_element_by_name('q')
file = open('test.txt','r')
search.send_keys(file.read())
browser.implicitly_wait(30)
browser.quit()