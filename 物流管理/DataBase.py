from pymysql import *
import random
class DataBase:
    def __init__(self):
        self.db_name='track_system'
        self.db=connect('localhost','yxg','yxg579521..',self.db_name)
    
    def auto_id(self):
        c=self.db.cursor()
        c.execute('''select max(UserId) from user ''')
        result=c.fetchone()
        self.db.commit()
        return result[0]+1
        
    def insertUser(self,data):
        c=self.db.cursor()
        c.execute('''INSERT into user values (%s,%s,%s,%s,%s,%s,%s,%s)''' ,data)
        self.db.commit()
    
    def find_user(self,username):
        c=self.db.cursor()
        c.execute('''select UserName from user where UserName=%s''',(username))
        result=c.fetchone()
        if result is None:
            return False
        else:
            return True
    
    def find_phone(self,phone):
        c=self.db.cursor()
        c.execute('''select phone from user where phone=%s''',(phone))
        result=c.fetchone()
        if result is None:
            return False
        else:
            return True       
    
    def Verify(self,username,password):
        c=self.db.cursor()
        c.execute('''select UserName,password from user where UserName=%s and password=%s''',
                  (username,password))
        result=c.fetchone()
        if result is None:
            return False
        else:
            return True
    
    def get_message(self,username):
        c=self.db.cursor()
        c.execute('''select * from user where UserName=%s''',username)
        result=c.fetchone()
        self.db.commit()
        return list(result)

    def update(self,username,data):
        c=self.db.cursor()
        c.execute('''delete from user where UserName=%s''',username)
        self.insertUser(data)
        self.db.commit()
    
        
    def get_otherPhone(self,username):
        c=self.db.cursor()
        c.execute('SELECT phone FROM track_system.user where UserName!=%s',username)
        result=c.fetchall()
        l=[]
        for i in result:
            l.append(i[0])
        self.db.commit()
        return l
    
    def getID(self,username):
        c=self.db.cursor()
        c.execute('select OrderId from track_system.order where State=0 and R_name=%s',username)
        result=c.fetchall()
        self.db.commit()
        l=[]
        for i in result:
            l.append(i[0])
        return l
    
    def getItem(self,id):
        c=self.db.cursor()
        c.execute('''select I_temprature,I_humidity,I_light from itme_state where OrderId=%s''',id)
        self.db.commit()
        return c.fetchone()
    
    def update_item(self,data):
        c=self.db.cursor()
        a=random.randint(-5,5)
        b=random.randint(-10,10)
        data[0]+=a
        data[1]+=b
        c.execute('''update itme_state set I_temprature=%s,I_humidity=%s,I_light=%s where OrderId=%s''',data)
        self.db.commit()        
    
    def get_section(self,id):
        c=self.db.cursor()
        c.execute('''SELECT I_class,I_humidity,I_temprature,I_light,I_click FROM track_system.itme_state
        where OrderId=%s''',id)
        result=c.fetchone()
        self.db.commit()
        return list(result)
    
    def judge(self,cla,humi,temp,light,click):
        c=self.db.cursor()
        c.execute('''select temp,humidity from section where class=%s''',cla)
        self.db.commit()
        result=c.fetchone()
        T=eval(result[0])
        H=eval(result[-1])
        if temp<T[0] or temp>T[-1]:
            return True
        if humi<H[0] or humi>H[-1]:
            return True
        if cla=='易碎品':
            if click=='是':
                return True
        if cla=='药品':
            if light=='是':
                return True
        return False
    
    def getCar(self):
        c=self.db.cursor()
        c.execute('''select * from car_detail''')
        result=c.fetchall()
        self.db.commit()
        l=[]
        for i in result:
            l.append(list(i))
        return l
    def get_Car_msg(self,car):
        c=self.db.cursor()
        c.execute('''select OrderId from 
                  logistics where L_car=%s and L_location!="已签收" ''',car)
        result=c.fetchall()
        self.db.commit()
        l=[]
        for i in result:
            l.append(i[0])
        return l
    
    def getloc(self,id):
        c=self.db.cursor()
        c.execute('''select L_location from logistics where OrderId=%s''',id)
        result=c.fetchone()
        self.db.commit()
        return result[0]
if __name__=='__main__':
    db=DataBase()
    a=db.getloc('D000001')
    print(a)
