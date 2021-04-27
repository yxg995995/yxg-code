# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'order.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
from qtpandas.models.DataFrameModel import DataFrameModel
class Ui_order(object):
    def setupUi(self, order):
        order.setObjectName("order")
        order.resize(681, 504)
        self.menulist = DataTableWidget(order)
        self.menulist.setGeometry(QtCore.QRect(90, 30, 581, 441))
        self.menulist.setObjectName("menulist")
        self.widget = QtWidgets.QWidget(order)
        self.widget.setGeometry(QtCore.QRect(10, 100, 77, 54))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.MyOrder = QtWidgets.QPushButton(self.widget)
        self.MyOrder.setObjectName("MyOrder")
        self.verticalLayout.addWidget(self.MyOrder)
        self.Check = QtWidgets.QPushButton(self.widget)
        self.Check.setObjectName("Check")
        self.verticalLayout.addWidget(self.Check)

        self.retranslateUi(order)
        QtCore.QMetaObject.connectSlotsByName(order)
        self.data=pd.read_csv(r'菜单.csv')
        self.model=DataFrameModel()
        self.menulist.setViewModel(self.model)
        self.model.setDataFrame(self.data)

    def retranslateUi(self, order):
        _translate = QtCore.QCoreApplication.translate
        order.setWindowTitle(_translate("order", "点餐界面"))
        self.MyOrder.setText(_translate("order", "我的订单"))
        self.Check.setText(_translate("order", "前往支付"))


from qtpandas.views.DataTableView import DataTableWidget
