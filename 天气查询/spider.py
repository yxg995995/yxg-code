import requests
import json
import pymssql
from DataBase import DataBase
from bs4 import BeautifulSoup
class Spider:
    def __init__(self):
        self.url='https://j.i8tq.com/weather2020/search/city.js'
        self.cityurl="http://www.weather.com.cn/weather/"
        #self.citySpider()
    
    def citySpider(self):
        self.DB=DataBase()
        self.doc=requests.get(self.url)
        self.doc.encoding='utf-8'
        self.l=self.doc.text.replace('var city_data = ','')
        data=json.loads(self.l)
        CITY=[]#
        for i in data:
            for j in data[i]:
                for p in data[i][j]:
                    total=[]
                    total.append(i)
                    total.append(j)
                    total.append(p)
                    total.append(data[i][j][p]['AREAID'])
                    CITY.append(total)
                    self.DB.insertCity(CITY)
                    self.DB.close()
    
    def tempSpider(self,province,city,town):
        self.DB=DataBase()
        ID=self.DB.getcityID(province, city, town)
        
        url=self.cityurl+str(ID[0])+".shtml"
        
        r=requests.get(url)
        r.encoding='utf-8'
        soup=BeautifulSoup(r.text,'html.parser')
        b=soup.find_all(attrs={'class':'sky'})
        time=[]
        temp=[]
        weather=[]
        win=[]
        for i in b[0:3]:
            time.append(i.h1.text)
            l=i.find_all('p')
            weather.append(l[0].text)
            temp.append(l[1].text)
            win.append(l[2].span.get('title'))
        msg1='城市：'+province+'省 '+city+'市 '+town+'区/县'+'\n'
        msg2='时间：'
        msg3='温度：'
        msg4='天气：'
        msg5='风向：'
        for i in range(len(time)):
            if i==len(time)-1:
                msg2+=str(time[i])+'\n'
                msg3+=str(temp[i])+'\n'
                msg4+=weather[i]+'\n'
                msg5+=win[i]
            else:
                msg2+=str(time[i])+'\t'
                msg3+=str(temp[i])+'\t'
                msg4+=weather[i]+'\t'
                msg5+=win[i]+'\t'
            
        result=msg1+msg2+msg3+msg4+msg5
        return result
        