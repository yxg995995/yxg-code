# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_register.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Admin_register(object):
    def setupUi(self, Admin_register):
        Admin_register.setObjectName("Admin_register")
        Admin_register.resize(431, 329)
        self.label = QtWidgets.QLabel(Admin_register)
        self.label.setGeometry(QtCore.QRect(160, 50, 130, 25))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(Admin_register)
        self.widget.setGeometry(QtCore.QRect(140, 240, 158, 25))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.register_2 = QtWidgets.QPushButton(self.widget)
        self.register_2.setObjectName("register_2")
        self.horizontalLayout.addWidget(self.register_2)
        self.cancle = QtWidgets.QPushButton(self.widget)
        self.cancle.setObjectName("cancle")
        self.horizontalLayout.addWidget(self.cancle)
        self.widget1 = QtWidgets.QWidget(Admin_register)
        self.widget1.setGeometry(QtCore.QRect(90, 97, 258, 129))
        self.widget1.setObjectName("widget1")
        self.gridLayout = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.widget1)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.adminN = QtWidgets.QLineEdit(self.widget1)
        self.adminN.setObjectName("adminN")
        self.gridLayout.addWidget(self.adminN, 0, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.widget1)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.adminP = QtWidgets.QLineEdit(self.widget1)
        self.adminP.setObjectName("adminP")
        self.gridLayout.addWidget(self.adminP, 1, 1, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.widget1)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.adminE = QtWidgets.QLineEdit(self.widget1)
        self.adminE.setObjectName("adminE")
        self.gridLayout.addWidget(self.adminE, 2, 1, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.widget1)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.yanzhen = QtWidgets.QLineEdit(self.widget1)
        self.yanzhen.setObjectName("yanzhen")
        self.gridLayout.addWidget(self.yanzhen, 3, 1, 1, 1)
        self.get = QtWidgets.QPushButton(self.widget1)
        self.get.setObjectName("get")
        self.gridLayout.addWidget(self.get, 3, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget1)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.adminK = QtWidgets.QLineEdit(self.widget1)
        self.adminK.setObjectName("adminK")
        self.gridLayout.addWidget(self.adminK, 4, 1, 1, 2)
        self.yanzhen.setPlaceholderText('区分大小写')
        self.retranslateUi(Admin_register)
        QtCore.QMetaObject.connectSlotsByName(Admin_register)
        self.adminP.setEchoMode(QtWidgets.QLineEdit.Password)

    def retranslateUi(self, Admin_register):
        _translate = QtCore.QCoreApplication.translate
        Admin_register.setWindowTitle(_translate("Admin_register", "管理员注册界面"))
        self.label.setText(_translate("Admin_register", "管理员注册"))
        self.register_2.setText(_translate("Admin_register", "注册"))
        self.cancle.setText(_translate("Admin_register", "取消"))
        self.label_2.setText(_translate("Admin_register", "名称"))
        self.label_3.setText(_translate("Admin_register", "密码"))
        self.label_4.setText(_translate("Admin_register", "邮箱"))
        self.label_6.setText(_translate("Admin_register", "验证码"))
        self.get.setText(_translate("Admin_register", "获取"))
        self.label_5.setText(_translate("Admin_register", "密钥"))


