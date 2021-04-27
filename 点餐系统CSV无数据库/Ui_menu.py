# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
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

#看菜界面
class Ui_menu(QWidget):
    def setupUi(self, menu):
        menu.setObjectName("menu")
        menu.resize(573, 413)
        self.verticalLayout = QtWidgets.QVBoxLayout(menu)
        self.verticalLayout.setObjectName("verticalLayout")
        self.MenuTable = QtWidgets.QTableView(menu)
        self.MenuTable.setObjectName("MenuTable")
        self.verticalLayout.addWidget(self.MenuTable)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cancel = QtWidgets.QPushButton(menu)
        self.cancel.setObjectName("cancel")
        self.horizontalLayout.addWidget(self.cancel)
        self.order = QtWidgets.QPushButton(menu)
        self.order.setObjectName("order")
        self.horizontalLayout.addWidget(self.order)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.MenuTable.horizontalHeader().setStretchLastSection(True)
        self.MenuTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.retranslateUi(menu)
        QtCore.QMetaObject.connectSlotsByName(menu)
        self.setTableView()
    
    #设置表格信息
    def setTableView(self):
        data=pd.read_csv('菜单.csv')
        rows=len(data)
        columns=len(data.columns)
        self.model=QStandardItemModel(rows,columns)
        self.model.setHorizontalHeaderLabels(['菜名','价格'])
        for row in range(rows):
            for column in range(columns):
                item=QStandardItem(np.array(data)[row][column])
                self.model.setItem(row,column,item)
        self.MenuTable.setModel(self.model)
                
        
        
    def retranslateUi(self, menu):
        _translate = QtCore.QCoreApplication.translate
        menu.setWindowTitle(_translate("menu", "菜单界面"))
        self.cancel.setText(_translate("menu", "不想吃了"))
        self.order.setText(_translate("menu", "前往点餐"))


