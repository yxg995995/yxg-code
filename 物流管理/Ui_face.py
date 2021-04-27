# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Face.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Face(object):
    def setupUi(self, Face):
        Face.setObjectName("Face")
        Face.resize(266, 251)
        self.gridLayout = QtWidgets.QGridLayout(Face)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Mine_btn = QtWidgets.QPushButton(Face)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Mine_btn.setFont(font)
        self.Mine_btn.setObjectName("Mine_btn")
        self.verticalLayout.addWidget(self.Mine_btn)
        self.history_btn = QtWidgets.QPushButton(Face)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.history_btn.setFont(font)
        self.history_btn.setObjectName("history_btn")
        self.verticalLayout.addWidget(self.history_btn)
        self.UnCheck_btn = QtWidgets.QPushButton(Face)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.UnCheck_btn.setFont(font)
        self.UnCheck_btn.setObjectName("UnCheck_btn")
        self.verticalLayout.addWidget(self.UnCheck_btn)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Face)
        QtCore.QMetaObject.connectSlotsByName(Face)

    def retranslateUi(self, Face):
        _translate = QtCore.QCoreApplication.translate
        Face.setWindowTitle(_translate("Face", "选择界面"))
        self.Mine_btn.setText(_translate("Face", "我的信息"))
        self.history_btn.setText(_translate("Face", "历史订单"))
        self.UnCheck_btn.setText(_translate("Face", "未验收订单"))


