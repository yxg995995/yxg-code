import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtWidgets import *
from Login import Ui_Login
from Register import Ui_Register
from DataBase import DataBase
from Table import Ui_MainWindow
from PyQt5.QtSql import QSqlDatabase  , QSqlQueryModel , QSqlQuery
from fun import Ui_fun_Dialog
class Login_window(QMainWindow):
    def __init__(self,parent=None):
        super(Login_window, self).__init__(parent) 
        #self.db=DataBase()
        self.login=Ui_Login()
        self.login.setupUi(self)
        self.db=DataBase()
        self.login.register_btn.clicked.connect(self.register_show)
        self.login.login_btn.clicked.connect(self.ui_show)

    def register_show(self):
        self.close()
        self.register=Register_window()
        self.register.show()    
    
    def ui_show(self):
        password=self.login.password.text()
        username=self.login.userName.text()
        if self.db.Verify(username, password):
            self.close()
            self.ui=UI()
            self.ui.show()
        else:
            reply=QMessageBox.information(self,'错误','账号或者密码错误，请重新输入')

class Register_window(QMainWindow):
    def __init__(self):
        super(Register_window, self).__init__()
        self.db=DataBase()
        self.register=Ui_Register()
        self.register.setupUi(self)
        self.register.register_ok.clicked.connect(self.Join)
        self.register.cancle.clicked.connect(self.to_login)
    
    def Join(self):
        username=self.register.userName.text()
        if self.db.find_user(username):
            self.register.user.clear()
            reply=QMessageBox.waring(self,'错误','用户已存在')
        else:
            password=self.register.password.text()
            cp=self.register.cp.text()
            if len(password)<8:
                reply=QMessageBox.waring(self,'错误','密码小于8位，请重新输入')
                self.register.password.clear()
            elif password.isdigit() or password.isalpha():
                reply=QMessageBox.waring(self,'错误','密码不能是纯数字或者字母')
                self.register.password.clear()
            elif cp!=password:
                reply=QMessageBox.waring(self,'错误','两次输入的密码不一致')
                self.register.cp.clear()
            else:
                reply=QMessageBox.information(self,'恭喜','注册成功')
                self.db.insertUser(username,password)
                self.login=Login_window()
                self.login.login.userName.setText(username)
                self.login.login.password.setText(password)
            self.close()
            self.login.show()

    def to_login(self):
        self.login=Login_window()
        self.close()
        self.login.show()



class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.DB=DataBase()
        self.ui.commodity_btn.clicked.connect(self.showC)
        self.ui.employee_btn.clicked.connect(self.showE)
        self.ui.receipt_btn.clicked.connect(self.showR)
        self.ui.detail_btn.clicked.connect(self.showD)
        
        self.ui.pre_btn.clicked.connect(self.Pre)
        self.ui.next_btn.clicked.connect(self.Next)
        self.ui.search_btn.clicked.connect(self.onSearch)
        self.ui.update_btn.clicked.connect(self.onClear)
        self.ui.update_btn.clicked.connect(self.ui.keyword.clear)
        self.queryModel = None
        self.currentPage = 0
        self.totalPage = 0
        self.totalRecrodCount = 0
        self.PageCount = 10
        
        #菜单栏
        self.ui.commodity.triggered[QAction].connect(self.funC)
        self.ui.employee.triggered[QAction].connect(self.funE)
        self.ui.receipt.triggered[QAction].connect(self.funR)
        self.ui.detail.triggered[QAction].connect(self.funD)
        
    def funC(self,q):
        if q.text()=='new':
            self.add=Fun(tablename=self.tablename)
            self.add.CCC()
            self.add.show()
        else:
            items=self.DB.get_name()
            item,ok=QInputDialog.getItem(self,'delete','产品名称',items,0,False)
            if ok and item:
                self.DB.delete_commodity(item)
                reply=QMessageBox.information(self,'提示','删除成功')
        self.showC()
    
    def funE(self,q):
        if q.text()=='new':
            self.add=Fun(tablename=self.tablename)
            self.add.EEE()
            self.add.show()
        else:
            items=self.DB.get_id()
            item,ok=QInputDialog.getItem(self,'delete','职员编号',items,0,False)
            if ok and item:
                self.DB.delete_employee(item)
                reply=QMessageBox.information(self,'提示','删除成功')
        self.showE()
    
    def funR(self,q):
        if q.text()=='new':
            self.add=Fun(tablename=self.tablename)
            self.add.RRR()
            self.add.show()
        else:
            items=self.DB.get_receiptNo()
            item,ok=QInputDialog.getItem(self,'delete','收据单号',items,0,False)
            if ok and item:
                self.DB.delete_receipt(item)
                reply=QMessageBox.information(self,'提示','删除成功')
        self.showR()

    def funD(self,q):
        if q.text()=='new':
            self.add=Fun(tablename=self.tablename)
            self.add.DDD()
            self.add.show()
        else:
            items=self.DB.get_detailNo()
            item,ok=QInputDialog.getItem(self,'delete','收据单号',items,0,False)
            if ok and item:
                self.DB.delete_detail(item)
                reply=QMessageBox.information(self,'提示','删除成功')
        self.showD()        
    
    def onClear(self):
        self.showC()
    
    def onSearch(self):
        feature=self.ui.feature.currentText()
        key="'%"+self.ui.keyword.text()+"%'"
        q="select * from "+self.tablename+" where "+feature+" like %s"
        query=(q%key)
        self.queryModel.setQuery(query)
        self.totalRecrodCount=self.queryModel.rowCount()
        self.currentPage = 1
        self.totalPage=self.getPageCount()
        self.updateStatus()
        
        
    def setTableView(self,tablename):
        self.db=QSqlDatabase.addDatabase('QMYSQL')
        self.db.setHostName('localhost')
        self.db.setDatabaseName('shop')
        self.db.setUserName('yxg')
        self.db.setPassword('yxg579521..')
        self.db.open()
        self.queryModel=QSqlQueryModel(self.ui.widget_2)
        self.currentPage = 1
        self.recordQuery(0,tablename)
        self.ui.tableView.setModel(self.queryModel)
        
    def recordQuery(self,limitIndex,tablename):
        q="select * from "+tablename+" limit %s,%s"
        szQuery = (q%(limitIndex , self.PageCount))
        self.queryModel.setQuery(szQuery)    
    
    def getTotalRecord(self):
        self.queryModel.setQuery("select * from "+self.tablename)
        rowCount = self.queryModel.rowCount()
        return rowCount
    
    def getPageCount(self):
        if self.totalRecrodCount % self.PageCount == 0:
            return(self.totalRecrodCount/self.PageCount)
        else:
            return(int(self.totalRecrodCount/self.PageCount)+1)
        
    def updateStatus(self):
        if self.currentPage== 1 :
            self.ui.pre_btn.setEnabled( False )
            self.ui.next_btn.setEnabled(True)
        else:
            self.ui.pre_btn.setEnabled( True )
            self.ui.next_btn.setEnabled( True )
    
    def showC(self):
        self.ui.feature.clear()
        items=['name','price','product_date','keep_num','expired']
        self.ui.feature.addItems(items)
        self.tablename='commodity'
        self.setTableView(self.tablename)
        self.queryModel.setHeaderData(0, Qt.Horizontal, "商品名称")
        self.queryModel.setHeaderData(1, Qt.Horizontal, "价格")
        self.queryModel.setHeaderData(2, Qt.Horizontal, "生产日期")
        self.queryModel.setHeaderData(3, Qt.Horizontal, "库存量")
        self.queryModel.setHeaderData(4, Qt.Horizontal, "是否过期")
        self.totalRecrodCount=self.getTotalRecord()
        self.totalPage=self.getPageCount()
        self.updateStatus()
        
        
    def showE(self):
        self.ui.feature.clear()
        items=['id','employeeName','sex','phone']
        self.ui.feature.addItems(items)
        self.tablename='employee'
        self.setTableView(self.tablename)
        self.queryModel.setHeaderData(0, Qt.Horizontal, "职员编号")
        self.queryModel.setHeaderData(1, Qt.Horizontal, "姓名")
        self.queryModel.setHeaderData(2, Qt.Horizontal, "性别")
        self.queryModel.setHeaderData(3, Qt.Horizontal, "联系电话")
        self.totalRecrodCount=self.getTotalRecord()
        self.totalPage=self.getPageCount()
        self.updateStatus()
    
    def showR(self):
        self.ui.feature.clear()
        items=['receiptNo','time','employeeName','payment','pay_type']
        self.ui.feature.addItems(items)
        self.tablename='receipt'
        self.setTableView(self.tablename)
        self.queryModel.setHeaderData(0, Qt.Horizontal, "收据单号")
        self.queryModel.setHeaderData(1, Qt.Horizontal, "时间")
        self.queryModel.setHeaderData(2, Qt.Horizontal, "办理职员")
        self.queryModel.setHeaderData(3, Qt.Horizontal, "总付款额")
        self.queryModel.setHeaderData(4, Qt.Horizontal, "支付方式")
        self.totalRecrodCount=self.getTotalRecord()
        self.totalPage=self.getPageCount()
        self.updateStatus()
        
    def showD(self):
        self.ui.feature.clear()
        items=['receiptNo','name','quantity','money']
        self.ui.feature.addItems(items)
        self.tablename='detail'
        self.setTableView(self.tablename)
        self.queryModel.setHeaderData(0, Qt.Horizontal, "收据单号")
        self.queryModel.setHeaderData(1, Qt.Horizontal, "商品名称")
        self.queryModel.setHeaderData(2, Qt.Horizontal, "数量")
        self.queryModel.setHeaderData(3, Qt.Horizontal, "付款额")
        self.totalRecrodCount=self.getTotalRecord()
        self.totalPage=self.getPageCount()
        self.updateStatus()
    
    def Pre(self):
        limitIndex=(self.currentPage-2)*self.PageCount
        self.recordQuery(limitIndex,self.tablename)
        self.currentPage-=1
        self.updateStatus()
        
    def Next(self):
        if self.totalPage==1:
            QMessageBox.information(self.ui.widget_2, "提示", "已经是最后一页了" )
            self.ui.next_btn.setEnabled(False)
            return
        if self.currentPage==self.totalPage:
            QMessageBox.information(self.ui.widget_2, "提示", "已经是最后一页了" )
            self.ui.next_btn.setEnabled(False)
            return
        limitIndex=self.currentPage*self.PageCount
        self.recordQuery(limitIndex,self.tablename)
        self.currentPage+=1
        self.updateStatus()

        
class Fun(QDialog):
    def __init__(self,tablename=None):
        super(Fun, self).__init__()
        self.db=DataBase()
        self.tablename=tablename
        self.fun=Ui_fun_Dialog()
        self.fun.setupUi(self)
        self.fun.cancle_btn.clicked.connect(self.close)
        self.fun.add_btn.clicked.connect(self.add)
    
    def add(self):
        data=[]
        input1=self.fun.input1.text()
        input2=self.fun.input2.text()
        input3=self.fun.input3.text()
        input4=self.fun.input4.text()
        input5=self.fun.input5.text()
        data=[input1,input2,input3,input4,input5]
        data=data[:self.n]
        self.db.insert(self.tablename, data)
        reply=QMessageBox.information(self,'提示','添加成功')
        self.close()
        
    def CCC(self):
        self.n=5
        self.fun.attr1.setText('商品名称')
        self.fun.attr2.setText('价格')
        self.fun.attr3.setText('生产日期')
        self.fun.attr4.setText('库存数量')
        self.fun.attr5.setText('是否过期')
        
    def EEE(self):
        self.n=4
        self.fun.attr1.setText('职员编号')
        self.fun.attr2.setText('职员姓名')
        self.fun.attr3.setText('性别')
        self.fun.attr4.setText('联系电话')
        self.fun.attr5.setText('')
        
    def RRR(self):
        self.n=5
        self.fun.attr1.setText('收据单号')
        self.fun.attr2.setText('时间')
        self.fun.attr3.setText('职员姓名')
        self.fun.attr4.setText('总收款')
        self.fun.attr5.setText('支付方式')
        
    def DDD(self):
        self.n=4
        self.fun.attr1.setText('收据单号')
        self.fun.attr2.setText('商品名称')
        self.fun.attr3.setText('购买数量')
        self.fun.attr4.setText('应收金额')
        self.fun.attr5.setText('')
    
    
class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.login=Login_window()
        self.login.show()
    

if __name__=="__main__":
    app=QApplication(sys.argv)
    win=Main()
    sys.exit(app.exec_())