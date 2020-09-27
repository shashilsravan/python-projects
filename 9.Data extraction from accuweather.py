from selenium import webdriver
import pandas as pd
import time

browser = webdriver.Chrome('chromedriver.exe')
browser.maximize_window()
month = 'august'
year = 2020
url = 'https://www.accuweather.com/en/in/rajahmundry/202193/' + month + '-weather/202193?year=' + str(year) + '&view=list'
browser.get(url)
time.sleep(5)

data = browser.find_elements_by_class_name('high')
temp_high = []
for d in data:
    t = d.get_attribute('textContent')
    temp_high.append(int(t[:2]))

time.sleep(2)
data2 = browser.find_elements_by_class_name('low')
temp_low = []
for d in data2:
    t = d.get_attribute('textContent')
    temp_low.append(int(t[3:5]))

data3 = browser.find_elements_by_xpath("//div[@class='info precip']/p[2]")
precip = []
for d in data3:
    t = d.get_attribute('textContent')
    if t[:2] == '7%':
        precip.append(7)
    else:
        precip.append(float(t[:2]))

date = [i for i in range(1, len(precip)+1)]

df = {'Date': date, "MaxTemp":temp_high, "LowTemp":temp_low, "Precpitation":precip}

df = pd.DataFrame(df)
df.to_csv(month+'.csv')
print('Done')