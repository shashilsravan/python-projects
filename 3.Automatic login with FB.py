from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

userid = '9182409060'
passid = 'Sravan@123'

browser = webdriver.Chrome('chromedriver.exe')
browser.maximize_window()
browser.get('https://www.facebook.com')

username = browser.find_element_by_xpath('.//*[@id="email"]')
username.send_keys(userid)

password = browser.find_element_by_id('pass')
password.send_keys(passid)

login = browser.find_element_by_id('u_0_b')
login.click()


time.sleep(10)
browser.get('https://www.facebook.com/')
time.sleep(5)

message = 'Hello J'
post = browser.find_element_by_xpath('//*[@name="xhpc_message"]')
post.send_keys(message)
time.sleep(5)
buttons = browser.find_elements_by_tag_name('button')
try:
    for button in buttons:
        if button.text == 'Post':
            button.click()
except:
    pass