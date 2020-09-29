#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver')

# print(chrome_browser)
chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

assert 'Selenium Easy Demo' in chrome_browser.title
button_text = chrome_browser.find_element_by_class_name("btn-default")
print(button_text.get_attribute('innerHTML'))

assert 'Show Message' in chrome_browser.page_source

user_message = chrome_browser.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys('I AM EXTRA COOL')
button_text.click()
output_message = chrome_browser.find_element_by_id('display')
assert 'I AM EXTRA COOL' in output_message.text

user_button2 = chrome_browser.find_element_by_css_selector('#get-input > .btn')
print(user_button2)

chrome_browser.quit()

