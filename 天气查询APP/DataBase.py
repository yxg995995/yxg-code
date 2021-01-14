from pymysql import *


class DataBase:
    
    def __init__(self):
        self.db_name='city'
        self.db=connect('localhost','yxg','yxg579521',self.db_name)
        
    def insertCity(self,citylist):
        c=self.db.cursor()
        c.executemany('''INSERT into city values (%s,%s,%s,%s)''' ,citylist)
        self.db.commit()
    def getcityID(self,province,city,area):
        c=self.db.cursor()
        c.execute('''select id from city.city where province=%s 
                  and city=%s and area=%s ''',(province,city,area))
        result=c.fetchone()
        self.db.commit()
        return result
    
    def getmsg(self):
        c=self.db.cursor()
        c.execute('''select * from city ''')
        result=c.fetchall()
        self.db.commit()
        return result
    
    def close(self):
        self.db.close()


        
        
        
