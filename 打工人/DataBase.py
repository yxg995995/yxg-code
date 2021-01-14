import sqlite3
class DataBase:
    def __init__(self):
        #自定义数据库名字
        self.DBname='D:/股票价格.db'
    
    #创建存储每天股票价格的数据表
    def CreateTable1(self):
        self.OpenDB()
        #sql语句
        sql='''create table everyday_gp (everyday datetime,openprice numeric(6,2),
        closeprice numeric(6,2),lowestprice numeric(6,2),highestprice numeric(6.2))'''
        self.cur.execute(sql)
        self.close()
        
    #创建存储当天每分钟股价的数据表
    def CreateTable2(self):
        self.OpenDB()
        #sql语句
        sql='''create table everymin_gp (everyminute datetime,nowprice numeric(6,2))'''
        self.cur.execute(sql)
        self.close()
        
    #将每天的股票的历史数据插入表1
    def InsertTB1(self,everyday,openprice,closeprice,lowestprice,highestprice):
        self.OpenDB()
        sql='''insert into everyday_gp  values (?,?,?,?,?)'''
        self.cur.execute(sql,(everyday,openprice,closeprice,lowestprice,highestprice))
        self.close()
        
    #将当天每分钟的股票价格插入表2
    def InsertTB2(self,everyminute,nowprice):
        self.OpenDB()
        sql='''insert into everymin_gp values (?,?)'''
        self.cur.execute(sql,(everyminute,nowprice))
        self.close()
    
    #查询表1每天的股价
    def GetDayData(self):
        self.OpenDB()
        sql='''select * from everyday_gp '''
        self.cur.execute(sql)
        result=self.cur.fetchall()
        self.close()
        return result
    
    #查询表2每分钟的股价
    def GetMinData(self):
        self.OpenDB()
        sql='''select * from everymin_gp'''
        self.cur.execute(sql)
        result=self.cur.fetchall()
        self.close()
        return result
    
    #打开数据库,有就打开，没有就创建
    def OpenDB(self):
        self.db=sqlite3.connect(self.DBname)
        self.cur=self.db.cursor()

    #释放游标，关闭数据库
    def close(self):
        self.db.commit()
        self.db.close()
    
if __name__=='__main__':
    DB=DataBase()
    DB.CreateTable1()
    DB.CreateTable2()