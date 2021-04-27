from pymysql import *
import datetime
class DataBase:
    def __init__(self):
        self.db_name='xinxi'
        self.db=connect('localhost','yxg','yxg579521..',self.db_name)
        
    def insertUser(self,username,password,phone):
        c=self.db.cursor()
        c.execute('''INSERT into user values (%s,%s,%s)''' ,(username,password,phone))
        self.db.commit()
    
    def find_user(self,username):
        c=self.db.cursor()
        c.execute('''select username from user where username=%s''',(username))
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
        c.execute('''select username,password from user where username=%s and password=%s''',
                  (username,password))
        result=c.fetchone()
        if result is None:
            return False
        else:
            return True
    
    def getUser_password(self,username):
        c=self.db.cursor()
        c.execute('''select password from username where username=%s 
                  ''',(username))
        result=c.fetchone()
        self.db.commit()
        return result
    
    def insertAdmin(self,username,password,email):
        c=self.db.cursor()
        c.execute('''INSERT into admin values (%s,%s,%s)''' ,(username,password,email))
        self.db.commit()
    
    def find_admin(self,username):
        c=self.db.cursor()
        c.execute('''select adminName from admin where adminName=%s''',(username))
        result=c.fetchone()
        if result is None:
            return False
        else:
            return True
    
    def find_email(self,email):
        c=self.db.cursor()
        c.execute('''select email from admin where email=%s''',(email))
        result=c.fetchone()
        if result is None:
            return False
        else:
            return True   
        
    def Verify_admin(self,username,password):
        c=self.db.cursor()
        c.execute('''select adminName,password from admin where adminName=%s and password=%s''',
                  (username,password))
        result=c.fetchone()
        if result is None:
            return False
        else:
            return True
    
    def getAdmin_password(self,username):
        c=self.db.cursor()
        c.execute('''select password from username where username=%s 
                  ''',(username))
        result=c.fetchone()
        self.db.commit()
        return result
        
        
    def insert_menu(self,data):
        c=self.db.cursor()
        c.executemany('''insert into menu values (%s,%s,%s,%s,%s)''',data)
        self.db.commit()
        
    def is_empty(self,id):
        c=self.db.cursor()
        c.execute('''select status from xinxi.table where id=%s ''',(id))
        result=c.fetchone()
        self.db.commit()
        if result[0]=='空':
            return True
        else:
            return False
    
    def set_full(self,id):
        c=self.db.cursor()
        c.execute('''update xinxi.table set status='已订' where id=%s''',(id))
        self.db.commit()
    
    def insert(self,tablename,data):
        c=self.db.cursor()
        n=len(data)
        a='%s,'*n
        b=a[:-1]
        data=tuple(data)
        q='INSERT into '+tablename+' values('+b+')'
        c.execute(q,data)
        self.db.commit()
        
    def get_mesg(self,Class):
        c=self.db.cursor()
        c.execute('''select pic,name,price from menu where class=%s ''',Class)
        l=[]
        result=c.fetchall()
        for i in result:
            l.append(list(i))
        return l
    
    def insert_order(self,data):
        self.delete_order()
        c=self.db.cursor()
        c.executemany('''insert into xinxi.order values(%s,%s,%s,%s)''', data)
        self.db.commit()
    
    def delete_order(self):
        c=self.db.cursor()
        c.execute('truncate table xinxi.order')
        self.db.commit()
    
    def insert_parameters(self,data):
        self.delete_parameters()
        c=self.db.cursor()
        c.execute('''insert into xinxi.parameters values(%s,%s,%s,%s,%s)''', data)
        self.db.commit()
    
    def delete_parameters(self):
        c=self.db.cursor()
        c.execute('truncate table xinxi.parameters')
        self.db.commit()
    
    
    def get_parameters(self):
        c=self.db.cursor()
        c.execute('''select * from xinxi.parameters ''')
        l=[]
        result=c.fetchall()
        for i in result[0]:
            l.append(list(eval(i)))
        return l
    
    def set_parameters(self):
        self.delete_parameters()
        self.insert_parameters(['[0,0,0,0]','[0,0,0,0,0]','[0,0,0,0,0,0]','[0,0,0,0,0]','[0,0,0,0,0,0]'])
    
    def get_quantityAndprice(self):
        c=self.db.cursor()
        c.execute('''SELECT sum(quantity),sum(price) from xinxi.order;''')
        result=c.fetchone()
        self.db.commit()
        l=[]
        for i in result:
            l.append(int(i))
        return l
    
    def get_order(self):
        c=self.db.cursor()
        c.execute('select * from xinxi.order')
        result=c.fetchall()
        self.db.commit()
        return result
    
    def insert_allOrder(self,username):
        c=self.db.cursor()
        c.execute('select * from xinxi.order')
        result=c.fetchall()
        l=[]
        date=datetime.datetime.now()
        for i in result:
            a=list(i)
            a.insert(0,username)
            a.insert(1,date)
            l.append(a)
        c.executemany('''insert into xinxi.all_order values(%s,%s,%s,%s,%s,%s)''',l)
        self.db.commit()

    def get_tableid(self):
        c=self.db.cursor()
        c.execute('''select id from xinxi.table''')
        result=c.fetchall()
        l=[]
        self.db.commit()
        for i in result:
            l.append(str(i[0]))
        return l
    
    def update_table(self,id):
        c=self.db.cursor()
        c.execute('''update xinxi.table set status='空' where id=%s''',id)
        self.db.commit()
    
    def setTable_empty(self):
        l=self.get_tableid()
        for i in l:
            self.update_table(eval(i))
            
    
    def get_menuName(self):
        c=self.db.cursor()
        c.execute('''select name from xinxi.menu''')
        result=c.fetchall()
        l=[]
        self.db.commit()
        for i in result:
            l.append(i[0])
        return l
    
    def get_menu(self,name):
        c=self.db.cursor()
        c.execute('''select * from xinxi.menu where name=%s''',name)
        result=c.fetchall()
        self.db.commit()
        return list(result[0])
    
    def update_menu(self,data):
        c=self.db.cursor()
        c.execute('''update xinxi.menu
                  set name=%s,class=%s,pic=%s,price=%s,introduction=%s 
                  where name=%s''',data)
        self.db.commit()
    
    def delete_menu(self,name):
        c=self.db.cursor()
        c.execute('DELETE FROM xinxi.menu where name=%s',name)
        self.db.commit()
    
    def insert(self,tablename,data):
        c=self.db.cursor()
        n=len(data)
        a='%s,'*n
        b=a[:-1]
        data=tuple(data)
        q='INSERT into '+tablename+' values('+b+')'
        c.execute(q,data)
        self.db.commit()
    
    def get_user(self):
        c=self.db.cursor()
        c.execute('''select username from user ''')
        result=c.fetchall()
        l=[]
        self.db.commit()
        for i in result:
            l.append(i[0])
        return l
    
    def delete_user(self,name):
        c=self.db.cursor()
        c.execute('DELETE FROM xinxi.user where username=%s',name)
        self.db.commit()
    
    def getSUM(self):
        c=self.db.cursor()
        c.execute('''select sum(sum) from xinxi.all_order''')
        result=c.fetchone()
        return result[0]
    def close(self):
        self.db.close()

import pandas as pd
import numpy as np
if __name__=='__main__':
    db=DataBase()
    data=db.getSUM()
    print(data)
