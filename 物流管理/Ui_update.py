# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Up.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Update(object):
    def setupUi(self, Update):
        Update.setObjectName("Update")
        Update.resize(330, 267)
        self.update = QtWidgets.QPushButton(Update)
        self.update.setGeometry(QtCore.QRect(60, 220, 75, 23))
        self.update.setObjectName("update")
        self.cancel = QtWidgets.QPushButton(Update)
        self.cancel.setGeometry(QtCore.QRect(170, 220, 75, 23))
        self.cancel.setObjectName("cancel")
        self.widget = QtWidgets.QWidget(Update)
        self.widget.setGeometry(QtCore.QRect(50, 40, 231, 161))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.temp = QtWidgets.QLineEdit(self.widget)
        self.temp.setObjectName("temp")
        self.gridLayout.addWidget(self.temp, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.humidity = QtWidgets.QLineEdit(self.widget)
        self.humidity.setObjectName("humidity")
        self.gridLayout.addWidget(self.humidity, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.light = QtWidgets.QComboBox(self.widget)
        self.light.setObjectName("light")
        self.gridLayout.addWidget(self.light, 2, 1, 1, 1)

        self.retranslateUi(Update)
        QtCore.QMetaObject.connectSlotsByName(Update)

    def retranslateUi(self, Update):
        _translate = QtCore.QCoreApplication.translate
        Update.setWindowTitle(_translate("Update", "更改信息"))
        self.update.setText(_translate("Update", "更改"))
        self.cancel.setText(_translate("Update", "取消"))
        self.label.setText(_translate("Update", "温度"))
        self.label_2.setText(_translate("Update", "湿度"))
        self.label_3.setText(_translate("Update", "光照"))


