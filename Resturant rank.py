import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import time
import random

title_list=[]
evaluation_list=[]
foodprice_list=[]
image_list=[]

page_form=1

while page_form<=10:
    
    url="https://tabelog.com/tw/rstLst/{}/?LstCatD=RC0101&LstCat=RC01&Cat=RC".format(page_form)  #this web site is regular , we can change page and going to next page 
    my_header={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
        }# Can find in Network. Header can increase crawler successful rate
    response = requests.get(url, headers=my_header)
    
    soup = BeautifulSoup(response.text,"html.parser")
    
    win=soup.find_all('li',class_="list-rst js-list-item")
    win1=win[0]
    win2= win1.find_all('p')
    shop = win2[0].find('a',target="_blank")
    
    valuation= win1.find_all('div',class_="list-rst__contents u-clearfix")
    evaluation = valuation[0].find('b',class_="c-rating__val")
    price= win1.find('li', class_="c-rating c-rating--sm")
    price1=price.find('span',class_="c-rating__val")
    img=win1.find('p',class_="list-rst__img") 
    img1=img.find('a',class_="c-img-target")
    
    
    image=img1.get('href')
    title =shop.text
    evaluation= evaluation.text
    foodprice= price1.text
    

    
    
    for idx,i in enumerate(win):   # Python’s enumerate() to get a counter and the value from the iterable at the same time!
        shop1= i.find('a',target="_blank")
        title=shop1.text
        shopevaluation=i.find('b',class_="c-rating__val")
        evaluation=shopevaluation.text
        shopimage=i.find('a',class_="c-img-target")
        image=shopimage.get('href')
        shopprice=i.find('span',class_="c-rating__val")
        foodprice=shopprice.text
        
        title_list.append(title)
        evaluation_list.append(evaluation)
        foodprice_list.append(foodprice)
        image_list.append(image)

    print(f'======================{idx+1} page  is over==========')
        
    page_form+=1



df = pd.DataFrame(columns=['title','evaluation','price','image'])
df['title'] = title_list
df['evaluation'] = evaluation_list
df['price'] =  foodprice_list
df['image'] = image_list    


dfSort=df.sort_values(by='evaluation',ascending=False).head(20)  #  In descending order by evaluation and take 20 record.
dfSort.reset_index(inplace=True)  

df
