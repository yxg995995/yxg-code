from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line, Pie, Tab,Map,Geo
from Spider import Spider
import time
from multiprocessing import Pool
import time
import multiprocessing
import requests
from bs4 import BeautifulSoup
from DataBase import DataBase
class Drawing:
    
    def __init__(self):
        self.spider=Spider()
    
    #绘制中国
    def China_map(self):
        capitalList=self.spider.db.get_capital_city()
        provinceList=self.spider.db.get_province()
        p = Pool(4)
        start=time.time()
        value=p.map(getAQI,capitalList) 
        p.close()
        p.join()
        print(value)
        end=time.time()
        print(end-start)
        num=len(capitalList)
        data=[]
        data1=[]
        start=time.time()
        for i in range(num):
            data.append([capitalList[i]+'市',value[i]])
            data1.append([provinceList[i],value[i]])
        c=(
           Map()
           .add("PM2.5", data1, 'china')
           .set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=200, is_piecewise=True),
                            title_opts=opts.TitleOpts(title='中国省会城市PM2.5浓度地图')
                            )
        )
        plt=(
            Geo()
            .add_schema(maptype='china')
            .add("PM2.5",data)
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(visualmap_opts=opts.VisualMapOpts(),
                             title_opts=opts.TitleOpts(title='中国省会城市PM2.5浓度地图'))
            
            )
        tab = Tab()
        tab.add(c,'PM2.5-有标注图')
        tab.add(plt, "PM2.5-无标注图")
        tab.render('中国省会城市PM2.5浓度分布图.html')
     
    
    def draw_bar(self,cityList,data)-> Bar:
        c = (
        Bar()
        .add_xaxis(cityList)
        .add_yaxis("PM2.5", data)
        .set_global_opts(
            datazoom_opts=[opts.DataZoomOpts()],
            title_opts=opts.TitleOpts(title="PM2.5柱状图"),
        )
        )
        return c
    
    def draw_Line(self,cityList,data)-> Line:
        c=(
            Line()
            .set_global_opts(
                tooltip_opts=opts.TooltipOpts(is_show=False),
                xaxis_opts=opts.AxisOpts(type_="category"),
                yaxis_opts=opts.AxisOpts(
                    type_="value",
                    axistick_opts=opts.AxisTickOpts(is_show=True),
                    splitline_opts=opts.SplitLineOpts(is_show=True),
                ),
            )
            .add_xaxis(cityList)
            .add_yaxis(
                series_name="PM2.5",
                y_axis=data,
                symbol="emptyCircle",
                is_symbol_show=True,
            )
        )
        return c
    
    def draw_Map(self,data,ProvinceName):
        c=(
           Map()
           .add("PM2.5", data, ProvinceName)
           .set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=200, is_piecewise=True),
                            title_opts=opts.TitleOpts(title=ProvinceName+'PM2.5浓度地图')
                            )
        )
        return c
    
    def Province_map(self,ProvinceName):
        p = Pool(4)
        city_list=self.spider.db.get_citylist(ProvinceName)
        start=time.time()
        value=p.map(getAQI,city_list) 
        p.close()
        p.join()
        print(value)
        end=time.time()
        print(end-start)
        num=len(city_list)
        data=[]
        for i in range(num):
            data.append([city_list[i]+'市',value[i]])
        tab = Tab()
        tab.add(self.draw_Map(data, ProvinceName),'PM2.5-map')
        tab.add(self.draw_bar(city_list,value), "PM2.5-bar")
        tab.add(self.draw_Line(city_list, value), "PM2.5-line")
        tab.render(ProvinceName+'省PM2.5组合图.html')
        
def getAQI(cityName):
    db=DataBase()
    data={}
    url=db.get_city_href(cityName)
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


if __name__=='__main__':
    
    draw=Drawing()
    #draw.Province_map('陕西')
    draw.China_map()
    #draw.Province_map('江西')