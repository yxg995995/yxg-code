# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'four.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_four(object):
    def setupUi(self, four):
        four.setObjectName("four")
        four.resize(738, 557)
        self.verticalLayout = QtWidgets.QVBoxLayout(four)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(four)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.excellent = QtWidgets.QLCDNumber(four)
        self.excellent.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.excellent.setProperty("value", 0.0)
        self.excellent.setObjectName("excellent")
        self.horizontalLayout.addWidget(self.excellent)
        self.label_5 = QtWidgets.QLabel(four)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.label_2 = QtWidgets.QLabel(four)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.fine = QtWidgets.QLCDNumber(four)
        self.fine.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.fine.setObjectName("fine")
        self.horizontalLayout.addWidget(self.fine)
        self.label_6 = QtWidgets.QLabel(four)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.label_3 = QtWidgets.QLabel(four)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.Pass = QtWidgets.QLCDNumber(four)
        self.Pass.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.Pass.setObjectName("Pass")
        self.horizontalLayout.addWidget(self.Pass)
        self.label_7 = QtWidgets.QLabel(four)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.label_4 = QtWidgets.QLabel(four)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.low = QtWidgets.QLCDNumber(four)
        self.low.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.low.setObjectName("low")
        self.horizontalLayout.addWidget(self.low)
        self.label_8 = QtWidgets.QLabel(four)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.clear = QtWidgets.QPushButton(four)
        self.clear.setObjectName("clear")
        self.horizontalLayout.addWidget(self.clear)
        self.draw = QtWidgets.QPushButton(four)
        self.draw.setObjectName("draw")
        self.horizontalLayout.addWidget(self.draw)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tabWidget = QtWidgets.QTabWidget(four)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(self.tab)
        self.webEngineView.setUrl(QtCore.QUrl("about:blank"))
        self.webEngineView.setObjectName("webEngineView")
        self.horizontalLayout_2.addWidget(self.webEngineView)
        self.tabWidget.addTab(self.tab, "")
        self.verticalLayout.addWidget(self.tabWidget)

        self.retranslateUi(four)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(four)

    def retranslateUi(self, four):
        _translate = QtCore.QCoreApplication.translate
        four.setWindowTitle(_translate("four", "四率一分界面"))
        self.label.setText(_translate("four", "优秀率"))
        self.label_5.setText(_translate("four", "%"))
        self.label_2.setText(_translate("four", "良好率"))
        self.label_6.setText(_translate("four", "%"))
        self.label_3.setText(_translate("four", "及格率"))
        self.label_7.setText(_translate("four", "%"))
        self.label_4.setText(_translate("four", "低分率"))
        self.label_8.setText(_translate("four", "%"))
        self.clear.setText(_translate("four", "重置"))
        self.draw.setText(_translate("four", "确定"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("four", "组合图"))


from PyQt5 import QtWebEngineWidgets
