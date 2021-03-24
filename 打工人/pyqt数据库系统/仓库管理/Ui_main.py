import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtWidgets import *
from Ui_login import Ui_Login
from Ui_register import Ui_Register
from DataBase import DataBase
from Ui_tablelist import Ui_TableList
from Ui_products import Ui_MainWindow
from Ui_add import Ui_add_Dialog
from Ui_inOrder import Ui_in_orderWindow
from Ui_inDetail import Ui_in_detailWindow
from Ui_outOrder import Ui_out_orderWindow
from Ui_outDetail import Ui_out_detailWindow
from CZ import Ui_cz_Dialog

class Login(QMainWindow):
    def __init__(self,parent=None):
        super(Login, self).__init__(parent) 
        self.db=DataBase()
        self.login=Ui_Login()
        self.login.setupUi(self)
        self.login.to_register.clicked.connect(self.register_show)
        self.login.login.clicked.connect(self.ui_show)

    def register_show(self):
        self.close()
        self.register=Register()
        self.register.show()    
    
    def ui_show(self):
        password=self.login.password.text()
        username=self.login.user.text()
        if self.db.verify_pass(username, password):
            self.close()
            self.ui=Table()
            self.ui.show()
        else:
            reply=QMessageBox.information(self,'错误','账号或者密码错误，请重新输入')
        
        
class Register(QMainWindow):
    def __init__(self):
        super(Register, self).__init__()
        self.db=DataBase()
        self.register=Ui_Register()
        self.register.setupUi(self)
        self.register.register_2.clicked.connect(self.Join)
        self.register.cancle.clicked.connect(self.back)
    
    def Join(self):
        username=self.register.user.text()
        if self.db.find_user(username):
            self.register.user.clear()
            self.register.user_error.setVisible(1)
        else:
            password=self.register.password.text()
            repassword=self.register.repassword.text()
            if len(password)<8:
                self.register.password_tip.setText('密码小于8位，请重新输入')
                self.register.password.clear()
            elif password.isdigit() or password.isalpha():
                self.register.password_tip.setText('密码不能是纯数字或者字母')
                self.register.password.clear()
            elif repassword!=password:
                self.register.repassword_tip.setVisible(1)
                self.register.repassword.clear()
            else:
                reply=QMessageBox.information(self,'恭喜','注册成功')
                self.db.insertUser(username,password)
                self.login=Login()
                self.login.login.user.setText(username)
                self.login.login.password.setText(password)
            self.close()
            self.login.show()

    def back(self):
        self.login=Login()
        self.close()
        self.login.show()
        
class Table(QMainWindow):
    def __init__(self):
        super(Table, self).__init__()
        self.ui=Ui_TableList()
        self.ui.setupUi(self)
        self.ui.product_btn.clicked.connect(self.product)
        self.ui.info_btn.clicked.connect(self.inorder)
        self.ui.info_detailBtn.clicked.connect(self.indetail)
        self.ui.out_btn.clicked.connect(self.outorder)
        self.ui.out_detailBtn.clicked.connect(self.outdetail)
        
    def product(self):
        self.product=Product()
        self.product.show()
    def inorder(self):
        self.inorder=In_Order()
        self.inorder.show()
    def indetail(self):
        self.indetail=In_Detail()
        self.indetail.show()
    def outdetail(self):
        self.outdetail=Out_Detail()
        self.outdetail.show()
    def outorder(self):
        self.outorder=Out_Order()
        self.outorder.show()

class Product(QMainWindow):
    def __init__(self):
        super(Product, self).__init__()
        self.product=Ui_MainWindow()
        self.db=DataBase()
        self.product.setupUi(self)
        self.product.menu.triggered[QAction].connect(self.fun)
    
    def fun(self,q):
        if q.text()=='add':
            self.add=Add()
            self.add.show()
        elif q.text()=='delete':
            items=self.db.get_id()
            item,ok=QInputDialog.getItem(self,'delete','产品编号',items,0,False)
            if ok and item:
                self.db.delete(int(item))
        else:
            items=self.db.get_id()
            item,ok=QInputDialog.getItem(self,'更新','产品编号',items,0,False)
            if ok and item:
                self.add=Add(int(item))
                self.add.pre_upadte()
                self.add.show()
        self.product.setTableView()
    
        
class In_Order(QMainWindow):
    def __init__(self):
        super(In_Order, self).__init__()
        self.inOrder=Ui_in_orderWindow()
        self.db=DataBase()
        self.inOrder.setupUi(self)
        self.inOrder.menu.triggered[QAction].connect(self.fun)
    
    def fun(self,q):
        if q.text()=='add':
            self.add=CZ_dialog(tablename='info_order')
            self.add.IO()
            self.add.show()
        else:
            items=self.db.get_IO()
            item,ok=QInputDialog.getItem(self,'delete','出库单号',items,0,False)
            if ok and item:
                self.db.delete_IO(item)
        self.inOrder.setTableView()

class In_Detail(QMainWindow):
    def __init__(self):
        super(In_Detail, self).__init__()
        self.inDetail=Ui_in_detailWindow()
        self.db=DataBase()
        self.inDetail.setupUi(self)
        self.inDetail.menu.triggered[QAction].connect(self.fun)
    
    def fun(self,q):
        if q.text()=='add':
            self.add=CZ_dialog(tablename='info_detail')
            self.add.ID()
            self.add.show()
        else:
            items=self.db.get_ID()
            item,ok=QInputDialog.getItem(self,'delete','出库单号',items,0,False)
            if ok and item:
                self.db.delete_ID(item)
        self.inDetail.setTableView()

class Out_Order(QMainWindow):
    def __init__(self):
        super(Out_Order, self).__init__()
        self.OutOrder=Ui_out_orderWindow()
        self.db=DataBase()
        self.OutOrder.setupUi(self)
        self.OutOrder.menu.triggered[QAction].connect(self.fun)
    
    def fun(self,q):
        if q.text()=='add':
            self.add=CZ_dialog(tablename='out_order')
            self.add.OO()
            self.add.show()
        else:
            items=self.db.get_OO()
            item,ok=QInputDialog.getItem(self,'delete','出库单号',items,0,False)
            if ok and item:
                self.db.delete_OO(item)
        self.OutOrder.setTableView()
        
class Out_Detail(QMainWindow):
    def __init__(self):
        super(Out_Detail, self).__init__()
        self.OutDetail=Ui_out_detailWindow()
        self.db=DataBase()
        self.OutDetail.setupUi(self)
        self.OutDetail.menu.triggered[QAction].connect(self.fun)
    
    def fun(self,q):
        if q.text()=='add':
            self.add=CZ_dialog(tablename='out_detail')
            self.add.OD()
            self.add.show()
        else:
            items=self.db.get_OD()
            item,ok=QInputDialog.getItem(self,'delete','出库单号',items,0,False)
            if ok and item:
                self.db.delete_OD(item)
        self.OutDetail.setTableView()       
class Add(QDialog):
    def __init__(self,item=None):
        super(Add, self).__init__()
        self.db=DataBase()
        self.item=item
        self.add=Ui_add_Dialog()
        self.add.setupUi(self)
        self.add.cancle_btn.clicked.connect(self.close)
        self.add.add_btn.clicked.connect(self.new)
        self.add.update_btn.setEnabled(False)
        self.add.update_btn.clicked.connect(self.update)
    
    def new(self):
        self.add.update_btn.setEnabled(False)
        data=[]
        name=self.add.name.text()
        data.append(name)
        in_price=self.add.info_price.text()
        data.append(eval(in_price))
        product_type=self.add.type.text()
        data.append(product_type)
        brand=self.add.brand.text()
        data.append(brand)
        out_price=self.add.out_price.text()
        data.append(eval(out_price))
        number=self.add.number.text()
        data.append(eval(number))
        self.db.info_product(data)
        reply=QMessageBox.information(self,'提示','添加成功')
        self.close()
    
    def pre_upadte(self):
        self.add.update_btn.setEnabled(True)
        self.add.add_btn.setEnabled(False)
        result=self.db.get_product(self.item)
        self.add.name.setText(result[1])
        self.add.info_price.setText(result[2])
        self.add.type.setText(result[3])
        self.add.brand.setText(result[4])
        self.add.out_price.setText(result[5])
        self.add.number.setText(str(result[6]))
    
    def update(self):
        data=[]
        name=self.add.name.text()
        data.append(name)
        in_price=self.add.info_price.text()
        data.append(eval(in_price))
        product_type=self.add.type.text()
        data.append(product_type)
        brand=self.add.brand.text()
        data.append(brand)
        out_price=self.add.out_price.text()
        data.append(eval(out_price))
        number=self.add.number.text()
        data.append(eval(number))
        data.append(self.item)
        self.db.update(data)
        reply=QMessageBox.information(self,'提示','更新成功')
        self.close()


class CZ_dialog(QDialog):
    def __init__(self,tablename=None):
        super(CZ_dialog, self).__init__()
        self.db=DataBase()
        self.tablename=tablename
        self.cz=Ui_cz_Dialog()
        self.cz.setupUi(self)
        self.cz.cancle_btn.clicked.connect(self.close)
        self.cz.add_btn.clicked.connect(self.add)
    
    def add(self):
        data=[]
        input1=self.cz.input1.text()
        input2=self.cz.input2.text()
        input3=self.cz.input3.text()
        input4=self.cz.input4.text()
        data=[input1,input2,input3,input4]
        self.db.insert(self.tablename, data)
        reply=QMessageBox.information(self,'提示','添加成功')
        self.close()
        
    def IO(self):
        self.cz.attr1.setText('入库单号')
        self.cz.attr2.setText('入库时间')
        self.cz.attr3.setText('经办人')
        self.cz.attr4.setText('联系电话')
    
    def ID(self):
        self.cz.attr1.setText('入库单号')
        self.cz.attr2.setText('商品编号')
        self.cz.attr3.setText('数量')
        self.cz.attr4.setText('成本')

        
    def OO(self):
        self.cz.attr1.setText('出库单号')
        self.cz.attr2.setText('出库时间')
        self.cz.attr3.setText('经办人')
        self.cz.attr4.setText('联系电话')

        
    def OD(self):
        self.cz.attr1.setText('出库单号')
        self.cz.attr2.setText('商品编号')
        self.cz.attr3.setText('数量')
        self.cz.attr4.setText('出售额')

        


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.db=DataBase()
        self.login=Login()
        self.login.show()
    

if __name__=="__main__":
    app=QApplication(sys.argv)
    win=Main()
    sys.exit(app.exec_())
        
        

