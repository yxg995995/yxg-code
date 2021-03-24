from pymysql import *


class DataBase:
    
    def __init__(self):
        self.db_name='inventorydb'
        self.db=connect('localhost','yxg','yxg579521..',self.db_name)
        
    def insertUser(self,username,password):
        c=self.db.cursor()
        c.execute('''INSERT into inventorydb.user values (%s,%s)''' ,(username,password))
        self.db.commit()
    
    def find_user(self,username):
        c=self.db.cursor()
        c.execute('''select username from user where username=%s''',(username))
        result=c.fetchone()
        if result is None:
            return False
        else:
            return True
    
    def verify_pass(self,username,password):
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
        c.execute('''select password from system.user where username=%s 
                  ''',(username))
        result=c.fetchone()
        self.db.commit()
        return result
    
    def get_maxid(self):
        c=self.db.cursor()
        c.execute('''select max(product_id) from products''')
        result=c.fetchone()
        return result[0]

    def info_product(self,data):
        c=self.db.cursor()
        product_id=self.get_maxid()+1
        data.insert(0,product_id)
        data=tuple(data)
        c.execute('''INSERT into products values(%s,%s,%s,%s,%s,%s,%s)
                  ''',data)
        self.db.commit()
    
    def get_id(self):
        c=self.db.cursor()
        c.execute('''select product_id from products ''')
        l=[]
        result=c.fetchall()
        for i in result:
           l.append(str(i[0])) 
        return l
    
    def delete(self,product_id):
        c=self.db.cursor()
        c.execute('DELETE FROM products where product_id=%s',product_id)
        self.db.commit()
    
    def update(self,data):
        c=self.db.cursor()
        q='''UPDATE products 
            set product_name=%s,in_price=%s,product_type=%s,
            brand=%s,out_price=%s,number=%s
            where product_id=%s'''
        c.execute(q,tuple(data))
        self.db.commit()
    
    def get_product(self,product_id):
        c=self.db.cursor()
        q='''select * from products where product_id=%s'''
        c.execute(q,product_id)
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
    
    def get_IO(self):
        c=self.db.cursor()
        c.execute('''select info_orderNo from info_order ''')
        l=[]
        result=c.fetchall()
        for i in result:
           l.append(str(i[0])) 
        return l
    
    def delete_IO(self,name):
        c=self.db.cursor()
        c.execute('DELETE FROM info_order where info_orderNo=%s',name)
        self.db.commit()
    
    def get_ID(self):
        c=self.db.cursor()
        c.execute('''select info_orderNo from info_detail''')
        l=[]
        result=c.fetchall()
        for i in result:
           l.append(str(i[0])) 
        return l
    
    def delete_ID(self,id):
        c=self.db.cursor()
        c.execute('DELETE FROM info_detail where info_orderNo=%s',id)
        self.db.commit()
    
    def get_OO(self):
        c=self.db.cursor()
        c.execute('''select out_orderNo from out_order ''')
        l=[]
        result=c.fetchall()
        for i in result:
           l.append(str(i[0])) 
        return l
    
    def delete_OO(self,OOid):
        c=self.db.cursor()
        c.execute('DELETE FROM out_order where out_orderNo=%s',OOid)
        self.db.commit()

    def get_OD(self):
        c=self.db.cursor()
        c.execute('''select out_orderNo from out_detail ''')
        l=[]
        result=c.fetchall()
        for i in result:
           l.append(str(i[0])) 
        return l
    
    def delete_OD(self,No):
        c=self.db.cursor()
        c.execute('DELETE FROM out_detail where out_orderNo=%s',No)
        self.db.commit()
        
    def close(self):
        self.db.close()

if __name__=='__main__':
    db=DataBase()
    data=['春季休闲裤',49,'裤子','李宁',79,520]
    print(db.get_product(1))
