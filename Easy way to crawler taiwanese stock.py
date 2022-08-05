# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 14:13:47 2022

@author: cooki
"""


from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 
import pandas 


PATH ="C:/Users/cooki/OneDrive/Desktop/chromedriver.exe" # Usin selenium have to douwn load chromedriver and control it. 
web = webdriver.Chrome(PATH)
web.implicitly_wait(10)


url = "https://isin.twse.com.tw/isin/class_i.jsp?kind=2&owncode=&stockname=&isincode=&markettype=1&issuetype=3&industry_code="
web.get(url)
#獲取下拉元素

web.find_element_by_css_selector('body > form > table > tbody > tr:nth-child(2) > td:nth-child(2) > input[type=text]').send_keys('Stock Name')
web.find_element_by_css_selector("input[value='確定']").click()

import pandas as pd
data=pd.read_html(web.page_source)[0]   
data.columns=data.iloc[0,:]
data=data.drop(index=[0])
stockNO=data['有價證券代號']
stockName=data['有價證券名稱']
