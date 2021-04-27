import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWebEngineWidgets import *
from DataBase import DataBase
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Ui_compare import Ui_compare
from Ui_now import Ui_monitor
from Draw import Drawing
from Spider import Spider
from Ui_air import Ui_Air
import datetime
import time
import pandas as pd
import numpy as np
class Air(QWidget):
    def __init__(self):
        self.spider=Spider()
        super(Air, self).__init__()
        self.db=DataBase()
        self.draw=Drawing()
        self.air=Ui_Air()
        self.air.setupUi(self)
        self.citylist=self.db.getcitylist()
        self.air.city1.addItems(self.citylist)
        self.air.city21.addItems(self.citylist)
        self.air.city22.addItems(self.citylist)
        self.air.city51.addItems(self.citylist)
        self.air.city31.addItems(self.citylist)
        self.air.city32.addItems(self.citylist)
        self.air.clear11.clicked.connect(self.Clear1)
        self.air.clear21.clicked.connect(self.Clear2)
        self.air.clear31.clicked.connect(self.Clear3)
        self.air.clear41.clicked.connect(self.Clear41)
        self.air.clear41.clicked.connect(self.Clear42)
        self.air.draw11.clicked.connect(self.Draw1)
        self.air.draw22.clicked.connect(self.Draw2)
        self.air.draw31.clicked.connect(self.Draw3)
        self.air.draw41.clicked.connect(self.Draw41)
        self.air.draw42.clicked.connect(self.Draw42)
        self.air.download.clicked.connect(self.Download)
        self.air.auto_btn.clicked.connect(self.prepare)
        self.first()
        
        
    def Download(self):
        cityname=self.air.city51.currentText()
        if cityname=='':
            replay=QMessageBox.warning(self,'警告','请勿查询空值')
            return
        start=self.air.start51.text()
        end=self.air.end51.text()
        date=datetime.date.today()
        date=str(date)
        if start>end or start>date or end>date:
            replay=QMessageBox.warning(self,'警告','时间有问题')
            return
        if not self.db.get_cityname(cityname, start, end):
            replay=QMessageBox.information(self,'提示','暂无该城市数据')
            self.air.city11.clear()
        else:
            data=self.db.getall(cityname, start, end)
            columns=['城市名','时间','AQI','质量等级','PM2.5','PM10','SO2','NO2']
            df=pd.DataFrame(data=data,columns=columns)
            df.to_csv(cityname+start+'~'+end+'空气质量数据.csv',index=0)
            replay=QMessageBox.information(self,'提示','下载成功')
            
    def prepare(self):
        self.db.judgeDate()
        start=time.time()
        self.spider.autoSpider()
        end=time.time()
        replay=QMessageBox.information(self,'提示','自动采集数据完毕,一共耗时'+str(end-start)+'秒')
        
    def first(self):
        date=self.db.getmaxdate()
        features=self.db.getmapdata(date)
        self.draw.draw_map1(features,date)
        url='D:/GitHub/yxg-code/打工人/空气质量/'+'各省会城市'+date+'的地图.html'
        self.air.webEngineView.load(QUrl(url))
        
    def Clear1(self):
        self.air.city1.clear()
        self.air.city1.addItems(self.citylist)
        self.air.start1.setDateTime(QDateTime(QDate(2021, 2, 1), QTime(0, 0, 0)))
        self.air.end1.setDateTime(QDateTime(QDate(2021, 2, 1), QTime(0, 0, 0)))
        url=''
        self.air.webEngineView11.load(QUrl(url))
        self.air.webEngineView12.load(QUrl(url))
        self.air.webEngineView13.load(QUrl(url))
        self.air.webEngineView14.load(QUrl(url))
        self.air.webEngineView15.load(QUrl(url))

    def Clear2(self):
        self.air.city21.clear()
        self.air.city22.clear()
        self.air.city21.addItems(self.citylist)
        self.air.city22.addItems(self.citylist)
        self.air.start2.setDateTime(QDateTime(QDate(2021, 2, 1), QTime(0, 0, 0)))
        self.air.end2.setDateTime(QDateTime(QDate(2021, 2, 1), QTime(0, 0, 0)))
        url=''
        self.air.webEngineView21.load(QUrl(url))
        self.air.webEngineView22.load(QUrl(url))
        self.air.webEngineView23.load(QUrl(url))
        self.air.webEngineView24.load(QUrl(url))
        self.air.webEngineView25.load(QUrl(url))
    
    def Clear3(self):
        self.air.start3.setDateTime(QDateTime(QDate(2021, 2, 1), QTime(0, 0, 0)))
        url=''
        self.air.webEngineView31.load(QUrl(url))
        
    def Clear41(self):
        self.air.city31.clear()
        self.air.city31.addItems(self.citylist)
        self.air.start41.setDateTime(QDateTime(QDate(2021, 2, 1), QTime(0, 0, 0)))
        self.air.end41.setDateTime(QDateTime(QDate(2021, 2, 1), QTime(0, 0, 0)))
        self.air.feature.clear()
        features=['AQI','PM2.5','PM10','SO2','NO2']
        self.air.feature.addItems(features)
        url=''
        self.air.webEngineView41.load(QUrl(url))

    def Clear42(self):
        self.air.city32.clear()
        self.air.city32.addItems(self.citylist)
        self.air.start42.setDateTime(QDateTime(QDate(2021, 2, 1), QTime(0, 0, 0)))
        self.air.end42.setDateTime(QDateTime(QDate(2021, 2, 1), QTime(0, 0, 0)))
        url=''
        self.air.webEngineView42.load(QUrl(url))
        
    def Draw1(self):
        cityname=self.air.city1.currentText()
        if cityname=='':
            replay=QMessageBox.warning(self,'警告','请勿查询空值')
            return
        start=self.air.start1.text()
        end=self.air.end1.text()
        date=datetime.date.today()
        date=str(date)
        if start>end or start>date or end>date:
            replay=QMessageBox.warning(self,'警告','时间有问题')
            return
        if not self.db.get_cityname(cityname, start, end):
            replay=QMessageBox.information(self,'提示','暂无该城市数据')
            self.air.city11.clear()
        else:
            data=self.db.get_cityname(cityname, start, end)
            aqi=['AQI']
            time=[]
            pm25=['PM2.5']
            pm10=['PM10']
            so2=['SO2']
            no2=['NO2']
            for i in data:
                aqi.append(i[0])
                time.append(i[1])
                pm25.append(i[2])
                pm10.append(i[3])
                so2.append(i[4])
                no2.append(i[5])
            self.draw.draw_Line(cityname, time, aqi)
            self.draw.draw_Line(cityname, time, pm25)
            self.draw.draw_Line(cityname, time, pm10)
            self.draw.draw_Line(cityname, time, so2)
            self.draw.draw_Line(cityname, time, no2)
            url1='D:/GitHub/yxg-code/打工人/空气质量/'+cityname+'AQI折线图.html'
            self.air.webEngineView11.load(QUrl(url1))
            url2='D:/GitHub/yxg-code/打工人/空气质量/'+cityname+'PM2.5折线图.html'
            self.air.webEngineView12.load(QUrl(url2))
            url3='D:/GitHub/yxg-code/打工人/空气质量/'+cityname+'PM10折线图.html'
            self.air.webEngineView13.load(QUrl(url3))
            url4='D:/GitHub/yxg-code/打工人/空气质量/'+cityname+'SO2折线图.html'
            self.air.webEngineView14.load(QUrl(url4))
            url5='D:/GitHub/yxg-code/打工人/空气质量/'+cityname+'NO2折线图.html'
            self.air.webEngineView15.load(QUrl(url5))
            
            
            
    def Draw2(self):
        cityname1=self.air.city21.currentText()
        cityname2=self.air.city22.currentText()
        if cityname1=='' or cityname2=='':
            replay=QMessageBox.warning(self,'警告','请勿查询空值')
            return
        if cityname1==cityname2:
            replay=QMessageBox.warning(self,'警告','请选择不同的城市')
            return
        start=self.air.start2.text()
        end=self.air.end2.text()
        date=datetime.date.today()
        date=str(date)
        if start>end or start>date or end>date:
            replay=QMessageBox.warning(self,'警告','时间有问题')
            return
        if not self.db.get_cityname(cityname1, start, end):
            replay=QMessageBox.information(self,'提示','暂无该城市1数据')
            self.air.city21.clear()
            return
        if not self.db.get_cityname(cityname2, start, end):
            replay=QMessageBox.information(self,'提示','暂无该城市2数据')
            self.air.city22.clear()
        else:
            data1=self.db.get_cityname(cityname1, start, end)
            data2=self.db.get_cityname(cityname2, start, end)
            level1=self.db.getLevel1(cityname1,start,end)
            level2=self.db.getLevel1(cityname2,start,end)
            aqi1=['AQI']
            aqi2=['AQI']
            time=[]
            pm25_1=['PM2.5']
            pm25_2=['PM2.5']
            pm10_1=['PM10']
            pm10_2=['PM10']
            so2_1=['SO2']
            so2_2=['SO2']
            no2_1=['NO2']
            no2_2=['NO2']
            for i in data1:
                aqi1.append(i[0])
                time.append(i[1])
                pm25_1.append(i[2])
                pm10_1.append(i[3])
                so2_1.append(i[4])
                no2_1.append(i[5])
            for j in data2:
                aqi2.append(j[0])
                pm25_2.append(j[2])
                pm10_2.append(j[3])
                so2_2.append(j[4])
                no2_2.append(j[5])
            self.draw.draw2_Line(cityname1,cityname2,time, aqi1,aqi2,level1,level2)
            self.draw.draw2_Line(cityname1,cityname2, time, pm25_1,pm25_2,level1,level2)
            self.draw.draw2_Line(cityname1,cityname2, time, pm10_1,pm10_2,level1,level2)
            self.draw.draw2_Line(cityname1, cityname2,time, so2_1,so2_2,level1,level2)
            self.draw.draw2_Line(cityname1,cityname2, time, no2_1,no2_2,level1,level2)
            url1='D:/GitHub/yxg-code/打工人/空气质量/不同城市的AQI比较图.html'
            self.air.webEngineView21.load(QUrl(url1))
            url2='D:/GitHub/yxg-code/打工人/空气质量/不同城市的PM2.5比较图.html'
            self.air.webEngineView22.load(QUrl(url2))
            url3='D:/GitHub/yxg-code/打工人/空气质量/不同城市的PM10比较图.html'
            self.air.webEngineView23.load(QUrl(url3))
            url4='D:/GitHub/yxg-code/打工人/空气质量/不同城市的SO2比较图.html'
            self.air.webEngineView24.load(QUrl(url4))
            url5='D:/GitHub/yxg-code/打工人/空气质量/不同城市的NO2比较图.html'
            self.air.webEngineView25.load(QUrl(url5))
        
            
    def Draw3(self):
        date=self.air.start3.text()
        date1=datetime.date.today()
        date1=str(date1)
        if date>date1:
            replay=QMessageBox.warning(self,'警告','时间有问题')
        else:
            features=self.db.getmapdata(date)
            self.draw.draw_map(features,date)
            url='D:/GitHub/yxg-code/打工人/空气质量/各省会城市的地图.html'
            self.air.webEngineView31.load(QUrl(url))
        
    def Draw41(self):
        cityname=self.air.city31.currentText()
        if cityname=='':
            replay=QMessageBox.warning(self,'警告','请勿查询空值')
            return
        start=self.air.start41.text()
        end=self.air.end41.text()
        date=datetime.date.today()
        date=str(date)
        feature=self.air.feature.currentText()
        q=self.air.q.text()
        if start>end or start>date or end>date:
            replay=QMessageBox.warning(self,'警告','时间有问题')
            return
        if not self.db.get_cityname(cityname, start, end):
            replay=QMessageBox.information(self,'提示','暂无该城市数据')
            self.air.city41.clear()
        elif not q.isdigit():
            replay=QMessageBox.warning(self,'警告','阈值必需为整数')
        elif q=='' or eval(q)<=0:
            replay=QMessageBox.warning(self,'警告','阈值请勿为空或小于零')
        else:
            
            result=self.db.getFeature(cityname, start, end, feature, q)
            if not result:
                replay=QMessageBox.information(self,'提示','阈值大于现有数据最大值')
            else:
                self.draw.draw_table(cityname, start, end, feature, q, result)
                url='D:/GitHub/yxg-code/打工人/空气质量/指标分析表格图.html'
                self.air.webEngineView41.load(QUrl(url))
                
    def Draw42(self):
        cityname=self.air.city32.currentText()
        if cityname=='':
            replay=QMessageBox.warning(self,'警告','请勿查询空值')
            return
        start=self.air.start42.text()
        end=self.air.end42.text()
        date=datetime.date.today()
        date=str(date)
        if start>end or start>date or end>date:
            replay=QMessageBox.warning(self,'警告','时间有问题')
            return
        if not self.db.get_cityname(cityname, start, end):
            replay=QMessageBox.information(self,'提示','暂无该城市数据')
            self.air.city42.clear()
        else:
            level=['优','良','轻度污染','中度污染','重度污染','严重污染']
            data=self.db.getLevel1(cityname, start, end)
            self.draw.draw_bar(cityname, start, end, level, data)
            url='D:/GitHub/yxg-code/打工人/空气质量/等级分布图.html'
            self.air.webEngineView42.load(QUrl(url))

class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.ui=Air()
        self.ui.show()
    

if __name__=="__main__":
    app=QApplication(sys.argv)
    win=Main()
    sys.exit(app.exec_())
        