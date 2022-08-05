import time 
import random
import requests
from bs4 import BeautifulSoup
import os
import pandas as pd

class books_webcrl:
    def __init__(self):
        pass

    def make_dir(self,path): 
        if not os.path.exists(path):
            os.makedirs(path)


    def webcrl(self,my_key,page_from,target_page):
        title_list = []
        price_list = []
        img_ink_list = []
        while page_from<=target_page:
            try:
                rst = random.randint(10,25)
                url =  'https://search.books.com.tw/search/query/cat/all/sort/1/v/0/spell/3/ms2/ms2_1/page/'+str(page_from)+'/key/'+my_key
                my_headers = {
                    'Host': 'search.books.com.tw',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.3'  
                }
                response = requests.get(url, headers = my_headers)
                response.text
                soup = BeautifulSoup(response.text , 'html.parser')
                windoes = soup.find_all('table',class_ = "table-searchlist clearfix")
                windows_bs4 = windoes[0]
                boxs = windows_bs4.find_all('tbody')
                boxs # items in the box
                for idx,box in enumerate(boxs):
                    box_a   = box.find('a',target="_blank")
                    box_img = box_a.find('img')
                    img_link = box_img.get('data-srcset')
                    title    = box_a.get('title')

                    boxs_price = box.find_all('td')[2]
                    prices = boxs_price.find('ul', class_="list-nav clearfix")
                    boxs_strong = prices.find_all('strong')
                    price = boxs_strong[-1].text

                    title_list.append(title)
                    price_list.append(price)
                    img_ink_list.append(img_link)
                print(f'======這頁({page_from})內容爬取完成了,休息{rst}秒========')
                page_from = page_from+1

                time.sleep(rst)
            except:
                print('偵測到錯誤')
                time.sleep(5)
                pass
        return title_list , price_list , img_ink_list