# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fun.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_cz_Dialog(object):
    def setupUi(self, cz_Dialog):
        cz_Dialog.setObjectName("cz_Dialog")
        cz_Dialog.resize(454, 318)
        self.layoutWidget = QtWidgets.QWidget(cz_Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(90, 70, 271, 101))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.attr2 = QtWidgets.QLabel(self.layoutWidget)
        self.attr2.setText("")
        self.attr2.setObjectName("attr2")
        self.gridLayout.addWidget(self.attr2, 0, 1, 1, 2)
        self.attr4 = QtWidgets.QLabel(self.layoutWidget)
        self.attr4.setText("")
        self.attr4.setObjectName("attr4")
        self.gridLayout.addWidget(self.attr4, 2, 1, 1, 2)
        self.input1 = QtWidgets.QLineEdit(self.layoutWidget)
        self.input1.setObjectName("input1")
        self.gridLayout.addWidget(self.input1, 1, 0, 1, 1)
        self.attr1 = QtWidgets.QLabel(self.layoutWidget)
        self.attr1.setText("")
        self.attr1.setObjectName("attr1")
        self.gridLayout.addWidget(self.attr1, 0, 0, 1, 1)
        self.attr3 = QtWidgets.QLabel(self.layoutWidget)
        self.attr3.setText("")
        self.attr3.setObjectName("attr3")
        self.gridLayout.addWidget(self.attr3, 2, 0, 1, 1)
        self.input2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.input2.setObjectName("input2")
        self.gridLayout.addWidget(self.input2, 1, 1, 1, 2)
        self.input4 = QtWidgets.QLineEdit(self.layoutWidget)
        self.input4.setObjectName("input4")
        self.gridLayout.addWidget(self.input4, 3, 1, 1, 2)
        self.input3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.input3.setObjectName("input3")
        self.gridLayout.addWidget(self.input3, 3, 0, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(cz_Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(100, 210, 239, 25))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_btn = QtWidgets.QPushButton(self.layoutWidget1)
        self.add_btn.setObjectName("add_btn")
        self.horizontalLayout.addWidget(self.add_btn)
        self.cancle_btn = QtWidgets.QPushButton(self.layoutWidget1)
        self.cancle_btn.setObjectName("cancle_btn")
        self.horizontalLayout.addWidget(self.cancle_btn)

        self.retranslateUi(cz_Dialog)
        QtCore.QMetaObject.connectSlotsByName(cz_Dialog)
        cz_Dialog.setTabOrder(self.input1, self.input2)
        cz_Dialog.setTabOrder(self.input2, self.input3)
        cz_Dialog.setTabOrder(self.input3, self.input4)
        cz_Dialog.setTabOrder(self.input4, self.add_btn)
        cz_Dialog.setTabOrder(self.add_btn, self.cancle_btn)

    def retranslateUi(self, cz_Dialog):
        _translate = QtCore.QCoreApplication.translate
        cz_Dialog.setWindowTitle(_translate("cz_Dialog", "新增产品"))
        self.add_btn.setText(_translate("cz_Dialog", "新增"))
        self.cancle_btn.setText(_translate("cz_Dialog", "取消"))


