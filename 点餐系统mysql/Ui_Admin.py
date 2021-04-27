# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Admin.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Ui_Admin(QDialog):
    def setupUi(self, Admin):
        Admin.setObjectName("Admin")
        Admin.resize(717, 542)
        self.gridLayout = QtWidgets.QGridLayout(Admin)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_btn = QtWidgets.QPushButton(Admin)
        self.add_btn.setObjectName("add_btn")
        self.horizontalLayout.addWidget(self.add_btn)
        self.delete_btn = QtWidgets.QPushButton(Admin)
        self.delete_btn.setObjectName("delete_btn")
        self.horizontalLayout.addWidget(self.delete_btn)
        self.one_empty = QtWidgets.QPushButton(Admin)
        self.one_empty.setEnabled(False)
        self.one_empty.setObjectName("one_empty")
        self.horizontalLayout.addWidget(self.one_empty)
        self.all_empty = QtWidgets.QPushButton(Admin)
        self.all_empty.setEnabled(False)
        self.all_empty.setObjectName("all_empty")
        self.horizontalLayout.addWidget(self.all_empty)
        self.label = QtWidgets.QLabel(Admin)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.SUM = QtWidgets.QLCDNumber(Admin)
        self.SUM.setObjectName("SUM")
        self.horizontalLayout.addWidget(self.SUM)
        self.label_2 = QtWidgets.QLabel(Admin)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.table_btn = QtWidgets.QPushButton(Admin)
        self.table_btn.setObjectName("table_btn")
        self.verticalLayout.addWidget(self.table_btn)
        self.menu_btn = QtWidgets.QPushButton(Admin)
        self.menu_btn.setObjectName("menu_btn")
        self.verticalLayout.addWidget(self.menu_btn)
        self.order_btn = QtWidgets.QPushButton(Admin)
        self.order_btn.setObjectName("order_btn")
        self.verticalLayout.addWidget(self.order_btn)
        self.user_btn = QtWidgets.QPushButton(Admin)
        self.user_btn.setObjectName("user_btn")
        self.verticalLayout.addWidget(self.user_btn)
        self.back = QtWidgets.QPushButton(Admin)
        self.back.setObjectName("back")
        self.verticalLayout.addWidget(self.back)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.tableView = QtWidgets.QTableView(Admin)
        self.tableView.setObjectName("tableView")
        self.gridLayout.addWidget(self.tableView, 1, 1, 1, 1)

        self.retranslateUi(Admin)
        QtCore.QMetaObject.connectSlotsByName(Admin)

    def retranslateUi(self, Admin):
        _translate = QtCore.QCoreApplication.translate
        Admin.setWindowTitle(_translate("Admin", "后台管理界面"))
        self.add_btn.setText(_translate("Admin", "新增"))
        self.delete_btn.setText(_translate("Admin", "删除"))
        self.one_empty.setText(_translate("Admin", "设置为空"))
        self.all_empty.setText(_translate("Admin", "全空按钮"))
        self.label.setText(_translate("Admin", "营业额"))
        self.label_2.setText(_translate("Admin", "元"))
        self.table_btn.setText(_translate("Admin", "餐桌管理"))
        self.menu_btn.setText(_translate("Admin", "菜单管理"))
        self.order_btn.setText(_translate("Admin", "订单管理"))
        self.user_btn.setText(_translate("Admin", "用户管理"))
        self.back.setText(_translate("Admin", "返回登陆"))


