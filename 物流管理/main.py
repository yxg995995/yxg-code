import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from Ui_login import Ui_Login
from Ui_register import Ui_Register
from DataBase import DataBase
from Ui_mine import Ui_Mine
from Ui_face import Ui_Face
from Ui_history import Ui_History
from PyQt5.QtSql import QSqlDatabase  , QSqlQueryModel , QSqlQuery
from Ui_uncheck import Ui_Uncheck
from Ui_update import Ui_Update
from Ui_final import Ui_Final

class Login_window(QMainWindow):
    def __init__(self,parent=None):
        super(Login_window, self).__init__(parent)
        #调用登陆程序
        self.login=Ui_Login()
        self.login.setupUi(self)
        self.db=DataBase()
        #注册按钮绑定前往注册函数
        self.login.to_register.clicked.connect(self.register_show)
        #登陆按钮绑定登陆函数
        self.login.login.clicked.connect(self.ui_show)

    def ui_show(self):
        #获取当前输入的用户名
        username=self.login.userID.text()
        #获取当前输入的密码
        password=self.login.password.text()
        #验证用户和密码
        if self.db.Verify(username, password):
            #True 关闭登陆界面 进入选择功能界面
            self.close()
            self.final=Final(username)
            self.final.show()
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

#注册界面
class Register_window(QWidget):
    #同登录界面一样
    def __init__(self):
        super(Register_window, self).__init__()
        self.db=DataBase()
        self.register=Ui_Register()
        self.register.setupUi(self)
        #绑定注册成功事件
        self.register.ok.clicked.connect(self.userJoin)
        #退回登录界面
        self.register.cancel.clicked.connect(self.to_login)
    
    #注册
    def userJoin(self):
        #当前输入的用户名
        username=self.register.username.text()     
        #当前输入的密码
        password=self.register.password.text()
        #当前确认的密码
        cp=self.register.cp.text()
        #手机号
        phone=self.register.phone.text()
        #性别
        sex=self.register.sex.currentText()
        #真实姓名
        trueName=self.register.trueName.text()
        #邮箱
        email=self.register.email.text()
        #地址
        addr=self.register.addr.toPlainText()
        #判断用户名是否已经被注册
        if username=='':
            reply=QMessageBox.information(self,'错误','用户名不能为空')

        elif self.db.find_user(username):
            reply=QMessageBox.information(self,'错误','用户已存在')
            self.register.username.clear()
        elif phone=='':
            reply=QMessageBox.information(self,'错误','电话不能为空')
        elif self.db.find_phone(phone):
            reply=QMessageBox.information(self,'错误','手机号已经注册过了')
            self.register.phone.clear()

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
                userID=self.db.auto_id()
                data=[userID,username,password,phone,sex,trueName,email,addr]
                #插入新用户
                self.db.insertUser(data)
                reply=QMessageBox.information(self,'恭喜','注册成功')
                self.login=Login_window()
                #设置登录界面的用户名和密码
                self.login.login.userID.setText(username)
                self.login.login.password.setText(password)
                self.close()
                self.login.show()

    def to_login(self):
        self.login=Login_window()
        self.close()
        self.login.show()


class Final(QWidget):
    def __init__(self,username):
        super(Final, self).__init__()
        self.ui=Ui_Final()
        self.db=DataBase()
        self.username=username
        self.ui.setupUi(self)  
        self.setbtn()
        self.ui.MyMessage.clicked.connect(self.mine)
        self.ui.update.setEnabled(False)
        self.ui.cancel.setEnabled(False)
        self.ui.update.clicked.connect(self.UP)
        self.ui.cancel.clicked.connect(self.showMessage)
        self.ui.dateTimeEdit.setDateTime(QDateTime.currentDateTime())
        self.ui.car1.clicked.connect(lambda: self.showselect(self.idlist1))
        self.ui.car2.clicked.connect(lambda: self.showselect(self.idlist2))
        self.ui.car3.clicked.connect(lambda: self.showselect(self.idlist3))
        self.ui.car4.clicked.connect(lambda: self.showselect(self.idlist4))
        self.ui.car5.clicked.connect(lambda: self.showselect(self.idlist5))
        self.ui.car6.clicked.connect(lambda: self.showselect(self.idlist6))
        self.ui.car7.clicked.connect(lambda: self.showselect(self.idlist7))
        self.ui.car8.clicked.connect(lambda: self.showselect(self.idlist8))
        self.ui.car9.clicked.connect(lambda: self.showselect(self.idlist9))
        self.init_timer()
        
    def Clear(self):
        self.ui.Class.clear()
        self.ui.location.clear()
        self.ui.hum.clear()
        self.ui.temp.clear()
        self.ui.light.clear()
        self.ui.Click.clear()
    
    def setbtn(self):
        car=self.db.getCar()
        self.idlist1=''
        self.idlist2=''
        self.idlist3=''
        self.idlist4=''
        self.idlist5=''
        self.idlist6=''
        self.idlist7=''
        self.idlist8=''
        self.idlist9=''
        for i in range(len(car)):
            message='司机编号\n'
            message+=car[i][0]+'\n'
            message+='小车编号\n'
            message+=car[i][1]+'\n'
            message+='司机电话\n'
            message+=car[i][2]+'\n'
            message+='订单编号\n'
            if i==0:
                self.idlist1=self.db.get_Car_msg(car[i][1])
            elif i==1:
                self.idlist2=self.db.get_Car_msg(car[i][1])
            elif i==2:
                self.idlist3=self.db.get_Car_msg(car[i][1])
            elif i==3:
                self.idlist4=self.db.get_Car_msg(car[i][1])
            elif i==4:
                self.idlist5=self.db.get_Car_msg(car[i][1])
            elif i==5:
                self.idlist6=self.db.get_Car_msg(car[i][1])
            elif i==6:
                self.idlist7=self.db.get_Car_msg(car[i][1])
            elif i==7:
                self.idlist8=self.db.get_Car_msg(car[i][1])
            elif i==8:
                self.idlist9=self.db.get_Car_msg(car[i][1])
                
            for j in eval('self.idlist'+str(i+1)):
                message+=j+'\n'
            eval('self.ui.car'+str(i+1)+'.setToolTip(message)')
                 
    def showselect(self,IDlist):
        self.Clear()
        item,ok=QInputDialog.getItem(self,'订单编号','选择要查看的订单',IDlist,0,False)
        self.item=item
        if ok and item:
            self.showMessage()
            self.ui.update.setEnabled(True)
            self.ui.cancel.setEnabled(True) 
            
    def showMessage(self):
        self.Clear()
        IS1=['是','否']
        IS2=['是','否']
        loca=self.db.getloc(self.item)
        self.ui.location.addItem(loca)
        data=self.db.get_section(self.item)
        self.ui.Class.addItem(data[0])
        self.ui.hum.setText(str(data[1]))
        self.ui.temp.setText(str(data[2]))
        self.ui.light.addItem(data[3])
        IS1.remove(data[3])
        self.ui.light.addItems(IS1)
        self.ui.Click.addItem(data[4])
        IS2.remove(data[4])
        self.ui.Click.addItems(IS2)
        self.warning()

    def warning(self):
        result=self.db.get_section(self.item)
        if self.db.judge(result[0],result[1],result[2],result[3],result[4]):
            replay=QMessageBox.warning(self.ui.tabWidget_2,'警告','物品状态不正常')

           
    def UP(self):
        d=[eval(self.ui.temp.text()),eval(self.ui.hum.text()),self.ui.light.currentText(),self.item]
        self.db.update_item(d)
        self.showMessage()
        replay=QMessageBox.information(self.ui.tabWidget_2,'提示','更改成功')
        
        
    def mine(self):
        self.close()
        self.m=Mine(self.username)
        self.m.show()
        
    def init_timer(self):
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.start()
        self.timer.timeout.connect(self.update_time)
 
    def update_time(self):
        self.ui.dateTimeEdit.setDateTime(QDateTime.currentDateTime())


#选择界面
class Face(QWidget):
    def __init__(self,username):
        super(Face, self).__init__()
        self.face=Ui_Face()
        self.face.setupUi(self)
        self.username=username
        self.face.Mine_btn.clicked.connect(self.goto_Mine)
        self.face.history_btn.clicked.connect(self.goto_History)
        self.face.UnCheck_btn.clicked.connect(self.goto_UnCheck)
    
    def goto_Mine(self):
        self.close()
        self.mine=Mine(self.username)
        self.mine.show()
    def goto_History(self):
        self.close()
        self.h=History(self.username)
        self.h.show()
    def goto_UnCheck(self):
        self.close()
        self.ui=Final(self.username)
        self.ui.show()

#我的信息界面
class Mine(QWidget):
    def __init__(self,username):
        super(Mine, self).__init__()
        self.username=username
        self.db=DataBase()
        self.mine=Ui_Mine()
        self.mine.setupUi(self)
        self.set_message()
        #绑定修改信息事件
        self.mine.Sure.clicked.connect(self.update)
        #绑定初始事件
        self.mine.fresh.clicked.connect(self.initialize)
        #退回登录界面
        self.mine.exit.clicked.connect(self.Exit)
        
        
    def set_message(self):
        self.message=self.db.get_message(self.username)
        self.mine.msg1.setText(self.message[1])
        self.mine.msg1.setEnabled(False)
        self.mine.msg2.setText(self.message[2])
        self.mine.msg3.setText(self.message[3])
        self.mine.msg4.clear()
        self.mine.msg4.addItem(self.message[4])
        if self.message[4]=='男':
            self.mine.msg4.addItem('女')
        else:
            self.mine.msg4.addItem('男')
        self.mine.msg5.setText(self.message[5])
        self.mine.msg6.setText(self.message[6])
        self.mine.msg7.setPlainText(self.message[-1])
    
    def update(self):
        data=[]
        data.append(self.message[0])
        for i in range(1,7):
            if i !=4:
                data.append(eval('self.mine.msg'+str(i)+'.text()'))
            else:
                data.append(self.mine.msg4.currentText())
        data.append(self.mine.msg7.toPlainText())
        
        if len(data[3])>11:
            reply=QMessageBox.information(self,'错误','手机号不能大于11位')
            self.mine.msg3.setText(self.message[3])
        elif data[3] in self.db.get_otherPhone(self.username):
            reply=QMessageBox.information(self,'错误','手机号已经注册了')
            self.mine.msg3.setText(self.message[3])
        else:
            self.db.update(self.username, data)
            reply=QMessageBox.information(self,'提示','修改成功')
            if self.mine.msg2.text()!=self.message[2]:
                reply=QMessageBox.information(self,'提示','您修改了密码，需要重新登录')
                self.close()
                self.login=Login_window()
                self.login.show()
            else:
                self.set_message()
            
    def initialize(self):
        self.set_message()
        
    def Exit(self):
        self.close()
        self.face=Face(self.username)
        self.face.show()
    

    

class History(QWidget):
    def __init__(self,username):
        super(History, self).__init__()
        self.username=username
        self.h=Ui_History()
        self.h.setupUi(self)
        self.h.search.clicked.connect(self.onSearch)
        self.h.clear.clicked.connect(self.onClear)
        self.h.Quit.clicked.connect(self.back)
        self.setTableView()
        
    def back(self):
        self.close()
        self.face=Face(self.username)
        self.face.show()        
    
    def onClear(self):
        self.setTableView()
    
    def onSearch(self):
        id=self.h.key.text()
        if id=="":
            replay=QMessageBox.information(self,'错误','请不要搜索空值')
        else:
            q="select * from track_system.order where OrderId='"+id+"' and R_name='"+self.username+"'"
            szQuery = (q)
            self.queryModel.setQuery(szQuery)
    
    def setTableView(self):
        self.db=QSqlDatabase.addDatabase('QMYSQL')
        self.db.setHostName('localhost')
        self.db.setDatabaseName('track_system')
        self.db.setUserName('yxg')
        self.db.setPassword('yxg579521..')
        self.db.open()
        self.queryModel=QSqlQueryModel(self.h.widget)
        self.recordQuery(self.username)
        self.h.tableView.setModel(self.queryModel)
        self.queryModel.setHeaderData(0, Qt.Horizontal, "订单号")
        self.queryModel.setHeaderData(1, Qt.Horizontal, "寄件人姓名")
        self.queryModel.setHeaderData(2, Qt.Horizontal, "寄件人地址")
        self.queryModel.setHeaderData(3, Qt.Horizontal, "收件人姓名")
        self.queryModel.setHeaderData(4, Qt.Horizontal, "收件人地址")
        self.queryModel.setHeaderData(5, Qt.Horizontal, "物品类型")
        self.queryModel.setHeaderData(6, Qt.Horizontal, "重量")
        self.queryModel.setHeaderData(7, Qt.Horizontal, "是否易碎")
        self.queryModel.setHeaderData(8, Qt.Horizontal, "状态")
        self.queryModel.setHeaderData(9, Qt.Horizontal, "备注")
         
    def recordQuery(self,username):
        q="select * from track_system.order where R_name='"+self.username+"'"
        szQuery = (q)
        self.queryModel.setQuery(szQuery)        


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
