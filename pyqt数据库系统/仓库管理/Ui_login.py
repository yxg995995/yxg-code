# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(445, 345)
        Login.setStyleSheet("")
        self.login_window = QtWidgets.QWidget(Login)
        self.login_window.setGeometry(QtCore.QRect(120, 10, 211, 331))
        self.login_window.setStyleSheet("background-image: url(:/pic/空白图.jpg);")
        self.login_window.setObjectName("login_window")
        self.login_title = QtWidgets.QLabel(self.login_window)
        self.login_title.setGeometry(QtCore.QRect(30, 30, 161, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.login_title.setFont(font)
        self.login_title.setObjectName("login_title")
        self.label_4 = QtWidgets.QLabel(self.login_window)
        self.label_4.setGeometry(QtCore.QRect(40, 80, 131, 31))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/pic/C:/Users/Windows 10/Downloads/login.png"))
        self.label_4.setObjectName("label_4")
        self.layoutWidget = QtWidgets.QWidget(self.login_window)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 140, 177, 137))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.login_user = QtWidgets.QLabel(self.layoutWidget)
        self.login_user.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.login_user.setObjectName("login_user")
        self.gridLayout.addWidget(self.login_user, 0, 0, 1, 1)
        self.user_icon = QtWidgets.QLabel(self.layoutWidget)
        self.user_icon.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.user_icon.setText("")
        self.user_icon.setPixmap(QtGui.QPixmap(":/pic/user (1).png"))
        self.user_icon.setObjectName("user_icon")
        self.gridLayout.addWidget(self.user_icon, 1, 0, 1, 1)
        self.user = QtWidgets.QLineEdit(self.layoutWidget)
        self.user.setObjectName("user")
        self.gridLayout.addWidget(self.user, 1, 1, 1, 2)
        self.login_password = QtWidgets.QLabel(self.layoutWidget)
        self.login_password.setObjectName("login_password")
        self.gridLayout.addWidget(self.login_password, 2, 0, 1, 1)
        self.password_icon = QtWidgets.QLabel(self.layoutWidget)
        self.password_icon.setText("")
        self.password_icon.setPixmap(QtGui.QPixmap(":/pic/password.png"))
        self.password_icon.setObjectName("password_icon")
        self.gridLayout.addWidget(self.password_icon, 3, 0, 1, 1)
        self.password = QtWidgets.QLineEdit(self.layoutWidget)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.gridLayout.addWidget(self.password, 3, 1, 1, 2)
        self.login = QtWidgets.QPushButton(self.layoutWidget)
        self.login.setObjectName("login")
        self.gridLayout.addWidget(self.login, 4, 0, 1, 2)
        self.to_register = QtWidgets.QPushButton(self.layoutWidget)
        self.to_register.setObjectName("to_register")
        self.gridLayout.addWidget(self.to_register, 4, 2, 1, 1)
        self.icon = QtWidgets.QLabel(self.login_window)
        self.icon.setGeometry(QtCore.QRect(50, 80, 121, 31))
        self.icon.setText("")
        self.icon.setPixmap(QtGui.QPixmap(":/pic/login.png"))
        self.icon.setObjectName("icon")

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "登录界面"))
        self.login_title.setText(_translate("Login", "仓库管理系统"))
        self.login_user.setText(_translate("Login", "账号："))
        self.login_password.setText(_translate("Login", "密码："))
        self.login.setText(_translate("Login", "登录"))
        self.to_register.setText(_translate("Login", "注册"))


import source.apprcc_rc
