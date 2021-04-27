from pyecharts import options as opts
from pyecharts.charts import Kline #pycharts带有画k线的函数
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import talib as ta
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

class Drawing:
    def __init__(self):
        pass
    def dayK(self):
        #读取每天的数据
        data=pd.read_csv('Stock.csv')
        time=[]#装日期
        price=[]#装日的开盘价，收盘价，最高价，最低价
        time=list(data['日期'])
        self.name=data['名称'][0]#股票名字
        #将数据加入price
        for i in range(len(data)):
            price.append([data['开盘价'][i],data['收盘价'][i],
                          data['最低价'][i],data['最高价'][i]])
        #画K线图  详情可以去网上查pyecharts
        kline={
               Kline()
               #时间轴数据
               .add_xaxis(time)
               #y轴数据
               .add_yaxis("分日K线",price,
                          #颜色设置
                          itemstyle_opts=opts.ItemStyleOpts(
                            color="#ec0000",
                            color0="#00da3c",
                            border_color="#8A0000",
                            border_color0="#008F28",)
                          )
               #详情看pyecharts
               .set_global_opts(
                xaxis_opts=opts.AxisOpts(is_scale=True),
                yaxis_opts=opts.AxisOpts(
                    is_scale=True,
                    splitarea_opts=opts.SplitAreaOpts(
                        is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
                    ),
                ),
                datazoom_opts=[opts.DataZoomOpts(type_="inside")],
                #标题
                title_opts=opts.TitleOpts(title=self.name+"日K线图"),
                )
               #输出为
               .render('日K线图.html')
               }
    
    def weekK(self):
        #同上
        data=pd.read_csv('week.csv')
        time=[]
        time=list(data['周'])
        price=[]
        for i in range(len(data)):
            price.append([data['开盘价'][i],data['收盘价'][i],
                          data['最低价'][i],data['最高价'][i]])
        kline={
               Kline()
               .add_xaxis(time)
               .add_yaxis("分周K线",price,
                          itemstyle_opts=opts.ItemStyleOpts(
                            color="#ec0000",
                            color0="#00da3c",
                            border_color="#8A0000",
                            border_color0="#008F28",)
                          )
               .set_global_opts(
                xaxis_opts=opts.AxisOpts(is_scale=True),
                yaxis_opts=opts.AxisOpts(
                    is_scale=True,
                    splitarea_opts=opts.SplitAreaOpts(
                        is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
                    ),
                ),
                datazoom_opts=[opts.DataZoomOpts(type_="inside")],
                title_opts=opts.TitleOpts(title=self.name+"周K线图"),
                )
               .render('周K线图.html')
               }   

    
    def monthK(self):
        #同上
        data=pd.read_csv('month.csv')
        time=[]
        time=list(data['月份'])
        price=[]
        for i in range(len(data)):
            price.append([data['开盘价'][i],data['收盘价'][i],
                          data['最低价'][i],data['最高价'][i]])
        kline={
               Kline()
               .add_xaxis(time)
               .add_yaxis("分月K线",price,
                          itemstyle_opts=opts.ItemStyleOpts(
                            color="#ec0000",
                            color0="#00da3c",
                            border_color="#8A0000",
                            border_color0="#008F28",)
                          )
               .set_global_opts(
                xaxis_opts=opts.AxisOpts(is_scale=True),
                yaxis_opts=opts.AxisOpts(
                    is_scale=True,
                    splitarea_opts=opts.SplitAreaOpts(
                        is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
                    ),
                ),
                datazoom_opts=[opts.DataZoomOpts(type_="inside")],
                title_opts=opts.TitleOpts(title=self.name+"月K线图"),
                )
               .render('月K线图.html')
               }   

#无关紧要的语句 学过面向对象可能会理解 不会也不要紧 可留可不留
if __name__=='__main__':
    pass

    
