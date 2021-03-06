# -*- coding: utf-8 -*-

# monitor implementation generated from reading ui file 'now.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import datetime
class Ui_monitor(object):
    def setupUi(self, monitor):
        monitor.setObjectName("monitor")
        monitor.resize(819, 621)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(monitor)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.now = QtWidgets.QPushButton(monitor)
        self.now.setStyleSheet("background-color: rgb(48, 62, 255);")
        self.now.setObjectName("now")
        self.verticalLayout_2.addWidget(self.now)
        self.compare = QtWidgets.QPushButton(monitor)
        self.compare.setStyleSheet("background-color: rgb(53, 39, 255);")
        self.compare.setObjectName("compare")
        self.verticalLayout_2.addWidget(self.compare)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.widget = QtWidgets.QWidget(monitor)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.oneCity = QtWidgets.QHBoxLayout()
        self.oneCity.setObjectName("oneCity")
        self.label_5 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.oneCity.addWidget(self.label_5)
        self.now_city = QtWidgets.QLineEdit(self.widget)
        self.now_city.setObjectName("now_city")
        self.oneCity.addWidget(self.now_city)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.oneCity.addWidget(self.label_6)
        self.start = QtWidgets.QDateEdit(self.widget)
        self.start.setObjectName("start")
        self.oneCity.addWidget(self.start)
        self.label_7 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.oneCity.addWidget(self.label_7)
        self.end = QtWidgets.QDateEdit(self.widget)
        self.end.setObjectName("end")
        self.oneCity.addWidget(self.end)
        self.draw = QtWidgets.QPushButton(self.widget)
        self.draw.setObjectName("draw")
        self.oneCity.addWidget(self.draw)
        self.clear = QtWidgets.QPushButton(self.widget)
        self.clear.setObjectName("clear")
        self.oneCity.addWidget(self.clear)
        self.verticalLayout.addLayout(self.oneCity)
        self.tabWidget = QtWidgets.QTabWidget(self.widget)
        self.tabWidget.setObjectName("tabWidget")
        self.AQI = QtWidgets.QWidget()
        self.AQI.setObjectName("AQI")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.AQI)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.webEngineView1 = QtWebEngineWidgets.QWebEngineView(self.AQI)
        self.webEngineView1.setUrl(QtCore.QUrl("about:blank"))
        self.webEngineView1.setObjectName("webEngineView1")
        self.horizontalLayout.addWidget(self.webEngineView1)
        self.tabWidget.addTab(self.AQI, "")
        self.PM2 = QtWidgets.QWidget()
        self.PM2.setObjectName("PM2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.PM2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.webEngineView2 = QtWebEngineWidgets.QWebEngineView(self.PM2)
        self.webEngineView2.setUrl(QtCore.QUrl("about:blank"))
        self.webEngineView2.setObjectName("webEngineView2")
        self.horizontalLayout_2.addWidget(self.webEngineView2)
        self.tabWidget.addTab(self.PM2, "")
        self.PM10 = QtWidgets.QWidget()
        self.PM10.setObjectName("PM10")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.PM10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.webEngineView3 = QtWebEngineWidgets.QWebEngineView(self.PM10)
        self.webEngineView3.setUrl(QtCore.QUrl("about:blank"))
        self.webEngineView3.setObjectName("webEngineView3")
        self.horizontalLayout_3.addWidget(self.webEngineView3)
        self.tabWidget.addTab(self.PM10, "")
        self.NO2 = QtWidgets.QWidget()
        self.NO2.setObjectName("NO2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.NO2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.webEngineView4 = QtWebEngineWidgets.QWebEngineView(self.NO2)
        self.webEngineView4.setUrl(QtCore.QUrl("about:blank"))
        self.webEngineView4.setObjectName("webEngineView4")
        self.horizontalLayout_6.addWidget(self.webEngineView4)
        self.tabWidget.addTab(self.NO2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout_4.addWidget(self.widget)
        self.start.setDisplayFormat('yyyy-MM-dd')
        self.end.setDisplayFormat('yyyy-MM-dd')
        self.start.setDate(QDate.currentDate())
        self.end.setDate(QDate.currentDate())
        self.start.setMaximumDate(QDate.currentDate())
        self.end.setMaximumDate(QDate.currentDate())
        self.retranslateUi(monitor)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget.setTabEnabled(0,False)
        self.tabWidget.setTabEnabled(1,False)
        self.tabWidget.setTabEnabled(2,False)
        self.tabWidget.setTabEnabled(3,False)
        QtCore.QMetaObject.connectSlotsByName(monitor)

    def retranslateUi(self, monitor):
        _translate = QtCore.QCoreApplication.translate
        monitor.setWindowTitle(_translate("monitor", "monitor"))
        self.now.setText(_translate("monitor", "监测曲线"))
        self.compare.setText(_translate("monitor", "城市比较"))
        self.label_5.setText(_translate("monitor", "城市"))
        self.label_6.setText(_translate("monitor", "时间范围"))
        self.label_7.setText(_translate("monitor", "~"))
        self.draw.setText(_translate("monitor", "画图"))
        self.clear.setText(_translate("monitor", "清空"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.AQI), _translate("monitor", "AQI"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.PM2), _translate("monitor", "PM2.5"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.PM10), _translate("monitor", "PM10"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.NO2), _translate("monitor", "NO2"))


from PyQt5 import QtWebEngineWidgets
