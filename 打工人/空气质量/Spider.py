import requests
from bs4 import BeautifulSoup
from DataBase import DataBase
import pandas as pd
class Spider:
    def __init__(self):
        self.db=DataBase()
        pass
    
    def getHref(self):
        #用列表类型保存省份和城市,方便后面插入数据库
        Province=[]
        City=[]
        #爬取数据的网站是“天气后报”链接为“http://www.tianqihoubao.com/”
        #选取空气质量的链接如下
        url='http://www.tianqihoubao.com/aqi/'
        province_data=requests.get(url)
        province_data.encoding='gbk'
        province_data.status_code
        soup=BeautifulSoup(province_data.text,'html.parser')
        html=soup.find_all('div',{'class':'citychk'})
        for i in html:
            detail_data=i.find_all('dl')
            #选出detail_data的第一个数据，这里面包含直辖市的数据
            for  Municipalities in detail_data[0].find_all('a'):
                cityName=Municipalities.text.strip()
                #观察网页结果发下4个直辖市都在前面，所以当选到广州数据时跳出此时的for循环
                if cityName=='广州':
                    break
                city_href=Municipalities.get('href')
                Province.append((cityName,cityName))
                href='http://www.tianqihoubao.com/'+city_href
                City.append((cityName,href))
            for j in detail_data[1:]:
                Province_name=j.dt.text
                city=[]
                for data in j.find_all('a'):
                    city.append(data.text.strip())
                    href='http://www.tianqihoubao.com/'+data.get('href')
                    City.append((data.text.strip(),href))
                Province.append((Province_name,str(city)))
        #数据保存在csv表中
        a=pd.DataFrame(Province,columns=['省份','附属城市'])
        b=pd.DataFrame(City,columns=['城市名','超链接'])
        a.to_csv('各省及附属城市.csv')
        b.to_csv('城市名及链接.csv')
        #数据保存在数据库中
        self.db.insertProvinces(Province)
        self.db.insert_City_href(City)
    
    #feature 空气质量指标包含下面的选项 AQI,PM2.5,CO,SO2,PM10,O3,NO2
    def getAQI(self,cityName):
        data={}
        url=self.db.get_city_href(cityName)
        url=url[0]
        data['cityName']=cityName
        r=requests.get(url)
        r.encoding='gbk'
        soup=BeautifulSoup(r.text,'html.parser')
        b=soup.find_all('div',{'class':'mod-tab-quality'})
        for i in b:
            #空气质量指数
            aqi=i.find('div',{'class':'num'}).text.strip()
            data['AQI']=aqi
            status=i.find('div',{'class':'status'}).text.strip()
            data['status']=status
            J=i.find_all('li')
            PM2=J[0].text.strip().split('：')[-1]
            CO=J[1].text.strip().split('：')[-1]
            SO2=J[2].text.strip().split('：')[-1]
            PM10=J[3].text.strip().split('：')[-1]
            O3=J[4].text.strip().split('：')[-1]
            NO2=J[5].text.strip().split('：')[-1]
            data['PM2.5']=PM2
            data['CO']=CO
            data['SO2']=SO2
            data['PM10']=PM10
            data['O3']=O3
            data['NO2']=NO2
            
        return int(data['PM2.5'])

#面向对象编程，如果数据库没有数据则先运行这个爬虫程序，如果数据库有数据则直接进行画图
if __name__=='__main__':
    spider=Spider()
    spider.getHref()