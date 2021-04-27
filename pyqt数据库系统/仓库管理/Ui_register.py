# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QWidget , QHBoxLayout , QVBoxLayout , QApplication, 
                             QPushButton, QLineEdit ,QLabel , QSplitter ,  QTableView , 
                             QHeaderView , QMessageBox )
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.Qt import *
from PyQt5.QtSql import QSqlDatabase  , QSqlQueryModel , QSqlQuery

class Ui_Register(object):
    def setupUi(self, Register):
        Register.setObjectName("Register")
        Register.resize(557, 400)
        Register.setStyleSheet("")
        self.register_title = QtWidgets.QLabel(Register)
        self.register_title.setGeometry(QtCore.QRect(190, 20, 171, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        
        self.register_title.setFont(font)
        self.register_title.setStyleSheet("QLabel{border:None}")
        self.register_title.setAlignment(QtCore.Qt.AlignCenter)
        self.register_title.setObjectName("register_title")
        self.user_error = QtWidgets.QLabel(Register)
        
        self.user_error.setGeometry(QtCore.QRect(122, 109, 168, 16))
        self.user_error.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.user_error.setObjectName("user_error")
        self.register_user = QtWidgets.QLabel(Register)
        self.register_user.setGeometry(QtCore.QRect(122, 83, 63, 19))
        
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        
        self.register_user.setFont(font)
        self.register_user.setStyleSheet("")
        self.register_user.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.register_user.setObjectName("register_user")
        self.user = QtWidgets.QLineEdit(Register)
        
        self.user.setGeometry(QtCore.QRect(233, 83, 191, 20))
        self.user.setObjectName("user")
        self.register_password = QtWidgets.QLabel(Register)
        self.register_password.setGeometry(QtCore.QRect(122, 127, 63, 19))
        
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        
        self.register_password.setFont(font)
        self.register_password.setObjectName("register_password")
        self.password = QtWidgets.QLineEdit(Register)
        self.password.setGeometry(QtCore.QRect(233, 127, 191, 20))
        self.password.setMaxLength(12)
        
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.password_tip = QtWidgets.QLabel(Register)
        self.password_tip.setEnabled(True)
        
        self.password_tip.setGeometry(QtCore.QRect(122, 153, 234, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        
        self.password_tip.setFont(font)
        self.password_tip.setMouseTracking(False)
        self.password_tip.setStyleSheet("")
        
        self.password_tip.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.password_tip.setObjectName("password_tip")
        
        self.register_repassword = QtWidgets.QLabel(Register)
        self.register_repassword.setGeometry(QtCore.QRect(122, 171, 105, 19))
        
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        
        self.register_repassword.setFont(font)
        self.register_repassword.setObjectName("register_repassword")
        self.repassword = QtWidgets.QLineEdit(Register)
        self.repassword.setGeometry(QtCore.QRect(233, 171, 191, 20))
        self.repassword.setMaxLength(12)
        
        self.repassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.repassword.setObjectName("repassword")
        self.repassword_tip = QtWidgets.QLabel(Register)
        
        self.repassword_tip.setEnabled(True)
        self.repassword_tip.setGeometry(QtCore.QRect(122, 197, 108, 16))
        self.repassword_tip.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.repassword_tip.setObjectName("repassword_tip")
        
        self.layoutWidget = QtWidgets.QWidget(Register)
        self.layoutWidget.setGeometry(QtCore.QRect(191, 250, 161, 58))
        self.layoutWidget.setObjectName("layoutWidget")
        
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.register_2 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(13)
        
        font.setBold(True)
        font.setWeight(75)
        self.register_2.setFont(font)
        
        self.register_2.setObjectName("register_2")
        self.verticalLayout.addWidget(self.register_2)
        self.cancle = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        
        font.setFamily("楷体")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        
        self.cancle.setFont(font)
        self.cancle.setObjectName("cancle")
        
        self.verticalLayout.addWidget(self.cancle)
        self.user_error.setVisible(0)
        self.repassword_tip.setVisible(0)

        self.retranslateUi(Register)
        self.register_2.clicked.connect(Register.close)
        self.cancle.clicked.connect(self.user.clear)
        self.cancle.clicked.connect(self.password.clear)
        self.cancle.clicked.connect(self.repassword.clear)
        QtCore.QMetaObject.connectSlotsByName(Register)

    def retranslateUi(self, Register):
        _translate = QtCore.QCoreApplication.translate
        Register.setWindowTitle(_translate("Register", "注册界面"))
        self.register_title.setText(_translate("Register", "注册账号"))
        self.user_error.setText(_translate("Register", "账号已经存在，请重新输入账号"))
        self.register_user.setText(_translate("Register", "账号："))
        
        self.register_password.setText(_translate("Register", "密码："))
        self.password_tip.setText(_translate("Register", "密码由数字和字母或者符合组成，不少于8位"))
        self.register_repassword.setText(_translate("Register", "确认密码："))
        self.repassword_tip.setText(_translate("Register", "两次密码输入不一致"))
        self.register_2.setText(_translate("Register", "注册"))
        
        self.cancle.setText(_translate("Register", "取消"))

import sys

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    product=QtWidgets.QWidget()
    win=Ui_Register()
    win.setupUi(product)
    product.show()
    sys.exit(app.exec_())
