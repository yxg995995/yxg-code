# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_add_Dialog(object):
    def setupUi(self, add_Dialog):
        add_Dialog.setObjectName("add_Dialog")
        add_Dialog.resize(454, 318)
        self.layoutWidget = QtWidgets.QWidget(add_Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 27, 274, 161))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.type = QtWidgets.QLineEdit(self.layoutWidget)
        self.type.setObjectName("type")
        self.gridLayout.addWidget(self.type, 3, 0, 1, 1)
        self.out_price = QtWidgets.QLineEdit(self.layoutWidget)
        self.out_price.setObjectName("out_price")
        self.gridLayout.addWidget(self.out_price, 6, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 1)
        self.info_price = QtWidgets.QLineEdit(self.layoutWidget)
        self.info_price.setObjectName("info_price")
        self.gridLayout.addWidget(self.info_price, 1, 1, 1, 2)
        self.brand = QtWidgets.QLineEdit(self.layoutWidget)
        self.brand.setObjectName("brand")
        self.gridLayout.addWidget(self.brand, 3, 1, 1, 2)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)
        self.number = QtWidgets.QLineEdit(self.layoutWidget)
        self.number.setObjectName("number")
        self.gridLayout.addWidget(self.number, 6, 1, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 1, 1, 1)
        self.name = QtWidgets.QLineEdit(self.layoutWidget)
        self.name.setObjectName("name")
        self.gridLayout.addWidget(self.name, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 1, 1, 1)
        self.widget = QtWidgets.QWidget(add_Dialog)
        self.widget.setGeometry(QtCore.QRect(100, 210, 239, 25))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_btn = QtWidgets.QPushButton(self.widget)
        self.add_btn.setObjectName("add_btn")
        self.horizontalLayout.addWidget(self.add_btn)
        self.update_btn = QtWidgets.QPushButton(self.widget)
        self.update_btn.setObjectName("update_btn")
        self.horizontalLayout.addWidget(self.update_btn)
        self.cancle_btn = QtWidgets.QPushButton(self.widget)
        self.cancle_btn.setObjectName("cancle_btn")
        self.horizontalLayout.addWidget(self.cancle_btn)

        self.retranslateUi(add_Dialog)
        QtCore.QMetaObject.connectSlotsByName(add_Dialog)

    def retranslateUi(self, add_Dialog):
        _translate = QtCore.QCoreApplication.translate
        add_Dialog.setWindowTitle(_translate("add_Dialog", "新增产品"))
        self.label_9.setText(_translate("add_Dialog", "类型"))
        self.label.setText(_translate("add_Dialog", "产品名称"))
        self.label_2.setText(_translate("add_Dialog", "品牌"))
        self.label_6.setText(_translate("add_Dialog", "入仓价"))
        self.label_4.setText(_translate("add_Dialog", "出仓价"))
        self.label_3.setText(_translate("add_Dialog", "库存"))
        self.add_btn.setText(_translate("add_Dialog", "新增"))
        self.update_btn.setText(_translate("add_Dialog", "更新"))
        self.cancle_btn.setText(_translate("add_Dialog", "取消"))


