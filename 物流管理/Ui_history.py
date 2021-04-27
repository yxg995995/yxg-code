# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'history.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtWidgets import *

class Ui_History(object):
    def setupUi(self, History):
        History.setObjectName("History")
        History.resize(493, 433)
        self.gridLayout = QtWidgets.QGridLayout(History)
        self.gridLayout.setObjectName("gridLayout")
        self.key = QtWidgets.QLineEdit(History)
        self.key.setObjectName("key")
        self.gridLayout.addWidget(self.key, 0, 0, 1, 1)
        self.search = QtWidgets.QPushButton(History)
        self.search.setObjectName("search")
        self.gridLayout.addWidget(self.search, 0, 1, 1, 1)
        self.clear = QtWidgets.QPushButton(History)
        self.clear.setObjectName("clear")
        self.gridLayout.addWidget(self.clear, 0, 2, 1, 1)
        self.Quit = QtWidgets.QPushButton(History)
        self.Quit.setObjectName("Quit")
        self.gridLayout.addWidget(self.Quit, 0, 3, 1, 1)
        self.widget = QtWidgets.QWidget(History)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableView = QtWidgets.QTableView(self.widget)
        self.tableView.setObjectName("tableView")
        self.horizontalLayout.addWidget(self.tableView)
        self.gridLayout.addWidget(self.widget, 1, 0, 1, 4)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.retranslateUi(History)
        QtCore.QMetaObject.connectSlotsByName(History)

    def retranslateUi(self, History):
        _translate = QtCore.QCoreApplication.translate
        History.setWindowTitle(_translate("History", "历史订单查询"))
        self.key.setPlaceholderText(_translate("History", "输入订单号查询"))
        self.search.setText(_translate("History", "搜索"))
        self.clear.setText(_translate("History", "初始化"))
        self.Quit.setText(_translate("History", "退出"))


