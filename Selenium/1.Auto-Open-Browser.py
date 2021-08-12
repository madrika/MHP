from selenium import webdriver
import os
import time

path = os.path.dirname(os.path.abspath(__file__))
address = os.path.join(path , "chromedriver.exe")

driver = webdriver.Chrome(address)
driver.get('https://instagram.comte')

time.sleep(5)

#Close All Browser Page
driver.quit()
#Close Current Browser Page
# driver.close()