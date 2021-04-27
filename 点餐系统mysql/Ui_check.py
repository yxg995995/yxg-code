# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Check.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import QSqlDatabase  , QSqlQueryModel , QSqlQuery
class Ui_Check(QWidget):
    def setupUi(self, Check):
        Check.setObjectName("Check")
        Check.resize(547, 387)
        Check.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(Check)
        self.label.setGeometry(QtCore.QRect(20, 10, 70, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.back_menu = QtWidgets.QPushButton(Check)
        self.back_menu.setGeometry(QtCore.QRect(450, 10, 70, 30))
        self.back_menu.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.back_menu.setObjectName("back_menu")
        self.tableView = QtWidgets.QTableView(Check)
        self.tableView.setGeometry(QtCore.QRect(10, 50, 531, 271))
        self.tableView.setObjectName("tableView")
        self.to_pay = QtWidgets.QPushButton(Check)
        self.to_pay.setGeometry(QtCore.QRect(460, 350, 75, 23))
        self.to_pay.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.to_pay.setObjectName("to_pay")
        self.layoutWidget = QtWidgets.QWidget(Check)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 350, 232, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.quantity = QtWidgets.QLCDNumber(self.layoutWidget)
        self.quantity.setObjectName("quantity")
        self.horizontalLayout.addWidget(self.quantity)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.SUM = QtWidgets.QLCDNumber(self.layoutWidget)
        self.SUM.setObjectName("SUM")
        self.horizontalLayout.addWidget(self.SUM)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)

        self.retranslateUi(Check)
        QtCore.QMetaObject.connectSlotsByName(Check)
        self.setTableView()
        
    def setTableView(self):
        self.db=QSqlDatabase.addDatabase('QMYSQL')
        self.db.setHostName('localhost')
        self.db.setDatabaseName('xinxi')
        self.db.setUserName('yxg')
        self.db.setPassword('yxg579521..')
        self.db.open()
        self.queryModel=QSqlQueryModel(self)
        self.currentPage = 1
        self.recordQuery()
        self.tableView.setModel(self.queryModel)
        self.queryModel.setHeaderData(0, Qt.Horizontal, "商品名称")
        self.queryModel.setHeaderData(1, Qt.Horizontal, "数量")
        self.queryModel.setHeaderData(2, Qt.Horizontal, "价格")
        self.queryModel.setHeaderData(3, Qt.Horizontal, "总计")
        
    def recordQuery(self):
        q="select * from xinxi.order"
        szQuery = (q)
        self.queryModel.setQuery(szQuery)
        
    def retranslateUi(self, Check):
        _translate = QtCore.QCoreApplication.translate
        Check.setWindowTitle(_translate("Check", "已选菜品界面"))
        self.label.setText(_translate("Check", "已购餐品"))
        self.back_menu.setText(_translate("Check", "我再看看"))
        self.to_pay.setText(_translate("Check", "去支付"))
        self.label_3.setText(_translate("Check", "总计："))
        self.label_4.setText(_translate("Check", "件"))
        self.label_5.setText(_translate("Check", "共"))
        self.label_6.setText(_translate("Check", "元"))
import sys
if __name__=='__main__':
    app=QtWidgets.QApplication(sys.argv)
    win=Ui_Check()
    menu=QtWidgets.QWidget()
    win.setupUi(menu)
    menu.show()
    sys.exit(app.exec_())

