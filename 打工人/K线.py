from DataBase import DataBase
from pyecharts import options as opts
from pyecharts.charts import Kline #pycharts带有画k线的函数
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import talib as ta
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

class PlotK:
    def __init__(self):
        self.db=DataBase()

    def K1(self):
        data=self.db.GetDayData()
        time=[]#装日期
        price=[]#装日的开盘价，收盘价，最高价，最低价
        for i in data:
            time.append(i[0])
            price.append(i[1:])
        kline=Kline()
        kline.add_xaxis(time)
        kline.add_yaxis("分日K线",price)
        kline.set_global_opts(title_opts=opts.TitleOpts(title="K线图"))
        kline.render("分日K线.html")
    
    def K2(self):
        data=self.db.GetMinData()
        time=[]
        price=[]
        for i in data:
            time.append(i[0])
            price.append(i[1])
        Open=0
        Close=0
        Low=0
        High=0
        price2=[]
        for i in range(int(len(price)/60)):#计算出每个小时的开盘价，收盘价，最高价，最低价
            d=[]
            Open=price[i*60]
            Close=price[60*(i+1)]
            Low=min(price[i*60:60*(i+1)])
            High=max(price[i*60:60*(i+1)])
            d.append(Open)
            d.append(Close)
            d.append(Low)
            d.append(High)
            price2.append(d)
        date=[]
        for j in range(len(time)):#生成每天的小时时间
            year=time[j].split(' ')[0]
            if j%240==0 and j!=0:
                date.append(year+" 10:30")
                date.append(year+" 11:30/13:00")
                date.append(year+" 14:00")
                date.append(year+" 15:00")
                if j==len(time)-1:
                    year=''
                else:
                    year=time[j+1].split(' ')[0]
        kline=Kline()
        kline.add_xaxis(date)
        kline.add_yaxis("K线", price2)
        kline.set_global_opts(
        title_opts=opts.TitleOpts(title="分时K线图"))
        kline.render('分时K线.html')
    
    def JDK(self):
        data=self.db.GetDayData()
        time=[]
        price=[]
        for i in range(len(data)):
            time.append(data[i][0])
            price.append(data[i][1:])
        fig = plt.figure(figsize=(5,2), dpi=100,facecolor="white")
        price=pd.DataFrame(price,columns=['open','close','low','high'])
        K,D=ta.STOCH(price.high.values, price.low.values, price.close.values,
                        fastk_period=9, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)
        J=3*K-2*D
        plt.plot(np.arange(0, len(time)),K, 'blue', label='K')  # K
        plt.plot(np.arange(0, len(time)),D, 'g--', label='D')  # D
        plt.plot(np.arange(0, len(time)),J, 'r-', label='J')  # J
        plt.legend(loc='best', shadow=True, fontsize='10')
        plt.ylabel(u"KDJ")
        plt.xlabel("日期")
        plt.xlim(0, len(time))  # 设置一下x轴的范围 
        x=[]
        lable=[]
        for i in range(0,len(time),15):
            x.append(i)
            lable.append(time[i])
        # X轴刻度设定 每15天标一个日期， 标签设置为日期
        plt.xticks(x,lable) 
        plt.xticks(rotation=45)
        plt.show()
        
    def MACD(self):
        data=self.db.GetDayData()
        fig = plt.figure(figsize=(5,2), dpi=100,facecolor="white")
        time=[]
        price=[]
        for i in range(len(data)):
            time.append(data[i][0])
            price.append(data[i][1:])
        price=pd.DataFrame(price,columns=['open','close','low','high'])
        macd_dif, macd_dea, macd_bar = ta.MACD(price.close.values, fastperiod=12, slowperiod=26, signalperiod=9)
        plt.plot(np.arange(0, len(time)), macd_dif, 'red', label='macd dif')  # dif
        plt.plot(np.arange(0, len(time)), macd_dea, 'blue', label='macd dea')  # dea
        
        bar_red = np.where(macd_bar > 0, 2 * macd_bar, 0)# 绘制BAR>0 柱状图
        bar_green = np.where(macd_bar < 0, 2 * macd_bar, 0)# 绘制BAR<0 柱状图
        plt.bar(np.arange(0, len(time)), bar_red, facecolor='red')
        plt.bar(np.arange(0, len(time)), bar_green, facecolor='green')
        
        plt.legend(loc='best',shadow=True, fontsize ='10')
        plt.ylabel(u"MACD")
        plt.xlim(0,len(time)) #设置一下x轴的范围
        plt.xticks(range(0,len(time),15))#X轴刻度设定 每15天标一个日期
        plt.show()
        
        
if __name__=='__main__':
    plot=PlotK()
    plot.JDK()
    plot.K1()
    plot.K2()
    plot.MACD()

    