# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'orderingType.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Type(object):
    def setupUi(self, Type):
        Type.setObjectName("Type")
        Type.setEnabled(True)
        Type.resize(510, 371)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        Type.setFont(font)
        Type.setStyleSheet("background-image: url(:/pic/bg.png);")
        self.now_btn = QtWidgets.QPushButton(Type)
        self.now_btn.setGeometry(QtCore.QRect(44, 72, 71, 51))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.now_btn.setFont(font)
        self.now_btn.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.now_btn.setObjectName("now_btn")
        self.book_btn = QtWidgets.QPushButton(Type)
        self.book_btn.setGeometry(QtCore.QRect(40, 180, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.book_btn.setFont(font)
        self.book_btn.setStyleSheet("background-color: rgb(160, 147, 255);")
        self.book_btn.setObjectName("book_btn")
        self.book_btn.raise_()
        self.now_btn.raise_()

        self.retranslateUi(Type)
        QtCore.QMetaObject.connectSlotsByName(Type)

    def retranslateUi(self, Type):
        _translate = QtCore.QCoreApplication.translate
        Type.setWindowTitle(_translate("Type", "点单选择界面"))
        self.now_btn.setText(_translate("Type", "直接就餐"))
        self.book_btn.setText(_translate("Type", "预约就餐"))

