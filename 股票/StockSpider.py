import requests
import json
import pandas as pd
import numpy as np
import datetime
class Spider:
    def __init__(self,id):
        #股票代码
        self.Stock_code=id
    #从网易财经上爬取某只股票的历史价格并插入到stock表保存    
    def daySpider(self,start,end):
        #起始时间
        start_time=start
        #终止时间
        end_time=end
        #网易url组成
        url="http://quotes.money.163.com/service/chddata.html?code=1"\
                +self.Stock_code+"&start="+start_time+"&end="+end_time+\
                "&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP"
        doc=requests.get(url)
        #去除\n \r等符号
        data=doc.text.splitlines()
        #需要的数据列名字
        clo=['日期','月份','周','名称','开盘价','收盘价','最低价','最高价']
        n=len(data)
        #用于装删选出来的数据
        l1=[]
        #判断股票是否退市或者不存在
        if n==1:
            return False
        #装数据
        for i in range(n-1):
            #将字符串转成列表
            l=data[-i-1].split(',')
            #将时期数据分成列表
            s=l[0].split('-')
            #判断时期属于第几周
            result=self.select_week(s[0],s[1],s[2])
            #l[0][:7]去时期的月份数据
            l1.append([l[0],l[0][0:7],result,l[2],l[6],l[3],l[5],l[4]])
        #转换成DataFarme类型数据
        a=pd.DataFrame(data=l1,columns=clo)
        #保存为csv表 csv表和execel表类似
        a.to_csv('Stock.csv')
        
        #获取每周的数据
        
        #选出所有不同的周数
        week=list(a['周'].unique())
        #保存每周的数据
        week_price=[]
        #装填数据
        for i in week:
            Open=list(a[a['周']==i]['开盘价'])[0]
            Close=list(a[a['周']==i]['收盘价'])[-1]
            High=max(a[a['周']==i]['最高价'])
            Low=min(a[a['周']==i]['最低价'])
            week_price.append([i,Open,Close,Low,High])
        #周表表头 和clo1一样的功能
        clo2=['周','开盘价','收盘价','最低价','最高价']
        b=pd.DataFrame(data=week_price,columns=clo2)
        b.to_csv('week.csv')
        
        #获取每个月的数据
        #同取每周数据类似
        month=list(a['月份'].unique())
        month_price=[]
        for i in month:
            Open=list(a[a['月份']==i]['开盘价'])[0]
            Close=list(a[a['月份']==i]['收盘价'])[-1]
            High=max(a[a['月份']==i]['最高价'])
            Low=min(a[a['月份']==i]['最低价'])
            month_price.append([i,Open,Close,Low,High])
        clo3=['月份','开盘价','收盘价','最低价','最高价']
        c=pd.DataFrame(data=month_price,columns=clo3)
        c.to_csv('month.csv')
        return True
    
    #判断日期属于第几周
    def select_week(self,year,month,day):
        a=datetime.date(eval(year), int(month), int(day)).isocalendar()
        #取年份和周数
        result=str(a[0])+'-'+str(a[1])
        return result
    
    '''import datetime
        datetime.date(2017, 12, 31).isocalendar()
        (2017, 52, 7)　　# 给定2017年12月31日，返回该日期对应2017年的第52周的第7天'''

#可以忽略
if __name__=='__main__':
    # id为股票代码
    id='000001'
    a=Spider(id)
    a.daySpider('20200101', '20201231')