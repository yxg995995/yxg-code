# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fendang.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_fendang(object):
    def setupUi(self, fendang):
        fendang.setObjectName("fendang")
        fendang.resize(736, 546)
        self.verticalLayout = QtWidgets.QVBoxLayout(fendang)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(fendang)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.one = QtWidgets.QLineEdit(fendang)
        self.one.setObjectName("one")
        self.horizontalLayout.addWidget(self.one)
        self.label_2 = QtWidgets.QLabel(fendang)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.two = QtWidgets.QLineEdit(fendang)
        self.two.setObjectName("two")
        self.horizontalLayout.addWidget(self.two)
        self.label_3 = QtWidgets.QLabel(fendang)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.three = QtWidgets.QLineEdit(fendang)
        self.three.setObjectName("three")
        self.horizontalLayout.addWidget(self.three)
        self.clear = QtWidgets.QPushButton(fendang)
        self.clear.setObjectName("clear")
        self.horizontalLayout.addWidget(self.clear)
        self.draw = QtWidgets.QPushButton(fendang)
        self.draw.setObjectName("draw")
        self.horizontalLayout.addWidget(self.draw)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(fendang)
        self.webEngineView.setUrl(QtCore.QUrl("about:blank"))
        self.webEngineView.setObjectName("webEngineView")
        self.verticalLayout.addWidget(self.webEngineView)

        self.retranslateUi(fendang)
        QtCore.QMetaObject.connectSlotsByName(fendang)

    def retranslateUi(self, fendang):
        _translate = QtCore.QCoreApplication.translate
        fendang.setWindowTitle(_translate("fendang", "分档达线分析"))
        self.label.setText(_translate("fendang", "一档线"))
        self.label_2.setText(_translate("fendang", "二档线"))
        self.label_3.setText(_translate("fendang", "三档线"))
        self.clear.setText(_translate("fendang", "重置"))
        self.draw.setText(_translate("fendang", "确定"))


from PyQt5 import QtWebEngineWidgets
