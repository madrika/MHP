from selenium import webdriver
import os
import time

path = os.path.dirname(os.path.abspath(__file__))
address = os.path.join(path , "chromedriver.exe")

driver = webdriver.Chrome(address)
driver.get("https://instagram.com")

time.sleep(5)

#1
# test = driver.find_element_by_name("username")
# test.send_keys("test")

#2
# test = driver.find_element_by_class_name("_2hvTZ")
# test.send_keys("test")

#3
# test = driver.find_element_by_css_selector("#loginForm > div > div:nth-child(1) > div > label > input")
# test.send_keys("test")

#4
# test = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
# test.send_keys("test")

#5
# test = driver.find_elements_by_tag_name("h1")
# print(test)

#6
# test = driver.find_element_by_partial_link_text("t pass")
# test.click()


#7
# test = driver.find_element_by_link_text("Forgot password?")
# test.click()

#8
# Custom XPATH----   Xpath = //tagname[@Attribute='Value']

test = driver.find_element_by_xpath('//input[@name = "username"]')
test.send_keys('test')
