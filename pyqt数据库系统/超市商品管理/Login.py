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
        Login.resize(600, 375)
        Login.setStyleSheet("background-image: url(:/pic/login.png);")
        self.widget = QtWidgets.QWidget(Login)
        self.widget.setGeometry(QtCore.QRect(130, 30, 331, 291))
        self.widget.setStyleSheet("background-image: url(:/pic/空白图.jpg);")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(70, 10, 211, 71))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(self.widget)
        self.layoutWidget.setGeometry(QtCore.QRect(90, 80, 161, 111))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.userName = QtWidgets.QLineEdit(self.layoutWidget)
        self.userName.setObjectName("userName")
        self.verticalLayout.addWidget(self.userName)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.password = QtWidgets.QLineEdit(self.layoutWidget)
        self.password.setObjectName("password")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.verticalLayout.addWidget(self.password)
        self.splitter = QtWidgets.QSplitter(self.widget)
        self.splitter.setGeometry(QtCore.QRect(90, 220, 151, 41))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.login_btn = QtWidgets.QPushButton(self.splitter)
        self.login_btn.setObjectName("login_btn")
        self.register_btn = QtWidgets.QCommandLinkButton(self.splitter)
        self.register_btn.setObjectName("register_btn")

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "登录界面"))
        self.label.setText(_translate("Login", "超市商品管理系统"))
        self.label_2.setText(_translate("Login", "用户名"))
        self.label_3.setText(_translate("Login", "密码"))
        self.login_btn.setText(_translate("Login", "登录"))
        self.register_btn.setText(_translate("Login", "注册"))


import apprcc_rc
