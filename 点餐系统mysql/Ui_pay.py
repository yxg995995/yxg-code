# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pay.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Pay(object):
    def setupUi(self, Pay):
        Pay.setObjectName("Pay")
        Pay.resize(400, 300)
        self.widget = QtWidgets.QWidget(Pay)
        self.widget.setGeometry(QtCore.QRect(90, 50, 198, 61))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.paynumber = QtWidgets.QLCDNumber(self.widget)
        self.paynumber.setObjectName("paynumber")
        self.horizontalLayout.addWidget(self.paynumber)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.widget1 = QtWidgets.QWidget(Pay)
        self.widget1.setGeometry(QtCore.QRect(110, 200, 158, 25))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pay = QtWidgets.QPushButton(self.widget1)
        self.pay.setObjectName("pay")
        self.horizontalLayout_2.addWidget(self.pay)
        self.cancel = QtWidgets.QPushButton(self.widget1)
        self.cancel.setObjectName("cancel")
        self.horizontalLayout_2.addWidget(self.cancel)

        self.retranslateUi(Pay)
        QtCore.QMetaObject.connectSlotsByName(Pay)

    def retranslateUi(self, Pay):
        _translate = QtCore.QCoreApplication.translate
        Pay.setWindowTitle(_translate("Pay", "确认支付"))
        self.label.setText(_translate("Pay", "您需要支付"))
        self.label_2.setText(_translate("Pay", "元"))
        self.pay.setText(_translate("Pay", "支付"))
        self.cancel.setText(_translate("Pay", "取消"))


