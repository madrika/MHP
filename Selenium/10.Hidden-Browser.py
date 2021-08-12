from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from colorama import Fore , Style
from password import username , password
import random
import os
import time



options = webdriver.ChromeOptions()
options.headless = True

addresss = os.path.abspath(__file__)
addresss = os.path.dirname(addresss)
addresss = os.path.join(addresss , 'chromedriver.exe')

driver = webdriver.Chrome(executable_path=addresss ,options=options)

os.system('cls')
driver.get('https://Madrika.com')

time.sleep(2)

t = driver.find_element_by_xpath('//*[@id="app"]/footer/div/div[2]/div[4]/a[2]').text
open('Madrika.txt' , 'w').write(t)