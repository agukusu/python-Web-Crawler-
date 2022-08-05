import requests
from bs4 import BeautifulSoup

import os 

class new:
    def __init__(self,):
        pass
    
    def mkdir_(self,path):
        if not os.path.exists(path):
            os.makedirs(path)

    def news_crl(self,img_lim=10):
        url =  'https://www.ettoday.net/news/hot-news.htm'
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'}

        res = requests.get(url , headers = headers)
        res.text
        soup = BeautifulSoup(res.text , 'html.parser')
        soup  
        boxs = soup.find_all('div',class_='piece clearfix')
    
        title_list =[]
        img_list = []
        for box in boxs:
            try:
                title    = box.find('img').get('title')
                if title == None:
                    break
                img_link = box.find('img').get('data-original')
                title_list.append(title)
                if len(title_list)==img_lim+1:
                    break
                img_list .append(img_link)
                print(title)
                print(img_link)
                print('======================================')
            
            except:
                break

        n=0   
        for link in img_list:
            L = 'https:'+ link
            urllib.request.urlretrieve(L,f'./0115/{n}.jpg')
            n=n+1
