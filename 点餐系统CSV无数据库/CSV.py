import pandas as pd
import numpy as np

# 用于订单数据，用户数据，菜单数据的一系列操作
class Operate:
    def __init__(self):
        pass
    
    #查询用户是否存在
    def find_user(self,user):
        data=pd.read_csv('用户.csv')
        if user in np.array(data['username']).tolist():
            return True
        else:
            return False
    
    #查询管理员ID是否存在
    def find_ID(self,id):
        data=pd.read_csv('管理员.csv')
        if id in np.array(data['管理员ID']).tolist():
            return True
        else:
            return False    
    #验证用户名和密码
    def verify_user(self,user,password):
        data=pd.read_csv('用户.csv')
        if [user,password] in np.array(data).tolist():
            return True
        else:
            return False
    
    #验证管理员的用户名和密码
    def verify_Admin(self,user,password):
        data=pd.read_csv('管理员.csv')
        if [user,password] in np.array(data).tolist():
            return True
        else:
            return False    
        
    #注册成功后，用户表插入新用户
    def insert_user(self,user,password):
        data=pd.read_csv('用户.csv')
        data=data.append([{'username':user,'password':password}])
        data.to_csv('用户.csv',index=0)
        
    #管理员注册成功后，管理员表插入新管理员
    def insert_admin(self,id,password):
        data=pd.read_csv('管理员.csv')
        data=data.append([{'管理员ID':id,'密码':password}])
        data.to_csv('管理员.csv',index=0)   
    
    
    #获取菜单名称
    def get_Menu_Name(self):
        data=pd.read_csv('菜单.csv')
        name=np.array(data['菜名']).tolist()
        return name
    
    #获取某个菜品的价格
    def get_price(self,menuname):
        data=pd.read_csv(r'菜单.csv')
        price=np.array(data[data['菜名']==menuname]['价格'])[0]
        return eval(price[0:-1])
    
    
    #获取临时订单的编号
    def get_temporary_No(self):
        data=pd.read_csv('临时订单.csv')
        result=data['订单编号'][0]
        return result
        
    #插入临时订单数据
    def insert_temporary(self,data):
        columns=['订单编号','订单人','时间','菜名','数量','价格','总计']
        order=pd.DataFrame(data=data,columns=columns)
        order.to_csv('临时订单.csv',index=0)
    
    #更新临时订单
    def update_temporary(self,data):
        old=pd.read_csv(r'临时订单.csv')
        columns=['订单编号','订单人','时间','菜名','数量','价格','总计']
        new=pd.DataFrame(data=data,columns=columns)
        old=old.append(new,ignore_index=True)
        old.to_csv('临时订单.csv',index=0)
    
    #清空临时订单
    def clear_temporary(self):
        columns=['订单编号','订单人','时间','菜名','数量','价格','总计']
        order=pd.DataFrame(data=[],columns=columns)
        order.to_csv('临时订单.csv',index=0)
    
    #删除某个订单
    def delete_temporary(self,menuname):
        data=pd.read_csv('临时订单.csv')
        data=data.drop(index=(data.loc[(data['菜名']==menuname)].index))
        data.to_csv('临时订单.csv',index=0)
        
    #判断临时订单是否为空
    def judge_empty(self):
        data=pd.read_csv('临时订单.csv')
        if len(data)==0:
            return True
        else:
            return False
        
    #获取临时订单的菜名信息
    def get_temporary_Name(self):
        data=pd.read_csv('临时订单.csv')
        name=np.array(data['菜名']).tolist()
        return name
    
    #获取临时订单的数量和总计
    def get_temporary_Price_and_num(self):
        data=pd.read_csv('临时订单.csv')
        prices=np.array(data['总计']).tolist()
        nums=np.array(data['数量']).tolist()
        price=0
        num=0
        for i in range(len(prices)):
            price+=int(prices[i][0:-1])
            num+=int(nums[i][0:-1])
        return price,num
    
    #格式化订单信息
    def message(self):
        data=pd.read_csv('临时订单.csv')
        orderNo=data['订单编号'][0]
        message=''
        message+="{:^30}\n".format(orderNo)
        for i in np.array(data[['菜名','数量','总计']]).tolist():
            n=len(i[0])
            n=n-4
            n=15-n
            message+=("{:<"+str(n)+"}{:8}{:8}\n").format(i[0],i[1],i[2])
        
        price,num=self.get_temporary_Price_and_num()
        message+="{:<17}{:8}{:8}".format('总计',str(num)+'份',str(price)+'元')
        return message
    
    #临时订单支付后插入订单
    def insert_Order(self):
        data1=pd.read_csv('临时订单.csv')
        data2=pd.read_csv('订单.csv')
        data=data2.append(data1,ignore_index=True)
        data.to_csv('订单.csv',index=0)
        self.clear_temporary()
        
        
#面向对象用法，一些测试函数功能是否有用的语句
if __name__=='__main__':  
    data=pd.read_csv('用户.csv')
    C=Operate()
    a=C.message()
    print(a)
    