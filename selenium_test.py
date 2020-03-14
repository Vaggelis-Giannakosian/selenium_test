import time

from selenium import webdriver


chrome_browser = webdriver.Chrome('./chromedriver')


chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

# assert we are on the correct page
assert 'Selenium Easy Demo' in chrome_browser.title

# find button
button = chrome_browser.find_element_by_css_selector('#get-input button')
button_text= button.get_attribute('innerHTML')

assert 'Show Message' in chrome_browser.page_source

user_message = chrome_browser.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys('I AM sooo coool')


first_stop = input('Press Enter to continue')

time.sleep(1)
button.click()
output_message = chrome_browser.find_element_by_id('display')

assert 'I AM sooo coool' in output_message.text



time.sleep(7);
chrome_browser.close()
chrome_browser.close()

chrome_browser.quit()
chrome_browser.quit()