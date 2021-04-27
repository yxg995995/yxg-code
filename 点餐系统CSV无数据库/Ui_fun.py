# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fun.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtWidgets import *
import pandas as pd
import numpy as np

#我的订单界面
class Ui_my_order(object):
    def setupUi(self, my_order):
        my_order.setObjectName("my_order")
        my_order.resize(571, 301)
        self.verticalLayout = QtWidgets.QVBoxLayout(my_order)
        self.verticalLayout.setObjectName("verticalLayout")
        self.orderView = QtWidgets.QTableView(my_order)
        self.orderView.setObjectName("orderView")
        self.verticalLayout.addWidget(self.orderView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ok = QtWidgets.QPushButton(my_order)
        self.ok.setObjectName("ok")
        self.horizontalLayout.addWidget(self.ok)
        self.add = QtWidgets.QPushButton(my_order)
        self.add.setObjectName("add")
        self.horizontalLayout.addWidget(self.add)       
        self.delete = QtWidgets.QPushButton(my_order)
        self.delete.setObjectName("delete")
        self.horizontalLayout.addWidget(self.delete)   
        self.clear = QtWidgets.QPushButton(my_order)
        self.clear.setObjectName("clear")
        self.horizontalLayout.addWidget(self.clear)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.orderView.horizontalHeader().setStretchLastSection(True)
        self.orderView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.retranslateUi(my_order)
        QtCore.QMetaObject.connectSlotsByName(my_order)
        self.setTableView()
    
    #设置表格信息
    def setTableView(self):
        data=pd.read_csv('临时订单.csv')
        rows=len(data)
        columns=len(data.columns)
        self.model=QStandardItemModel(rows,columns)
        self.model.setHorizontalHeaderLabels(['订单编号','订单人','时间','菜名','数量','价格','总计'])
        for row in range(rows):
            for column in range(columns):
                item=QStandardItem(np.array(data)[row][column])
                self.model.setItem(row,column,item)
        self.orderView.setModel(self.model)   
        
    def retranslateUi(self, my_order):
        _translate = QtCore.QCoreApplication.translate
        my_order.setWindowTitle(_translate("my_order", "我的订单"))
        self.ok.setText(_translate("my_order", "确定"))
        self.add.setText(_translate("my_order", "新增"))
        self.delete.setText(_translate("my_order", "删除"))
        self.clear.setText(_translate("my_order", "清空"))


