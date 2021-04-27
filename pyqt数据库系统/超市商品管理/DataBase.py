from pymysql import *


class DataBase:
    
    def __init__(self):
        self.db_name='shop'
        self.db=connect('localhost','yxg','yxg579521..',self.db_name)
        
    def insertUser(self,username,password):
        c=self.db.cursor()
        c.execute('''INSERT into user values (%s,%s)''' ,(username,password))
        self.db.commit()
    
    def find_user(self,username):
        c=self.db.cursor()
        c.execute('''select userName from user where username=%s''',(username))
        result=c.fetchone()
        if result is None:
            return False
        else:
            return True
    
    def Verify(self,username,password):
        c=self.db.cursor()
        c.execute('''select userName,password from user where username=%s and password=%s''',
                  (username,password))
        result=c.fetchone()
        if result is None:
            return False
        else:
            return True
    
    def getUser_password(self,username):
        c=self.db.cursor()
        c.execute('''select password from system.user where username=%s 
                  ''',(username))
        result=c.fetchone()
        self.db.commit()
        return result

    def insert(self,tablename,data):
        c=self.db.cursor()
        n=len(data)
        a='%s,'*n
        b=a[:-1]
        data=tuple(data)
        q='INSERT into '+tablename+' values('+b+')'
        c.execute(q,data)
        self.db.commit()
        
    def get_name(self):
        c=self.db.cursor()
        c.execute('''select name from commodity ''')
        l=[]
        result=c.fetchall()
        for i in result:
           l.append(str(i[0])) 
        return l
    
    def delete_commodity(self,name):
        c=self.db.cursor()
        c.execute('DELETE FROM commodity where name=%s',name)
        self.db.commit()
    
    def get_id(self):
        c=self.db.cursor()
        c.execute('''select id from employee''')
        l=[]
        result=c.fetchall()
        for i in result:
           l.append(str(i[0])) 
        return l
    
    def delete_employee(self,id):
        c=self.db.cursor()
        c.execute('DELETE FROM employee where id=%s',id)
        self.db.commit()
    
    def get_receiptNo(self):
        c=self.db.cursor()
        c.execute('''select receiptNo from receipt ''')
        l=[]
        result=c.fetchall()
        for i in result:
           l.append(str(i[0])) 
        return l
    
    def delete_receipt(self,receiptNo):
        c=self.db.cursor()
        c.execute('DELETE FROM receipt where receiptNo=%s',receiptNo)
        self.db.commit()

    def get_detailNo(self):
        c=self.db.cursor()
        c.execute('''select receiptNo from detail ''')
        l=[]
        result=c.fetchall()
        for i in result:
           l.append(str(i[0])) 
        return l
    
    def delete_detail(self,receiptNo):
        c=self.db.cursor()
        c.execute('DELETE FROM detail where receiptNo=%s',receiptNo)
        self.db.commit()
        
    def close(self):
        self.db.close()

if __name__=='__main__':
    db=DataBase()
    data=['春季休闲裤',49,'裤子','李宁',79,520]
    print(db.get_product(1))
