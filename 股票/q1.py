import requests
import json
import pandas as pd
import numpy as np    
#pyecharts python一个很厉害的画图库 动态展示效果
from pyecharts import options as opts
from pyecharts.charts import Kline #pycharts带有画k线的函数
from pyecharts.charts import Line,Tab #画折线图和组合图
def question1(start,end,id):
    #开始时间
    start_time=start
    #结束时间
    end_time=end
    #股票id
    Stock_code=id
    url="http://quotes.money.163.com/service/chddata.html?code=1"\
                +Stock_code+"&start="+start_time+"&end="+end_time+\
                "&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP"
    doc=requests.get(url)
    data=doc.text.splitlines()
    clo=['日期','名称','开盘价','收盘价','最低价','最高价']
    n=len(data)
    l1=[]
    #股票退市或者股票代码不存在 报错
    if n==1:
        return False
    #存放'日期','名称','开盘价','收盘价','最低价','最高价'数据
    for i in range(n-1):
        l=data[-i-1].split(',')
        l1.append([l[0],l[2],l[6],l[3],l[5],l[4]])
    #转换成DataFrame类型便于写入csv表
    a=pd.DataFrame(data=l1,columns=clo)
    a.to_csv('February.csv')
    time=[]
    price=[]
    name=l1[0][1]
    for i in l1:
        time.append(i[0])
        price.append(i[2:])
    #K线图
    kline={
        Kline()
        #横坐标
        .add_xaxis(time)
        #纵坐标
        .add_yaxis("分日K线",price,
                #设置K线的颜色
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
            #标题
            title_opts=opts.TitleOpts(title=name+"2月份K线图"),
            )
        #命名文件名
        .render('2月份线图.html')}

def question2():
    #question1()得到的2月份数据
    data=pd.read_csv('February.csv')
    #总成本=每天的收盘价*100相加
    cost=round(sum(data['收盘价'][0:8])*100,2)
    print('总成本为:{}元'.format(cost))
    #总资产=最后持股数*收盘价
    means=round(800*data['收盘价'][7],2)
    print('总资产为:{}元'.format(means))
    #总收益
    profit=(800*data['收盘价'][8]-cost)
    print('总收益为:{}元'.format(profit))
    rate=question3()
    print('收益率')
    print(rate)
    #最大回撤率
    MIN=min(data['收盘价'][0:8])
    MAX=max(data['收盘价'][0:8])
    max_rate=round((MAX-MIN)/(MAX)*100,2)
    print('最大回撤率{}'.format(max_rate))
    
def question3():
    data=pd.read_csv('February.csv')
    close=data['收盘价'][0:8]
    rate=[0.0]
    time=[]
    means=[]
    for i in range(len(close)):
        if i==7:
            means.append(round(800*close[i],2))
            time.append('第8天')
            pass
        else:
            means.append(round((i+1)*100*close[i],2))
            rate.append(round((close[i+1]-close[i])/close[i]*100,2))
            time.append('第'+str(i+1)+'天')
    #画折线图
    c1=(
       Line()
       .set_global_opts(
         xaxis_opts=opts.AxisOpts(type_="category"),
         yaxis_opts=opts.AxisOpts(
             type_="value",
             axistick_opts=opts.AxisTickOpts(is_show=True),
             splitline_opts=opts.SplitLineOpts(is_show=True),
                ),
            )
       #x轴
       .add_xaxis(time)
       #y轴
       .add_yaxis(
           series_name="资产",
           y_axis=means,
           symbol="emptyCircle",
           is_symbol_show=True,
        )
        )
    #同上
    c2=(
       Line()
       .set_global_opts(
         xaxis_opts=opts.AxisOpts(type_="category"),
         yaxis_opts=opts.AxisOpts(
             type_="value",
             axistick_opts=opts.AxisTickOpts(is_show=True),
             splitline_opts=opts.SplitLineOpts(is_show=True),
                ),
            )
            .add_xaxis(time)
            .add_yaxis(
                series_name="收益率",
                y_axis=rate,
                symbol="emptyCircle",
                is_symbol_show=True,
            )
        )
    #组合图 最后两个折线图能切换看
    tab=Tab()
    tab.add(c1,'总资产折线图')
    tab.add(c2,'收益率折线图')
    tab.render('收益率和总资产组合图.html')
    return rate
if __name__=='__main__':
    id='300175'
    question1('20210201','20210228',id)
    question2()
    question3()