from pymysql import *
import pandas as pd
import numpy as np
class DataBase:
    def __init__(self):
        self.db=connect(host='localhost', user='yxg', password='yxg579521..', database='memorandum',port=3306)
    
    def insertMsg(self,date,msg):
        c=self.db.cursor()
        c.execute('insert into message values (%s,%s)',(date,msg))
        self.db.commit()
    
    def getMsg(self,date):
        c=self.db.cursor()
        c.execute('select * from message where date>=%s order by date ',date)
        result=c.fetchall()
        self.db.commit()
        l=[]
        for i in result:
            l.append(list(i))
        if result==None:
            return ''
        else:
            return l
    
    def getDate(self,date):
        c=self.db.cursor()
        c.execute('select date from message where date=%s',date)
        result=c.fetchone()
        self.db.commit()
        if result==None:
            return False
        else:
            return True
    def getoneMsg(self,date):
        c=self.db.cursor()
        c.execute('select *  from  message  where date=%s',date)
        self.db.commit()
        result=c.fetchone()
        return result[1]
        
    def deleteMsg(self,date):
        c=self.db.cursor()
        c.execute('delete from  message  where date=%s',date)
        self.db.commit()
    
        
if __name__ == '__main__':
    db=DataBase()
    data=db.getoneMsg('2021-04-24')
    
