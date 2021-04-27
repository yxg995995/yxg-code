# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Order.ui'
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

#点餐界面
class Ui_order(QWidget):
    def setupUi(self, order):
        order.setObjectName("order")
        order.resize(524, 468)
        self.verticalLayout = QtWidgets.QVBoxLayout(order)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add = QtWidgets.QPushButton(order)
        self.add.setObjectName("add")
        self.horizontalLayout.addWidget(self.add)
        self.show = QtWidgets.QPushButton(order)
        self.show.setObjectName("show")
        self.horizontalLayout.addWidget(self.show)
        self.update = QtWidgets.QPushButton(order)
        self.update.setObjectName("update")
        self.horizontalLayout.addWidget(self.update)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.widget = QtWidgets.QWidget(order)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(23)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.tableView = QtWidgets.QTableView(self.widget)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_2.addWidget(self.tableView)
        self.verticalLayout.addWidget(self.widget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.confirm = QtWidgets.QPushButton(order)
        self.confirm.setObjectName("confirm")
        self.horizontalLayout_2.addWidget(self.confirm)
        self.cancle = QtWidgets.QPushButton(order)
        self.cancle.setObjectName("cancle")
        self.horizontalLayout_2.addWidget(self.cancle)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.retranslateUi(order)
        
        self.cancle.clicked.connect(self.close)
        QtCore.QMetaObject.connectSlotsByName(order)
        #展示菜单信息
        self.setTableView()
        #设置更新和展示按钮不可点击
        self.show.setEnabled(False)
        self.update.setEnabled(False)
        self.confirm.setEnabled(False)
        
    def setTableView(self):
        data=pd.read_csv('菜单.csv')
        #行
        rows=len(data)
        #列
        columns=len(data.columns)
        #表格储存任意数据
        self.model=QStandardItemModel(rows,columns)
        #设置头部信息
        self.model.setHorizontalHeaderLabels(['菜名','价格'])
        for row in range(rows):
            for column in range(columns):
                #转换为数组
                item=QStandardItem(np.array(data)[row][column])
                self.model.setItem(row,column,item)
        #设置表格
        self.tableView.setModel(self.model)        
    def retranslateUi(self, order):
        _translate = QtCore.QCoreApplication.translate
        order.setWindowTitle(_translate("order", "点餐界面"))
        self.add.setText(_translate("order", "新建订单"))
        self.show.setText(_translate("order", "显示订单"))
        self.update.setText(_translate("order", "更改订单"))
        self.label.setText(_translate("order", "菜单"))
        self.confirm.setText(_translate("order", "确认订单"))
        self.cancle.setText(_translate("order", "退出系统"))


