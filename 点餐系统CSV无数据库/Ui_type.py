# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'orderingType.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

#选择功能界面
class Ui_Type(object):
    def setupUi(self, Type):
        Type.setObjectName("Type")
        Type.setEnabled(True)
        Type.resize(300, 236)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        Type.setFont(font)
        Type.setStyleSheet("")
        self.widget = QtWidgets.QWidget(Type)
        self.widget.setGeometry(QtCore.QRect(70, 50, 161, 121))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.order = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.order.setFont(font)
        self.order.setStyleSheet("")
        self.order.setObjectName("order")
        self.verticalLayout.addWidget(self.order)
        self.look = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.look.setFont(font)
        self.look.setStyleSheet("")
        self.look.setObjectName("look")
        self.verticalLayout.addWidget(self.look)
        self.look.raise_()
        self.order.raise_()

        self.retranslateUi(Type)
        QtCore.QMetaObject.connectSlotsByName(Type)

    def retranslateUi(self, Type):
        _translate = QtCore.QCoreApplication.translate
        Type.setWindowTitle(_translate("Type", "选择界面"))
        self.order.setText(_translate("Type", "我要点餐"))
        self.look.setText(_translate("Type", "我要看菜"))


