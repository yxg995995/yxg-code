# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'end.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import QSqlDatabase  , QSqlQueryModel , QSqlQuery


class Ui_my_Order(QWidget):
    def setupUi(self, my_Order):
        my_Order.setObjectName("my_Order")
        my_Order.resize(524, 442)
        self.tableView = QtWidgets.QTableView(my_Order)
        self.tableView.setGeometry(QtCore.QRect(10, 50, 501, 331))
        self.tableView.setObjectName("tableView")
        self.label = QtWidgets.QLabel(my_Order)
        self.label.setGeometry(QtCore.QRect(20, 20, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.backmenu = QtWidgets.QPushButton(my_Order)
        self.backmenu.setGeometry(QtCore.QRect(440, 20, 75, 23))
        self.backmenu.setObjectName("backmenu")
        self.print = QtWidgets.QPushButton(my_Order)
        self.print.setGeometry(QtCore.QRect(210, 400, 75, 23))
        self.print.setObjectName("print")

        self.retranslateUi(my_Order)
        QtCore.QMetaObject.connectSlotsByName(my_Order)
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

    def retranslateUi(self, my_Order):
        _translate = QtCore.QCoreApplication.translate
        my_Order.setWindowTitle(_translate("my_Order", "订单界面"))
        self.label.setText(_translate("my_Order", "您的订单："))
        self.backmenu.setText(_translate("my_Order", "回去看看"))
        self.print.setText(_translate("my_Order", "打印"))


