from selenium import webdriver
import urllib.request

browser = webdriver.Chrome('chromedriver.exe')
link = 'https://www.instagram.com/'

# Profile Name
name = '_s.a.n_j.a.n.a_'
profile = link + name + '/'
browser.get(profile)
try:
    image = browser.find_element_by_xpath('//img[@class="_6q-tv"]')
except:
    image = browser.find_element_by_xpath('//img[@class="be6sR"]')
img_link = image.get_attribute('src')

path = name+'.jpg'
urllib.request.urlretrieve(img_link, path)