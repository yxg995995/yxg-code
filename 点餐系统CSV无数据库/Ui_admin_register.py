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
        self.layoutWidget = QtWidgets.QWidget(Admin_register)
        self.layoutWidget.setGeometry(QtCore.QRect(140, 230, 158, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.be_admin = QtWidgets.QPushButton(self.layoutWidget)
        self.be_admin.setObjectName("be_admin")
        self.horizontalLayout.addWidget(self.be_admin)
        self.cancle = QtWidgets.QPushButton(self.layoutWidget)
        self.cancle.setObjectName("cancle")
        self.horizontalLayout.addWidget(self.cancle)
        self.widget = QtWidgets.QWidget(Admin_register)
        self.widget.setGeometry(QtCore.QRect(120, 100, 189, 100))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.adminID = QtWidgets.QLineEdit(self.widget)
        self.adminID.setObjectName("adminID")
        self.gridLayout.addWidget(self.adminID, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.adminP = QtWidgets.QLineEdit(self.widget)
        self.adminP.setEchoMode(QtWidgets.QLineEdit.Password)
        self.adminP.setObjectName("adminP")
        self.gridLayout.addWidget(self.adminP, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.adminCP = QtWidgets.QLineEdit(self.widget)
        self.adminCP.setEchoMode(QtWidgets.QLineEdit.Password)
        self.adminCP.setObjectName("adminCP")
        self.gridLayout.addWidget(self.adminCP, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.adminK = QtWidgets.QLineEdit(self.widget)
        self.adminK.setEchoMode(QtWidgets.QLineEdit.Password)
        self.adminK.setObjectName("adminK")
        self.gridLayout.addWidget(self.adminK, 3, 1, 1, 1)

        self.retranslateUi(Admin_register)
        QtCore.QMetaObject.connectSlotsByName(Admin_register)

    def retranslateUi(self, Admin_register):
        _translate = QtCore.QCoreApplication.translate
        Admin_register.setWindowTitle(_translate("Admin_register", "管理员注册界面"))
        self.label.setText(_translate("Admin_register", "管理员注册"))
        self.be_admin.setText(_translate("Admin_register", "注册"))
        self.cancle.setText(_translate("Admin_register", "取消"))
        self.label_2.setText(_translate("Admin_register", "ID"))
        self.label_3.setText(_translate("Admin_register", "密码"))
        self.label_4.setText(_translate("Admin_register", "确认密码"))
        self.label_5.setText(_translate("Admin_register", "密钥"))


