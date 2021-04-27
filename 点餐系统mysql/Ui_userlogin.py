# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'userLogin.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_user_login(object):
    def setupUi(self, user_login):
        user_login.setObjectName("user_login")
        user_login.resize(576, 526)
        self.widget = QtWidgets.QWidget(user_login)
        self.widget.setGeometry(QtCore.QRect(20, 10, 541, 331))
        self.widget.setStyleSheet("background-image: url(:/pic/bg.png);")
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QWidget(user_login)
        self.widget_2.setGeometry(QtCore.QRect(80, 360, 410, 136))
        self.widget_2.setObjectName("widget_2")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.username = QtWidgets.QLineEdit(self.widget_2)
        self.username.setObjectName("username")
        self.gridLayout.addWidget(self.username, 0, 1, 1, 1)
        self.linkReg = QtWidgets.QCommandLinkButton(self.widget_2)
        self.linkReg.setObjectName("linkReg")
        self.gridLayout.addWidget(self.linkReg, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.password = QtWidgets.QLineEdit(self.widget_2)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.gridLayout.addWidget(self.password, 1, 1, 1, 1)
        self.linkAdmin = QtWidgets.QCommandLinkButton(self.widget_2)
        self.linkAdmin.setObjectName("linkAdmin")
        self.gridLayout.addWidget(self.linkAdmin, 1, 2, 1, 1)
        self.userLogin = QtWidgets.QPushButton(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.userLogin.setFont(font)
        self.userLogin.setObjectName("userLogin")
        self.gridLayout.addWidget(self.userLogin, 2, 0, 1, 1)
        self.cancel = QtWidgets.QPushButton(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cancel.setFont(font)
        self.cancel.setObjectName("cancel")
        self.gridLayout.addWidget(self.cancel, 2, 1, 1, 1)

        self.retranslateUi(user_login)
        QtCore.QMetaObject.connectSlotsByName(user_login)
        user_login.setTabOrder(self.username, self.password)
        user_login.setTabOrder(self.password, self.userLogin)
        user_login.setTabOrder(self.userLogin, self.cancel)
        user_login.setTabOrder(self.cancel, self.linkReg)
        user_login.setTabOrder(self.linkReg, self.linkAdmin)

    def retranslateUi(self, user_login):
        _translate = QtCore.QCoreApplication.translate
        user_login.setWindowTitle(_translate("user_login", "用户登陆界面"))
        self.label.setText(_translate("user_login", "姓名"))
        self.linkReg.setText(_translate("user_login", "注册"))
        self.label_2.setText(_translate("user_login", "密码"))
        self.linkAdmin.setText(_translate("user_login", "管理员登陆"))
        self.userLogin.setText(_translate("user_login", "登陆"))
        self.cancel.setText(_translate("user_login", "取消"))


import source.apprcc_rc
