# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'select.ui'
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


class Ui_have_select(QDialog):
    def setupUi(self, have_select):
        have_select.setObjectName("have_select")
        have_select.resize(559, 359)
        self.verticalLayout = QtWidgets.QVBoxLayout(have_select)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableView = QtWidgets.QTableView(have_select)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.pushButton = QtWidgets.QPushButton(have_select)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(have_select)
        QtCore.QMetaObject.connectSlotsByName(have_select)
        self.setTableView()
        
    def setTableView(self):
        self.db=QSqlDatabase.addDatabase('QMYSQL')
        self.db.setHostName('localhost')
        self.db.setDatabaseName('xinxi')
        self.db.setUserName('yxg')
        self.db.setPassword('yxg579521..')
        self.db.open()
        self.queryModel=QSqlQueryModel(self)
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
    
    
    
    def retranslateUi(self, have_select):
        _translate = QtCore.QCoreApplication.translate
        have_select.setWindowTitle(_translate("have_select", "已选界面"))
        self.pushButton.setText(_translate("have_select", "ok"))


