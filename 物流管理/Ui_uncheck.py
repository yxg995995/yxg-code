# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'unCheck.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Uncheck(object):
    def setupUi(self, Uncheck):
        Uncheck.setObjectName("Uncheck")
        Uncheck.resize(728, 553)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Uncheck)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget = QtWidgets.QWidget(Uncheck)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.key = QtWidgets.QLineEdit(self.widget)
        self.key.setText("")
        self.key.setObjectName("key")
        self.horizontalLayout_4.addWidget(self.key)
        self.detail = QtWidgets.QPushButton(self.widget)
        self.detail.setObjectName("detail")
        self.horizontalLayout_4.addWidget(self.detail)
        self.clear = QtWidgets.QPushButton(self.widget)
        self.clear.setObjectName("clear")
        self.horizontalLayout_4.addWidget(self.clear)
        self.back = QtWidgets.QPushButton(self.widget)
        self.back.setObjectName("back")
        self.horizontalLayout_4.addWidget(self.back)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.tableView1 = QtWidgets.QTableView(self.widget)
        self.tableView1.setObjectName("tableView1")
        self.verticalLayout_2.addWidget(self.tableView1)
        self.verticalLayout_3.addWidget(self.widget)
        self.tabWidget = QtWidgets.QTabWidget(Uncheck)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tableView2 = QtWidgets.QTableView(self.tab)
        self.tableView2.setObjectName("tableView2")
        self.horizontalLayout_3.addWidget(self.tableView2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout.setObjectName("gridLayout")
        self.tableView3 = QtWidgets.QTableView(self.tab_2)
        self.tableView3.setObjectName("tableView3")
        self.gridLayout.addWidget(self.tableView3, 0, 0, 2, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableView4 = QtWidgets.QTableView(self.tab_3)
        self.tableView4.setObjectName("tableView4")
        self.horizontalLayout.addWidget(self.tableView4)
        self.tabWidget.addTab(self.tab_3, "")
        self.verticalLayout_3.addWidget(self.tabWidget)

        self.retranslateUi(Uncheck)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Uncheck)

    def retranslateUi(self, Uncheck):
        _translate = QtCore.QCoreApplication.translate
        Uncheck.setWindowTitle(_translate("Uncheck", "未验收订单界面"))
        self.label.setText(_translate("Uncheck", "未验收订单"))
        self.key.setPlaceholderText(_translate("Uncheck", "请输入订单编号"))
        self.detail.setText(_translate("Uncheck", "更改物品信息"))
        self.clear.setText(_translate("Uncheck", "清空"))
        self.back.setText(_translate("Uncheck", "退出"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Uncheck", "订单信息"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Uncheck", "物品信息"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Uncheck", "车辆信息"))


