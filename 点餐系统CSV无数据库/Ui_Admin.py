# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Admin.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from qtpandas.views.DataTableView import DataTableWidget
from qtpandas.models.DataFrameModel import DataFrameModel
import pandas as pd

class Ui_Admin(object):
    def setupUi(self, Admin):
        Admin.setObjectName("Admin")
        Admin.resize(679, 490)
        self.centralwidget = QtWidgets.QWidget(Admin)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.menu_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.menu_btn.setFont(font)
        self.menu_btn.setObjectName("menu_btn")
        self.horizontalLayout.addWidget(self.menu_btn)
        self.user_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.user_btn.setFont(font)
        self.user_btn.setObjectName("user_btn")
        self.horizontalLayout.addWidget(self.user_btn)
        self.order_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.order_btn.setFont(font)
        self.order_btn.setObjectName("order_btn")
        self.horizontalLayout.addWidget(self.order_btn)
        self.back = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.back.setFont(font)
        self.back.setObjectName("back")
        self.horizontalLayout.addWidget(self.back)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.infoTable = DataTableWidget(self.centralwidget)
        self.infoTable.setObjectName("infoTable")
        self.verticalLayout.addWidget(self.infoTable)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        
        self.save = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.save.setFont(font)
        self.save.setObjectName("save")
        self.horizontalLayout_2.addWidget(self.save)
        
        self.original = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.original.setFont(font)
        self.original.setObjectName("original")
        self.horizontalLayout_2.addWidget(self.original)
        
        self.fresh = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.fresh.setFont(font)
        self.fresh.setObjectName("fresh")
        self.horizontalLayout_2.addWidget(self.fresh)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        Admin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Admin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 679, 23))
        self.menubar.setObjectName("menubar")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        Admin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Admin)
        self.statusbar.setObjectName("statusbar")
        Admin.setStatusBar(self.statusbar)
        self.update1 = QtWidgets.QAction(Admin)
        self.update1.setObjectName("update1")
        self.add = QtWidgets.QAction(Admin)
        self.add.setObjectName("add")
        self.update2 = QtWidgets.QAction(Admin)
        self.update2.setObjectName("update2")
        self.delete_2 = QtWidgets.QAction(Admin)
        self.delete_2.setObjectName("delete_2")
        self.delete_3 = QtWidgets.QAction(Admin)
        self.delete_3.setObjectName("delete_3")
        self.add_2 = QtWidgets.QAction(Admin)
        self.add_2.setObjectName("add_2")
        self.help = QtWidgets.QAction(Admin)
        self.help.setObjectName("help")
        self.actionAllEmpty = QtWidgets.QAction(Admin)
        self.actionAllEmpty.setObjectName("actionAllEmpty")
        self.menu_4.addAction(self.help)
        self.menubar.addAction(self.menu_4.menuAction())

        self.retranslateUi(Admin)
        QtCore.QMetaObject.connectSlotsByName(Admin)
        
        self.model=DataFrameModel()
        self.infoTable.setModel(self.model)

    def retranslateUi(self, Admin):
        _translate = QtCore.QCoreApplication.translate
        Admin.setWindowTitle(_translate("Admin", "后台管理界面"))
        self.menu_btn.setText(_translate("Admin", "菜单管理"))
        self.user_btn.setText(_translate("Admin", "用户管理"))
        self.order_btn.setText(_translate("Admin", "订单信息"))
        self.back.setText(_translate("Admin", "返回登录"))
        self.save.setText(_translate("Admin", "保存数据"))
        self.original.setText(_translate("Admin", "初始化"))
        self.fresh.setText(_translate("Admin", "刷新"))
        self.menu_4.setTitle(_translate("Admin", "帮助"))
        self.update1.setText(_translate("Admin", "update"))
        self.add.setText(_translate("Admin", "add"))
        self.update2.setText(_translate("Admin", "update"))
        self.delete_2.setText(_translate("Admin", "delete"))
        self.delete_3.setText(_translate("Admin", "delete"))
        self.add_2.setText(_translate("Admin", "add"))
        self.help.setText(_translate("Admin", "help"))
        self.actionAllEmpty.setText(_translate("Admin", "AllEmpty"))



