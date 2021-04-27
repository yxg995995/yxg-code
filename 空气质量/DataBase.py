from pymysql import *
import datetime
class DataBase:
    
    def __init__(self):
        #数据库名称
        self.db_name='air_qualitydb'
        #填自己mysql的用户名
        user='yxg'
        #填密码
        password='yxg579521..'
        self.db=connect('localhost',user,password,self.db_name)
    
    def inserCapitalName(self,data):
        c=self.db.cursor()
        c.executemany('insert into capitallist values(%s)',data)
        self.db.commit()
    
    def getCapitalName(self):
        c=self.db.cursor()
        c.execute('''select * from capitallist''')
        result=c.fetchall()
        l=[]
        for i in result:
            l.append(i[0])
        self.db.commit()
        return l
    
    def judgeDate(self):
        date=datetime.date.today()
        date=str(date)
        c=self.db.cursor()
        c.execute('delete from capitalcity where date=%s',date)
        self.db.commit()
    
    def get_cityname(self,cityname,start,end):
        c=self.db.cursor()
        c.execute('''select cityname from capitalcity  where cityname=%s''',cityname)
        result=c.fetchone()
        if result==None:
            self.db.commit()
            return False
        else:
            c.execute('''select aqi,date,pm25,pm10,so2,no2 from 
                      capitalcity where cityname=%s and date>=%s and date<=%s order by date''',(cityname,start,end))
            data=c.fetchall()
            l=[]
            for i in data:
                l.append(list(i))
            return l
    
    def getall(self,cityname,start,end):
        c=self.db.cursor()
        c.execute('select * from capitalcity where cityname=%s and date>=%s and date<=%s order by date',
                  (cityname,start,end))
        self.db.commit()
        result=c.fetchall()
        l=[]
        for i in result:
            l.append(list(i))
        return l
            
    
    def insert_citydata(self,data):
        c=self.db.cursor()
        c.executemany('''insert into capitalcity values (%s,%s,%s,%s,%s,%s,%s,%s)''',data)
        self.db.commit()
        
    def getmapdata(self,date):
        c=self.db.cursor()
        c.execute('''select aqi,level,pm25,pm10,so2,no2 from capitalcity where date=%s order by cityname''',date)
        result=c.fetchall()
        features=[]
        for i in result:
            features.append(list(i))
        self.db.commit()
        return features
        
    
    def getFeature(self,cityname,start,end,feature,q):
        c=self.db.cursor()
        if feature=='PM2.5':
            feature='pm25'
        sql='select * from capitalcity where cityname=%s and '+feature+'>=%s and date>=%s and date<=%s'
        c.execute(sql,(cityname,eval(q),start,end))
        result=c.fetchall()
        self.db.commit()
        if result==None:
            return False
        l=[]
        for i in result:
            l.append(list(i))
        return l
    
    def getLevel1(self,cityname,start,end):
        c=self.db.cursor()
        l=[]
        for i in ['优','良','轻度污染','中度污染','重度污染','严重污染']:
            sql='SELECT count(*) FROM air_qualitydb.capitalcity where cityname=%s\
                    and date>=%s and date<=%s and level=%s'
            c.execute(sql,(cityname,start,end,i))
            result=c.fetchone()[0]
            l.append(result)
        self.db.commit()
        return l
        #关闭数据库
    
    def getcitylist(self):
        c=self.db.cursor()
        c.execute('''select * from air_qualitydb.capitallist''')
        result=c.fetchall()
        l=[]
        for i in result:
            l.append(i[0])
        self.db.commit()
        return l
    
    def getmaxdate(self):
        c=self.db.cursor()
        c.execute('select max(date) from capitalcity')
        result=c.fetchone()[0]
        self.db.commit()
        return result
    
    def close(self):
        self.db.close()

if __name__=='__main__':
    db=DataBase()
    a=db.getmaxdate()