# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tablelist.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QWidget , QHBoxLayout , QVBoxLayout , QApplication, 
                             QPushButton, QLineEdit ,QLabel , QSplitter ,  QTableView , 
                             QHeaderView , QMessageBox )
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.Qt import *
from PyQt5.QtSql import QSqlDatabase  , QSqlQueryModel , QSqlQuery

class Ui_TableList(object):
    def setupUi(self, TableList):
        TableList.setObjectName("TableList")
        TableList.resize(400, 300)
        font = QtGui.QFont()
        font.setPointSize(11)
        TableList.setFont(font)
        
        self.layoutWidget = QtWidgets.QWidget(TableList)
        self.layoutWidget.setGeometry(QtCore.QRect(130, 70, 130, 159))
        self.layoutWidget.setObjectName("layoutWidget")
        
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.product_btn = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        
        self.product_btn.setFont(font)
        self.product_btn.setObjectName("product_btn")
        self.verticalLayout.addWidget(self.product_btn)
        self.splitter = QtWidgets.QSplitter(self.layoutWidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        
        self.info_btn = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        
        self.info_btn.setFont(font)
        self.info_btn.setObjectName("info_btn")
        self.info_detailBtn = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.info_detailBtn.setFont(font)
        self.info_detailBtn.setObjectName("info_detailBtn")
        self.verticalLayout.addWidget(self.splitter)
        
        self.splitter_2 = QtWidgets.QSplitter(self.layoutWidget)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        
        self.out_btn = QtWidgets.QPushButton(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        
        font.setWeight(75)
        self.out_btn.setFont(font)
        self.out_btn.setObjectName("out_btn")
        self.out_detailBtn = QtWidgets.QPushButton(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        
        font.setBold(True)
        font.setWeight(75)
        self.out_detailBtn.setFont(font)
        self.out_detailBtn.setObjectName("out_detailBtn")
        self.verticalLayout.addWidget(self.splitter_2)
        self.label = QtWidgets.QLabel(TableList)
        self.label.setGeometry(QtCore.QRect(110, 20, 161, 31))
        font = QtGui.QFont()
        
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(TableList)
        QtCore.QMetaObject.connectSlotsByName(TableList)

    def retranslateUi(self, TableList):
        _translate = QtCore.QCoreApplication.translate
        TableList.setWindowTitle(_translate("TableList", "查看表单"))
        self.product_btn.setText(_translate("TableList", "库存商品表"))
        self.info_btn.setText(_translate("TableList", "入库单表"))
        
        self.info_detailBtn.setText(_translate("TableList", "入库单明细表"))
        self.out_btn.setText(_translate("TableList", "出库单表"))
        self.out_detailBtn.setText(_translate("TableList", "出库单明细表"))
        self.label.setText(_translate("TableList", "数据库表单"))


import sys

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    product=QtWidgets.QWidget()
    win=Ui_TableList()
    win.setupUi(product)
    product.show()
    sys.exit(app.exec_())