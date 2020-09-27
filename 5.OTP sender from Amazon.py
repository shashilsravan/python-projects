from selenium import webdriver

browser = webdriver.Chrome('chromedriver.exe')
browser.maximize_window()
browser.get('https://www.amazon.in/ap/signin?_encoding=UTF8&ignoreAuthState=1&openid.assoc_handle=inflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3Fref_%3Dnav_custrec_signin&switch_account=')

email = browser.find_element_by_xpath('//*[@id="ap_email"]')

# Place the number here
email.send_keys('7997603815')

sendBtn = browser.find_element_by_xpath('//*[@id="continue"]')
sendBtn.click()

sendOTP = browser.find_element_by_id('continue')
sendOTP.click()

times = 10
for _ in range(times):
    browser.find_element_by_link_text("Resend OTP").click()
