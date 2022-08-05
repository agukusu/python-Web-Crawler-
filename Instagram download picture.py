# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 16:45:15 2021

@author: cooki
"""

from tkinter import YView
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os
import wget # Download Web Page and FILES

PATH ="C:/Users/cooki/OneDrive/Desktop/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.instagram.com/")



username = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.NAME, "username"))
        )
password = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.NAME, "password"))
        )
#定義出帳號密碼的標籤
username.send_keys('Your Account')
password.send_keys('Your Password')

Login= driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button') #find button position and click it.
Login.click()

search = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input'))
        )
keyword = "魔動閃霸"
search.send_keys(keyword)
time.sleep(1)
search.send_keys(Keys.RETURN)
time.sleep(1)
search.send_keys(Keys.RETURN)
#Instagram has to send two times.



WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CLASS_NAME, "FFVAD"))
        )

path = os.path.join(keyword)
os.mkdir(path)    #create file

count=0

#Following we are finding the tag and wen site
imgs = driver.find_elements_by_class_name("FFVAD")

for img in imgs:
    save_as= os.path.join(path,keyword+str(count)+'.jpg')
   # print(img.get_attribute("src"))
    wget.download(img.get_attribute("src"),save_as)
    count += 1



