# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminLogin.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_admin_login(object):
    def setupUi(self, admin_login):
        admin_login.setObjectName("admin_login")
        admin_login.resize(571, 503)
        self.widget = QtWidgets.QWidget(admin_login)
        self.widget.setGeometry(QtCore.QRect(10, 10, 541, 331))
        self.widget.setStyleSheet("background-image: url(:/pic/bg.png);")
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QWidget(admin_login)
        self.widget_2.setGeometry(QtCore.QRect(90, 350, 410, 136))
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
        self.adminname = QtWidgets.QLineEdit(self.widget_2)
        self.adminname.setObjectName("adminname")
        self.gridLayout.addWidget(self.adminname, 0, 1, 1, 1)
        self.adminR = QtWidgets.QCommandLinkButton(self.widget_2)
        self.adminR.setObjectName("adminR")
        self.gridLayout.addWidget(self.adminR, 0, 2, 1, 1)
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
        self.linku = QtWidgets.QCommandLinkButton(self.widget_2)
        self.linku.setObjectName("linku")
        self.gridLayout.addWidget(self.linku, 1, 2, 1, 1)
        self.adminLogin = QtWidgets.QPushButton(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.adminLogin.setFont(font)
        self.adminLogin.setObjectName("adminLogin")
        self.gridLayout.addWidget(self.adminLogin, 2, 0, 1, 1)
        self.cancel = QtWidgets.QPushButton(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cancel.setFont(font)
        self.cancel.setObjectName("cancel")
        self.gridLayout.addWidget(self.cancel, 2, 1, 1, 1)

        self.retranslateUi(admin_login)
        QtCore.QMetaObject.connectSlotsByName(admin_login)
        admin_login.setTabOrder(self.adminname, self.password)
        admin_login.setTabOrder(self.password, self.adminLogin)
        admin_login.setTabOrder(self.adminLogin, self.cancel)
        admin_login.setTabOrder(self.cancel, self.adminR)
        admin_login.setTabOrder(self.adminR, self.linku)

    def retranslateUi(self, admin_login):
        _translate = QtCore.QCoreApplication.translate
        admin_login.setWindowTitle(_translate("admin_login", "管理员登陆界面"))
        self.label.setText(_translate("admin_login", "姓名"))
        self.adminR.setText(_translate("admin_login", "注册"))
        self.label_2.setText(_translate("admin_login", "密码"))
        self.linku.setText(_translate("admin_login", "用户登陆"))
        self.adminLogin.setText(_translate("admin_login", "登陆"))
        self.cancel.setText(_translate("admin_login", "取消"))


import source.apprcc_rc
