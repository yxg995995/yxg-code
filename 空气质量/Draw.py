from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line, Pie, Tab,Map,Geo,PictorialBar,Page
from pyecharts.components import Table
from Spider import Spider
import time
from multiprocessing import Pool
import time
import multiprocessing
import requests
from bs4 import BeautifulSoup
from DataBase import DataBase
from pyecharts.globals import SymbolType
from pyecharts.commons.utils import JsCode
from pyecharts.options import ComponentTitleOpts
import numpy as np
class Drawing:
    
    def __init__(self):
        self.db=DataBase()
    

        
    def draw_Line(self,cityname,time,feature):
        avg=round(np.mean(np.array(feature[1:])),1)
        c=(
            Line()
            .set_global_opts(
                title_opts=opts.TitleOpts(title=cityname+feature[0]+"折线图",
                                          subtitle=cityname+feature[0]+'平均值:'+str(avg)),
                xaxis_opts=opts.AxisOpts(type_="category"),
                yaxis_opts=opts.AxisOpts(
                    type_="value",
                    axistick_opts=opts.AxisTickOpts(is_show=True),
                    splitline_opts=opts.SplitLineOpts(is_show=True),
                ),
            )
            .add_xaxis(time)
            .add_yaxis(
                series_name=feature[0],
                y_axis=feature[1:],
                symbol="emptyCircle",
                is_symbol_show=True,
                markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="min"),
                                                               opts.MarkPointItem(type_="max")]),
            )
            .render(cityname+feature[0]+"折线图.html")
        )
    
        
    def draw2_Line(self,city1,city2,time,feature1,feature2,level1,level2):
        avg1=round(np.mean(np.array(feature1[1:])),1)
        avg2=round(np.mean(np.array(feature2[1:])),1)
        line= (
            Line()
            .add_xaxis(time)
            .add_yaxis(city1, 
                       feature1[1:],
                       markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="min"),
                                                               opts.MarkPointItem(type_="max")]),)
            .add_yaxis(city2, 
                       feature2[1:],
                       markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="min"),
                                                               opts.MarkPointItem(type_="max")]),)
            .set_global_opts(title_opts=opts.TitleOpts(title=city1+'与'+city2+'的'+feature1[0]+"对比折线图",
                subtitle=city1+feature1[0]+'平均值:'+str(avg1)+"  "+city2+feature2[0]+'平均值:'+str(avg2)))
        )
        
        level=['优','良','轻度污染','中度污染','重度污染','严重污染']
        pie1= (
            Pie()
            .add("", [list(z) for z in zip(level,level1)])
            .set_global_opts(title_opts=opts.TitleOpts(title=city1+"空气质量等级"))
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {d}%"))
        )
        
        pie2= (
            Pie()
            .add("", [list(z) for z in zip(level,level2)])
            .set_global_opts(title_opts=opts.TitleOpts(title=city2+"空气质量等级"))
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {d}%"),)
        )
        page = Page()
        page.add(line,pie1,pie2)
        page.render('不同城市的'+feature1[0]+"比较图.html")
        
    def draw_map(self,features,date):
        citys=['上海','新疆','甘肃','北京','江苏','广西','江西','安徽','内蒙古',
               '黑龙江','天津','山西','广东','四川','西藏','云南','浙江','湖北',
               '辽宁','山东','海南','河北','福建','青海','陕西','贵州','河南',
               '重庆','宁夏','吉林','湖南','']
        data=[list(z) for z in zip(citys,features)]
        c= (
            Map()
            .add("", data, "china",)
            .set_global_opts(title_opts=opts.TitleOpts(title='各省会城市 '+date+' 空气概括图'),
                             visualmap_opts=opts.VisualMapOpts(),
             tooltip_opts=opts.TooltipOpts('axis',formatter=JsCode('''function(params){
              return    params.data.name+'<br/>'+
                      'AQI:'+params.data.value[0]+'<br/>'+
                      '空气质量等级：'+params.data.value[1]+'<br/>'+
                      'PM2.5：'+params.data.value[2]+'<br/>'+
                      'PM10：'+params.data.value[3]+'<br/>'+
                      'SO2：'+params.data.value[4]+'<br/>'+
                      'NO2：'+params.data.value[5]}''',)
              )
                            )
           .render('各省会城市的地图.html')              
        )
                 
    def draw_map1(self,features,date):
        citys=['上海','新疆','甘肃','北京','江苏','广西','江西','安徽','内蒙古',
               '黑龙江','天津','山西','广东','四川','西藏','云南','浙江','湖北',
               '辽宁','山东','海南','河北','福建','青海','陕西','贵州','河南',
               '重庆','宁夏','吉林','湖南','']
        data=[list(z) for z in zip(citys,features)]
        c= (
            Map()
            .add("", data, "china",)
            .set_global_opts(title_opts=opts.TitleOpts(title='各省会城市 '+date+' 空气概括图'),
                             visualmap_opts=opts.VisualMapOpts(),
             tooltip_opts=opts.TooltipOpts('axis',formatter=JsCode('''function(params){
              return    params.data.name+'<br/>'+
                      'AQI:'+params.data.value[0]+'<br/>'+
                      '空气质量等级：'+params.data.value[1]+'<br/>'+
                      'PM2.5：'+params.data.value[2]+'<br/>'+
                      'PM10：'+params.data.value[3]+'<br/>'+
                      'SO2：'+params.data.value[4]+'<br/>'+
                      'NO2：'+params.data.value[5]}''',)
              )
                            )
           .render('各省会城市'+date+'的地图.html')              
        )
    
    def draw_table(self,cityname,start,end,feature,q,l):
        table = Table()
        headers =['城市名','时间','AQI','质量等级','PM2.5','PM10','SO2','NO2']
        rows = l
        table.add(headers, rows)
        table.set_global_opts(
            title_opts=ComponentTitleOpts(title=cityname+feature+'值>'+q+'的详细数据', 
                                          subtitle='时间范围:'+start+'~'+end)
        )
        table.render("指标分析表格图.html")
    
    def draw_bar(self,cityname,start,end,level,data):
        c = (
            Bar()
            .add_xaxis(level)
            .add_yaxis("天数", data)
            .set_global_opts(title_opts=opts.TitleOpts(title=cityname+"空气质量等级分布情况", 
                                                       subtitle='时间范围:'+start+'~'+end))
            .render("等级分布图.html")
        )

if __name__=='__main__':
    pass