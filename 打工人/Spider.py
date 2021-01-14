import requests
import json
from DataBase import DataBase
class Spider:
    def __init__(self):
        self.db=DataBase()
        #股票代码
        self.Stock_code="000002"
    #从网易财经上爬取某只股票的历史价格并插入到表1保存    
    def daySpider(self):
        start_time=20200701
        end_time=20201231
        url="http://quotes.money.163.com/service/chddata.html?code=1"\
                +self.Stock_code+"&start="+str(start_time)+"&end="+str(end_time)+\
                "&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP"
        doc=requests.get(url)
        data=doc.text.splitlines()
        n=len(data)
        for i in range(n-1):
            l=data[-i-1].split(',')
            self.db.InsertTB1(l[0],l[6],l[3],l[5],l[4])
            
    #从东方财富网爬取某只股票的一天里面9：30到15：00每分钟的股票价格并插入表2保存
    def minSpider(self):
        url='http://pdfm.eastmoney.com/EM_UBG_PDTI_Fast/api/js?rtntype=5&id='+self.Stock_code+\
        '2&type=r&iscr=false'
        doc=requests.get(url)
        l=doc.text.replace('(','').replace(')','')
        data=json.loads(l)
        for i in data['data']:
            l=i.split(',')
            self.db.InsertTB2(l[0],l[1])

if __name__=='__main__':
    spider=Spider()
    spider.daySpider()
    spider.minSpider()