import requests
from bs4 import BeautifulSoup
from DataBase import DataBase
import pandas as pd
import numpy as np
import re
from urllib import parse
from selenium import webdriver
import time
from getMonth import get_month_range
from multiprocessing import Pool
import multiprocessing
class Spider:
    def __init__(self):
        self.db=DataBase()
    
    #获取所有城市名
    def autoSpider(self):
        citylist=self.db.getCapitalName()
        pattern1 = re.compile(u'\d{4}-\d{2}-\d{2}')
        pattern2 = re.compile(r'（[\u4e00-\u9fa5]+）')
        Data=[]
        for city in citylist:
            try:
                url='http://www.pm25.in/'+city
                kv={'user-agent':'Mozilla/5.0'}
                r=requests.get(url,headers=kv)
                soup=BeautifulSoup(r.text,'html.parser')
                b=soup.find('div',{'class':'span12 data'})
                data=[city]
                level=soup.find('div',{'class':'level'}).h4.text.strip()
                level=pattern2.search(level).group()[1:-1]
                date=soup.find('div',{'class':'live_data_time'}).p.text.strip()
                date=pattern1.search(date).group()
                data.append(date)
                n=0
                for i in b.find_all('div',{'class':'value'}):
                    if n in [3,5,6,8]:
                        n+=1
                    else:
                        data.append(i.text.strip())
                        n+=1
                data.insert(3,level)
                data[-1],data[-2]=data[-2],data[-1]
                Data.append(data)
            except AttributeError:
                print(city)
        self.db.insert_citydata(Data)
    
if __name__=='__main__':
    spider=Spider()
    spider.getCity()