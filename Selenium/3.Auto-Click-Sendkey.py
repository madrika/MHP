from selenium import webdriver
import os
import time


driver = webdriver.Firefox(executable_path=r'D:\Project\pythonProject\Robot\Selenium\geckodriver.exe')

driver.get("https://Madrika.com")

time.sleep(5)

blog = driver.find_element_by_xpath('//*[@id="navbar"]/div/ul/li[6]/a')
blog.click()
time.sleep(3)
article = driver.find_element_by_xpath('//*[@id="app"]/section[2]/div/div/div[2]/div[2]/div/a')
article.click()
time.sleep(3)
comment = driver.find_element_by_xpath('//*[@id="comment"]/textarea')
comment.send_keys("عالی بود")
time.sleep(2)
Apply = driver.find_element_by_class_name('btn')
Apply.click()


