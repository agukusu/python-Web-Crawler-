# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 12:48:02 2021

@author: cooki
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



PATH ="C:/Users/cooki/OneDrive/Desktop/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(PATH)   #Using python open web site


driver.get("https://www.dcard.tw/f")
search=driver.find_element_by_name("query")
search.send_keys("Keyword")
search.send_keys(Keys.RETURN)

WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CLASS_NAME, "sc-3yr054-1"))
)

# Find titles and pick tag

titles= driver.find_elements_by_class_name("tgn9uw-3") 

for title in titles:
    print(title.text)

link =driver.find_element_by_link_text("#分享 狼王12月14日復盤")
link.click()

