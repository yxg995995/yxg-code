from pymysql import *
class DataBase:
    
    def __init__(self):
        #数据库名称
        self.db_name='air_qualitydb'
        #填自己mysql的用户名
        user='yxg'
        #填密码
        password='yxg579521..'
        self.db=connect('localhost',user,password,self.db_name)
    
    #数据库表一provinces 属性有Province,citylist
    def insertProvinces(self,province):
        c=self.db.cursor()
        c.executemany('''INSERT into provinces values (%s,%s)''' ,province)
        self.db.commit()
    
    #数据库表二city_href 属性有cityName href
    def insert_City_href(self,city_href):
        c=self.db.cursor()
        c.executemany('''INSERT into city_href values (%s,%s)''' ,city_href)
        self.db.commit()
    
    #获取全国31个省份或者直辖市的省会城市（没有香港，澳门和台湾的数据）
    def get_capital_city(self):
        c=self.db.cursor()
        c.execute('''select cityList from provinces ''')
        result=c.fetchall()
        l=[]
        for i in range(len(result)):
            if i<4:
                l.append(result[i][0])
            else:
                l.append(eval(result[i][0])[0])
        self.db.commit()
        return l
    
    def get_province(self):
        c=self.db.cursor()
        c.execute('''select Province from provinces''')
        result=c.fetchall()
        l=[]
        for i in result:
            l.append(i[0])
        self.db.commit()
        return l
    
    #返回某个省份的全部附属城市
    def get_citylist(self,provinceName):
        c=self.db.cursor()
        c.execute(''' select cityList from provinces where Province = %s ''',provinceName)
        result=c.fetchone()
        self.db.commit()
        return eval(result[0])
        
    #获取某个城市的超链接
    def get_city_href(self,cityName):
        c=self.db.cursor()
        c.execute('''select href from city_href where cityName=%s ''',cityName)
        result=c.fetchone()
        self.db.commit()
        return result
    
    #关闭数据库
    def close(self):
        self.db.close()

if __name__=='__main__':
    db=DataBase()
    a=db.get_capital_city()
    print(a)