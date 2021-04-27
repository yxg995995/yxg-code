# -*- coding: utf-8 -*-

# test implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import sip
class Ui_test(object):
    def setupUi(self, test):
        test.setObjectName("test")
        test.resize(772, 300)
        self.layoutWidget = QtWidgets.QWidget(test)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 50, 700, 23))
        self.layoutWidget.setObjectName("layoutWidget")

        self.towCity = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.towCity.setContentsMargins(0, 0, 0, 0)
        self.towCity.setObjectName("towCity")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.towCity.addWidget(self.label_8)
        self.now_city_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.now_city_2.setObjectName("now_city_2")
        self.towCity.addWidget(self.now_city_2)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self.towCity.addWidget(self.label_9)
        self.start1_2 = QtWidgets.QDateEdit(self.layoutWidget)
        self.start1_2.setObjectName("start1_2")
        self.towCity.addWidget(self.start1_2)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.towCity.addWidget(self.label_10)
        self.end1_2 = QtWidgets.QDateEdit(self.layoutWidget)
        self.end1_2.setObjectName("end1_2")
        self.towCity.addWidget(self.end1_2)
        self.one = QtWidgets.QPushButton(test)
        self.one.setGeometry(QtCore.QRect(170, 190, 75, 23))
        self.one.setObjectName("one")
        self.two = QtWidgets.QPushButton(test)
        self.two.setGeometry(QtCore.QRect(270, 190, 75, 23))
        self.two.setObjectName("two")
        self.first = QtWidgets.QPushButton(test)
        self.first.setGeometry(QtCore.QRect(370, 190, 75, 23))
        self.first.setObjectName("first")
        self.second = QtWidgets.QPushButton(test)
        self.second.setGeometry(QtCore.QRect(470, 190, 75, 23))
        self.second.setObjectName("second")
        self.label_11=''
        self.now_city_3=''
        self.retranslateUi(test)
        QtCore.QMetaObject.connectSlotsByName(test)
        
        self.one.clicked.connect(self.one1)
        self.two.clicked.connect(self.two2)
        self.first.clicked.connect(self.print1)
        self.second.clicked.connect(self.print2)
    
    def print1(self):
        print(self.now_city_2.text())
    
    def print2(self):
        print(self.now_city_3.text())
    
    def one1(self):
        sip.delete(self.towCity)
        self.towCity = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.towCity.setContentsMargins(0, 0, 0, 0)
        self.towCity.setObjectName("towCity")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.towCity.addWidget(self.label_8)
        self.now_city_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.now_city_2.setObjectName("now_city_2")
        self.towCity.addWidget(self.now_city_2)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self.towCity.addWidget(self.label_9)
        self.start1_2 = QtWidgets.QDateEdit(self.layoutWidget)
        self.start1_2.setObjectName("start1_2")
        self.towCity.addWidget(self.start1_2)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.towCity.addWidget(self.label_10)
        self.end1_2 = QtWidgets.QDateEdit(self.layoutWidget)
        self.end1_2.setObjectName("end1_2")
        self.towCity.addWidget(self.end1_2)
        self.one = QtWidgets.QPushButton(test)
        self.one.setGeometry(QtCore.QRect(170, 190, 75, 23))
        self.one.setObjectName("one")
        self.two = QtWidgets.QPushButton(test)
        self.two.setGeometry(QtCore.QRect(270, 190, 75, 23))
        self.two.setObjectName("two")
        self.retranslateUi1(test)
        QtCore.QMetaObject.connectSlotsByName(test)     
        
    def two2(self):
        sip.delete(self.towCity)
        self.towCity = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.towCity.setContentsMargins(0, 0, 0, 0)
        self.towCity.setObjectName("towCity")
        
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.towCity.addWidget(self.label_8)
        
        self.now_city_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.now_city_2.setObjectName("now_city_2")
        self.towCity.addWidget(self.now_city_2)
        
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.towCity.addWidget(self.label_11)
        
        self.now_city_3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.now_city_3.setObjectName("now_city_3")
        self.towCity.addWidget(self.now_city_3)
        
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self.towCity.addWidget(self.label_9)
        self.start1_2 = QtWidgets.QDateEdit(self.layoutWidget)
        self.start1_2.setObjectName("start1_2")
        self.towCity.addWidget(self.start1_2)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.towCity.addWidget(self.label_10)
        self.end1_2 = QtWidgets.QDateEdit(self.layoutWidget)
        self.end1_2.setObjectName("end1_2")
        self.towCity.addWidget(self.end1_2)
        self.retranslateUi2(test)
        QtCore.QMetaObject.connectSlotsByName(test)        
        
    def retranslateUi(self, test):
        _translate = QtCore.QCoreApplication.translate
        test.setWindowTitle(_translate("test", "test"))
        self.label_8.setText(_translate("test", "城市1"))
        self.label_9.setText(_translate("test", "时间范围"))
        self.label_10.setText(_translate("test", "~"))
        self.one.setText(_translate("test", "one"))
        self.two.setText(_translate("test", "two"))
        self.first.setText(_translate("test", "first"))
        self.second.setText(_translate("test", "second"))
        
    def retranslateUi1(self, test):
        _translate = QtCore.QCoreApplication.translate
        test.setWindowTitle(_translate("test", "test"))
        self.label_8.setText(_translate("test", "城市1"))
        self.label_9.setText(_translate("test", "时间范围"))
        self.label_10.setText(_translate("test", "~"))
        self.one.setText(_translate("test", "one"))
        self.two.setText(_translate("test", "two"))
        self.first.setText(_translate("test", "first"))
        self.second.setText(_translate("test", "second"))

    def retranslateUi2(self, test):
        _translate = QtCore.QCoreApplication.translate
        test.setWindowTitle(_translate("test", "test"))
        self.label_8.setText(_translate("test", "城市1"))
        self.label_11.setText(_translate("test", "城市2"))
        self.label_9.setText(_translate("test", "时间范围"))
        self.label_10.setText(_translate("test", "~"))
        self.one.setText(_translate("test", "one"))
        self.two.setText(_translate("test", "two"))
        self.first.setText(_translate("test", "first"))
        self.second.setText(_translate("test", "second"))

import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
if __name__=="__main__":
    app=QApplication(sys.argv)
    test=QMainWindow()
    win=Ui_test()
    win.setupUi(test)
    test.show()
    sys.exit(app.exec_())
