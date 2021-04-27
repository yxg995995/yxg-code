import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtWidgets import *
from Ui_login import Ui_Login
from Ui_register import Ui_Register
from CSV import Operate
import random
import time
import pandas as pd
from Ui_order import Ui_order
from Ui_type import Ui_Type
from Ui_menu import Ui_menu
from Ui_fun import Ui_my_order
from Ui_check import Ui_Check
from Ui_pay import Ui_Pay

from Ui_Admin import Ui_Admin
from Ui_admin_register import Ui_Admin_register

#用户登陆界面 继承主窗口QMainWindow
class Login_window(QMainWindow):
    def __init__(self,parent=None):
        super(Login_window, self).__init__(parent)
        #调用登陆程序
        self.login=Ui_Login()
        self.login.setupUi(self)
        #调用CSV程序
        self.csv=Operate()
        #清除临时订单数据，防止因异常退出导致出错
        self.csv.clear_temporary()
        #按钮绑定事件
        #注册按钮绑定前往注册函数
        self.login.to_register.clicked.connect(self.register_show)
        #登陆按钮绑定登陆函数
        self.login.login_btn.clicked.connect(self.ui_show)
        #管理员登入事件
        self.login.login_admin.clicked.connect(self.admin_show)
        #管理员注册
        self.login.register_amin.clicked.connect(self.register_admin)
    
            
    def ui_show(self):
        #获取当前输入的用户名
        username=self.login.user.text()
        #获取当前输入的密码
        password=self.login.password.text()
        #验证用户和密码
        if self.csv.verify_user(username, password):
            #True 关闭登陆界面 进入选择功能界面
            self.close()
            #username用于传递当前登陆的用户
            self.ui=Type(username)
            self.ui.show()
        #验证失败 弹出错误对话框
        else:
            reply=QMessageBox.information(self,'错误','账号或者密码错误，请重新输入')     
            
    def register_show(self):
        #关闭当前窗口
        self.close()
        #新创建窗口
        self.register=Register_window()
        #展示窗口
        self.register.show()    

    def admin_show(self):
        username=self.login.Admin.text()
        password=self.login.admin_password.text()
        
        if self.csv.verify_Admin(username, password):
            self.close()
            self.admin=Admin()
            self.admin.show()
        else:
            reply=QMessageBox.information(self,'错误','账号或者密码错误，请重新输入')
            
    def register_admin(self):
        self.close()
        self.register=Register_Admin()
        self.register.show()
    



#注册界面
class Register_window(QMainWindow):
    #同登录界面一样
    def __init__(self):
        super(Register_window, self).__init__()
        self.csv=Operate()
        self.register=Ui_Register()
        self.register.setupUi(self)
        #绑定注册成功事件
        self.register.register_ok.clicked.connect(self.userJoin)
        #退回登录界面
        self.register.cancle.clicked.connect(self.to_login)
    
    #注册
    def userJoin(self):
        #当前输入的用户名
        username=self.register.userName.text()     
        #当前输入的密码
        password=self.register.password.text()
        #当前确认的密码
        cp=self.register.cp.text()
        #判断用户名是否已经被注册
        if self.csv.find_user(username):
            reply=QMessageBox.information(self,'错误','用户已存在')
            self.register.userName.clear()
        else:
            #密码小于8位报错
            if len(password)<8:
                self.register.password.clear()
                reply=QMessageBox.information(self,'错误','密码小于8位，请重新输入')
            #密码纯字母或数字报错
            elif password.isdigit() or password.isalpha():
                self.register.password.clear() 
                reply=QMessageBox.information(self,'错误','密码不能是纯数字或者字母')    
            #两次输入密码不一致报错
            elif cp!=password:
                self.register.cp.clear()
                reply=QMessageBox.information(self,'错误','两次输入的密码不一致')
            #注册成功
            else:
                reply=QMessageBox.information(self,'恭喜','注册成功')
                #插入新用户
                self.csv.insert_user(username, password)
                self.login=Login_window()
                #设置登录界面的用户名和密码
                self.login.login.user.setText(username)
                self.login.login.password.setText(password)
                self.close()
                self.login.show()

    def to_login(self):
        self.login=Login_window()
        self.close()
        self.login.show()


#后台管理界面
class Admin(QMainWindow):
    def __init__(self):
        super(Admin, self).__init__()   
        self.admin=Ui_Admin()
        self.admin.setupUi(self)
        self.admin.menu_btn.clicked.connect(self.showM)
        self.admin.user_btn.clicked.connect(self.showU)
        self.admin.order_btn.clicked.connect(self.showO)
        self.admin.original.clicked.connect(self.setOriginal)
        self.admin.save.clicked.connect(self.Save)
        self.admin.back.clicked.connect(self.Back)
        self.admin.fresh.clicked.connect(self.Fresh)
        self.status='菜单.csv'
        self.data=pd.read_csv(self.status)
        self.original_data=self.data.copy()
        self.admin.model.setDataFrame(self.data)
        
    def Back(self):
        self.close()
        self.login=Login_window()
        self.login.show()
    
    def Fresh(self):
        self.judge_status()
        self.admin.model.setDataFrame(self.data)        
    
    def Save(self):
        self.data.to_csv(self.status,index=0)
        replay=QMessageBox.information(self,'提示','保存成功')
        
    def setOriginal(self):
        self.admin.model.setDataFrame(self.original_data)
    
    def judge_status(self):
        self.data=pd.read_csv(self.status)
        self.original_data=self.data.copy()

            
    def showM(self):
        self.status='菜单.csv'
        self.judge_status()
        self.admin.model.setDataFrame(self.data)
        
    def showU(self):
        self.status='用户.csv'
        self.judge_status()
        self.admin.model.setDataFrame(self.data)
        
    def showO(self):
        self.status='订单.csv'
        self.judge_status()
        self.admin.model.setDataFrame(self.data)
        

        

class Register_Admin(QWidget):
    def __init__(self):
        super(Register_Admin, self).__init__()   
        self.ui=Ui_Admin_register()
        self.ui.setupUi(self)
        self.csv=Operate()
        self.ui.be_admin.clicked.connect(self.newAdmin)
        self.ui.cancle.clicked.connect(self.back)
    
    def back(self):
        self.login=Login_window()
        self.close()
        self.login.show()        
        
    
    def newAdmin(self):
        #密钥 （高阶功能：随机生成密钥，邮箱发送，再进行验证）
        self.key='abcd'
        #当前输入的管理员ID
        ID=self.ui.adminID.text() 
        #当前输入的密码
        password=self.ui.adminP.text()
        #当前确认的密码
        cp=self.ui.adminCP.text()
        #当前输入的密钥
        key=self.ui.adminK.text()
        #判断用户名是否已经被注册
        if self.csv.find_ID(ID):
            reply=QMessageBox.information(self,'错误','ID已存在')
            self.ui.adminID.clear()
        else:
            #密码小于8位报错
            if len(password)<8:
                self.ui.adminP.clear()
                reply=QMessageBox.information(self,'错误','密码小于8位，请重新输入')
            #密码纯字母或数字报错
            elif password.isdigit() or password.isalpha():
                self.ui.adminP.clear() 
                reply=QMessageBox.information(self,'错误','密码不能是纯数字或者字母')    
            #两次输入密码不一致报错
            elif cp!=password:
                self.ui.adminCP.clear()
                reply=QMessageBox.information(self,'错误','两次输入的密码不一致')
            #注册成功
            elif key!=self.key:
                self.ui.adminK.clear()
                reply=QMessageBox.information(self,'错误','密钥不正确')                
            else:
                reply=QMessageBox.information(self,'恭喜','注册成功')
                #插入新管理员
                self.csv.insert_admin(ID, password)
                self.login=Login_window()
                #设置登录界面的用户名和密码
                self.login.login.Admin.setText(ID)
                self.login.login.admin_password.setText(password)
                self.close()
                self.login.show()        

#选择功能界面
class Type(QMainWindow):
    def __init__(self,username):
        super(Type, self).__init__()
        self.username=username
        self.ui=Ui_Type()
        self.ui.setupUi(self)
        self.ui.look.clicked.connect(self.Look)
        self.ui.order.clicked.connect(self.toOrder)
    
    #前往看菜    
    def Look(self):
        self.close()
        self.ui=MenuTable(self.username)
        self.ui.show()
    
    #前往点餐
    def toOrder(self):
        self.close()
        self.order=Order(self.username)
        self.order.show()

#点餐
class Order(QWidget):
    def __init__(self,username):
        super(Order, self).__init__()
        self.username=username
        self.s='qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM'
        self.csv=Operate()
        self.ui=Ui_order()
        self.ui.setupUi(self)
        #新增订单
        self.ui.add.clicked.connect(self.new)
        #展示订单
        self.ui.show.clicked.connect(self.showOrder)
        #更新订单
        self.ui.update.clicked.connect(self.update)
        #确认订单
        self.ui.confirm.clicked.connect(self.confirm)
        #退出界面
        self.ui.cancle.clicked.connect(self.Quit)
    
    def Quit(self):
        self.close()
        self.login=Login_window()
        self.login.show()
    
        
    #新增订单
    def new(self):
        if not self.csv.judge_empty():
            replay=QMessageBox.information(self,'提示','存在未支付订单，新建订单将会覆盖之前的订单',
                                                    QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
            if replay==QMessageBox.Yes:
                pass
            else:
                return
        #订单编号
        self.orderNo=''
        for i in range(6):
            self.orderNo+=random.choice(self.s)
        #设置变量判断是否继续点餐
        a=False
        #保存数据
        data=[]
        #循环是否点餐
        while a!=True:
            #总计
            Sum=0
            #时间
            t=''
            #获取全部菜名
            items=self.csv.get_Menu_Name()
            #弹出选择对话框
            item,ok=QInputDialog.getItem(self,'选择您要的菜','菜名',items,0,False)
            if ok and item:
                #价格
                price=self.csv.get_price(item)
                #数量
                num,ok=QInputDialog.getInt(self,'选择数量','请输入数量')
                if num>0:
                    if ok:
                        #计算总计
                        Sum=str(price*num)+'元'
                        #时间位当前时间
                        t=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        #添加数据
                        data.append([self.orderNo,self.username,t,item,str(num)+'份',str(price)+'元/份',Sum])
                        #是否继续点餐
                        replay=QMessageBox.information(self,'提示','是否继续点菜',
                                                        QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
                        if replay==QMessageBox.Yes:
                            a=False
                        else:
                            a=True
                    #选择数量退出后判断是否继续点餐
                    else:
                        replay=QMessageBox.information(self,'提示','是否继续点菜',
                                                        QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
                        if replay==QMessageBox.Yes:
                            a=False
                        else:
                            a=True
                else:
                    replay=QMessageBox.information(self,'提示','请输入大于0的整数')
                    replay=QMessageBox.information(self,'提示','是否继续点菜',
                                                  QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
                    if replay==QMessageBox.Yes:
                        a=False
                    else:
                        a=True
            #选菜退出后判断是否继续点餐
            else:
                replay=QMessageBox.information(self,'提示','是否退出点菜',
                                                    QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
                if replay==QMessageBox.Yes:
                    a=True
                else:
                    a=True
        #判断是否点了菜
        if data!=[]:
            #有的话就将数据插入临时表
            self.csv.insert_temporary(data)
            #设置更新和展示按钮可用
            self.ui.show.setEnabled(True)
            self.ui.update.setEnabled(True)
            self.ui.confirm.setEnabled(True)
        
    #展示我的订单
    def showOrder(self):
        self.my_order=My_order(self.username)
        self.my_order.show()
        #如果清空 设置更新和展示按钮不可用
        if self.my_order.close:
            if self.csv.judge_empty():
                self.ui.show.setEnabled(False)
                self.ui.update.setEnabled(False)
                self.ui.confirm.setEnabled(False)
            
    #更新订单
    def update(self):
        a=False
        #保存数据
        data=[]
        #循环是否点餐
        while a!=True:
            #获取已订的全部菜名
            items=self.csv.get_temporary_Name()
            item,ok=QInputDialog.getItem(self,'选择您要更改的菜','菜名',items,0,False)
            #选择更换
            if ok and item:
                #所有菜名
                menus=self.csv.get_Menu_Name()
                #进行更换选择
                menu,ok=QInputDialog.getItem(self,'选择您要的菜','菜名',menus,0,False)
                if ok and menu:
                    price=self.csv.get_price(menu)
                    num,ok=QInputDialog.getInt(self,'选择数量','请输入数量')
                    if ok:
                        self.csv.delete_temporary(item)
                        Sum=str(price*num)+'元'
                        t=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        self.csv.update_temporary([[self.orderNo,self.username,t,menu,
                                                   str(num)+'份',str(price)+'元/份',Sum]])
                        #是否继续换菜
                        replay=QMessageBox.information(self,'提示','是否继续换菜',
                                                        QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
                        if replay==QMessageBox.Yes:
                            a=False
                        else:
                            a=True
                    else:
                        replay=QMessageBox.information(self,'提示','是否继续换菜',
                                                        QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
                        if replay==QMessageBox.Yes:
                            a=False
                        else:
                            a=True
            else:
                replay=QMessageBox.information(self,'提示','是否退出换菜',
                                                    QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
                if replay==QMessageBox.Yes:
                    a=True
                else:
                    a=True
                    
    #确认订单
    def confirm(self):
        self.close()
        self.check=Check(self.username)
        self.check.show()
        

#我的订单界面
class My_order(QDialog):
    def __init__(self,username):
        super(My_order, self).__init__()
        self.username=username
        self.ui=Ui_my_order()
        self.csv=Operate()
        self.ui.setupUi(self)
        self.ui.clear.clicked.connect(self.Clear)
        self.ui.ok.clicked.connect(self.close)
        self.ui.add.clicked.connect(self.Add)
        self.ui.delete.clicked.connect(self.Delete)
    
    #清空临时订单
    def Clear(self):
        replay=QMessageBox.warning(self,'警告','确定清空吗？',
                QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
        if replay==QMessageBox.Yes:
           self.csv.clear_temporary()
           self.ui.setTableView()
    
    def Add(self):
        self.orderNo=self.csv.get_temporary_No()
        Sum=0
        #时间
        t=''
        #获取全部菜名
        items=self.csv.get_Menu_Name()
        #弹出选择对话框
        item,ok=QInputDialog.getItem(self,'选择您要的菜','菜名',items,0,False)
        if ok and item:
            #价格
            price=self.csv.get_price(item)
            #数量
            num,ok=QInputDialog.getInt(self,'选择数量','请输入数量')
            if ok:
                #计算总计
                Sum=str(price*num)+'元'
                #时间位当前时间
                t=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                #添加数据
                self.csv.update_temporary([[self.orderNo,self.username,t,item,
                                                   str(num)+'份',str(price)+'元/份',Sum]])
                replay=QMessageBox.information(self,'提示','添加成功')
                self.ui.setTableView()
        
    def Delete(self):
        items=self.csv.get_temporary_Name()
        #弹出选择对话框
        item,ok=QInputDialog.getItem(self,'选择您要的菜','菜名',items,0,False)
        if ok and item:
            self.csv.delete_temporary(item)
            replay=QMessageBox.information(self,'提示','删除成功')
            self.ui.setTableView()

#看菜界面
class MenuTable(QWidget):
    def __init__(self,username):
        super(MenuTable, self).__init__()
        self.userName=username
        self.menuList=Ui_menu()
        self.menuList.setupUi(self)
        self.menuList.order.clicked.connect(self.to_Order)
        self.menuList.cancel.clicked.connect(self.close)
    
    #前往点餐
    def to_Order(self):
        self.close()
        self.order=Order(self.userName)
        self.order.show()

#确认支付界面
class Check(QWidget):
    def __init__(self,username):
        super(Check, self).__init__()
        self.username=username
        self.check=Ui_Check()
        self.check.setupUi(self)
        self.csv=Operate()
        #获取订单的数量和总计
        self.price,self.num=self.csv.get_temporary_Price_and_num()
        #展示数量
        self.check.quantity.display(self.num)
        #展示价格
        self.check.SUM.display(self.price)
        #设置字体为黑
        self.check.quantity.setSegmentStyle(QLCDNumber.Filled)
        self.check.SUM.setSegmentStyle(QLCDNumber.Filled)
        self.check.back_menu.clicked.connect(self.back)
        self.check.cancel.clicked.connect(self.Cancel)
        self.check.to_pay.clicked.connect(self.Pay)
    
    #取消订单
    def Cancel(self):
        replay=QMessageBox.warning(self,'警告','取消订单后将会删除现有订单，确定取消订单吗？',
                                   QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
        if replay==QMessageBox.Yes:
            self.csv.clear_temporary()
            replay==QMessageBox.information(self,'提示','取消订单成功,将退回点餐界面')
            self.close()
            self.ui=Order(self.username)
            self.ui.show()
    
    #支付成功跳转
    def Pay(self):
        replay=QMessageBox.information(self,'提示','支付成功')
        self.close()
        self.pay=Pay(self.username)
        self.pay.show()
        
    #再回去看看
    def back(self):
        self.close()
        self.ui=Order(self.username)
        self.ui.ui.show.setEnabled(True)
        self.ui.ui.update.setEnabled(True)
        self.ui.ui.confirm.setEnabled(True)
        self.ui.show()

#支付界面
class Pay(QDialog):
    def __init__(self,username):
        super(Pay, self).__init__()
        self.username=username
        self.csv=Operate()
        self.ui=Ui_Pay()
        self.ui.setupUi(self)
        #订单信息打印
        self.message=self.csv.message()
        self.ui.message.setPlainText(self.message)
        self.csv.insert_Order()
        self.ui.Print.clicked.connect(self.Print)
        self.ui.to_order.clicked.connect(self.backOrder)
        self.ui.byebye.clicked.connect(self.Quit)
    
    #打印信息到控制台
    def Print(self):
        print(self.message)
    
    #继续点餐
    def backOrder(self):
        self.close()
        self.order=Order(self.username)
        self.order.show()
    #退出系统
    def Quit(self):
        self.close()
    

#主程序
class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.login=Login_window()
        self.login.show()
    
#启动程序
if __name__=="__main__":
    app=QApplication(sys.argv)
    win=Main()
    sys.exit(app.exec_())
