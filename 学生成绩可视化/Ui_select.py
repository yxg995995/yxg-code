# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'select.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_select(object):
    def setupUi(self, select):
        select.setObjectName("select")
        select.resize(336, 250)
        self.gridLayout = QtWidgets.QGridLayout(select)
        self.gridLayout.setObjectName("gridLayout")
        self.Chinese = QtWidgets.QPushButton(select)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Chinese.setFont(font)
        self.Chinese.setObjectName("Chinese")
        self.gridLayout.addWidget(self.Chinese, 0, 0, 1, 2)
        self.Math = QtWidgets.QPushButton(select)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Math.setFont(font)
        self.Math.setObjectName("Math")
        self.gridLayout.addWidget(self.Math, 0, 2, 1, 2)
        self.English = QtWidgets.QPushButton(select)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.English.setFont(font)
        self.English.setObjectName("English")
        self.gridLayout.addWidget(self.English, 0, 4, 1, 2)
        self.Physics = QtWidgets.QPushButton(select)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Physics.setFont(font)
        self.Physics.setObjectName("Physics")
        self.gridLayout.addWidget(self.Physics, 1, 0, 1, 1)
        self.Chemistry = QtWidgets.QPushButton(select)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Chemistry.setFont(font)
        self.Chemistry.setObjectName("Chemistry")
        self.gridLayout.addWidget(self.Chemistry, 1, 1, 1, 2)
        self.Biology = QtWidgets.QPushButton(select)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Biology.setFont(font)
        self.Biology.setObjectName("Biology")
        self.gridLayout.addWidget(self.Biology, 1, 3, 1, 2)
        self.comprehensive = QtWidgets.QPushButton(select)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.comprehensive.setFont(font)
        self.comprehensive.setObjectName("comprehensive")
        self.gridLayout.addWidget(self.comprehensive, 1, 5, 1, 1)

        self.retranslateUi(select)
        QtCore.QMetaObject.connectSlotsByName(select)

    def retranslateUi(self, select):
        _translate = QtCore.QCoreApplication.translate
        select.setWindowTitle(_translate("select", "Form"))
        self.Chinese.setText(_translate("select", "语文"))
        self.Math.setText(_translate("select", "数学"))
        self.English.setText(_translate("select", "英语"))
        self.Physics.setText(_translate("select", "物理"))
        self.Chemistry.setText(_translate("select", "化学"))
        self.Biology.setText(_translate("select", "生物"))
        self.comprehensive.setText(_translate("select", "综合"))


