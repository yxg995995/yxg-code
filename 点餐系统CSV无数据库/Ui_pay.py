# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pay.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtWidgets import *

class Ui_Pay(object):
    def setupUi(self, Pay):
        Pay.setObjectName("Pay")
        Pay.resize(426, 326)
        self.message = QtWidgets.QTextEdit(Pay)
        self.message.setGeometry(QtCore.QRect(50, 30, 321, 221))
        self.message.setObjectName("message")
        self.Print = QtWidgets.QPushButton(Pay)
        self.Print.setGeometry(QtCore.QRect(20, 290, 75, 23))
        self.Print.setObjectName("Print")
        self.widget = QtWidgets.QWidget(Pay)
        self.widget.setGeometry(QtCore.QRect(240, 290, 163, 25))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.to_order = QtWidgets.QPushButton(self.widget)
        self.to_order.setObjectName("to_order")
        self.horizontalLayout.addWidget(self.to_order)
        self.byebye = QtWidgets.QPushButton(self.widget)
        self.byebye.setObjectName("byebye")
        self.horizontalLayout.addWidget(self.byebye)

        self.retranslateUi(Pay)
        QtCore.QMetaObject.connectSlotsByName(Pay)

    def retranslateUi(self, Pay):
        _translate = QtCore.QCoreApplication.translate
        Pay.setWindowTitle(_translate("Pay", "确认支付"))
        self.Print.setText(_translate("Pay", "打印信息"))
        self.to_order.setText(_translate("Pay", "继续点餐"))
        self.byebye.setText(_translate("Pay", "不点了"))


