# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Air.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Air(object):
    def setupUi(self, Air):
        Air.setObjectName("Air")
        Air.resize(841, 620)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(Air)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.tabWidget = QtWidgets.QTabWidget(Air)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_20 = QtWidgets.QWidget()
        self.tab_20.setObjectName("tab_20")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.tab_20)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_20)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.auto_btn = QtWidgets.QPushButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.auto_btn.setFont(font)
        self.auto_btn.setStyleSheet("border-radius: 35px;  border: 2px groove gray;\n"
"background-color: rgb(0, 255, 255);\n"
"")
        self.auto_btn.setObjectName("auto_btn")
        self.verticalLayout_10.addWidget(self.auto_btn)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_16 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_17.addWidget(self.label_16)
        self.city51 = QtWidgets.QComboBox(self.groupBox_2)
        self.city51.setObjectName("city51")
        self.horizontalLayout_17.addWidget(self.city51)
        self.label_17 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_17.addWidget(self.label_17)
        self.start51 = QtWidgets.QDateEdit(self.groupBox_2)
        self.start51.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 2, 1), QtCore.QTime(0, 0, 0)))
        self.start51.setMinimumDate(QtCore.QDate(2021, 2, 1))
        self.start51.setObjectName("start51")
        self.horizontalLayout_17.addWidget(self.start51)
        self.label_18 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_17.addWidget(self.label_18)
        self.end51 = QtWidgets.QDateEdit(self.groupBox_2)
        self.end51.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 2, 1), QtCore.QTime(0, 0, 0)))
        self.end51.setMinimumDate(QtCore.QDate(2021, 2, 1))
        self.end51.setObjectName("end51")
        self.horizontalLayout_17.addWidget(self.end51)
        self.download = QtWidgets.QPushButton(self.groupBox_2)
        self.download.setObjectName("download")
        self.horizontalLayout_17.addWidget(self.download)
        self.verticalLayout_10.addLayout(self.horizontalLayout_17)
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(self.groupBox_2)
        self.webEngineView.setUrl(QtCore.QUrl("about:blank"))
        self.webEngineView.setObjectName("webEngineView")
        self.verticalLayout_10.addWidget(self.webEngineView)
        self.verticalLayout_12.addWidget(self.groupBox_2)
        self.tabWidget.addTab(self.tab_20, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.city1 = QtWidgets.QComboBox(self.tab)
        self.city1.setObjectName("city1")
        self.horizontalLayout.addWidget(self.city1)
        self.label_2 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.start1 = QtWidgets.QDateEdit(self.tab)
        self.start1.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 2, 1), QtCore.QTime(0, 0, 0)))
        self.start1.setMinimumDate(QtCore.QDate(2021, 2, 1))
        self.start1.setObjectName("start1")
        self.horizontalLayout.addWidget(self.start1)
        self.label_3 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.end1 = QtWidgets.QDateEdit(self.tab)
        self.end1.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 2, 1), QtCore.QTime(0, 0, 0)))
        self.end1.setMinimumDate(QtCore.QDate(2021, 2, 1))
        self.end1.setObjectName("end1")
        self.horizontalLayout.addWidget(self.end1)
        self.clear11 = QtWidgets.QPushButton(self.tab)
        self.clear11.setObjectName("clear11")
        self.horizontalLayout.addWidget(self.clear11)
        self.draw11 = QtWidgets.QPushButton(self.tab)
        self.draw11.setObjectName("draw11")
        self.horizontalLayout.addWidget(self.draw11)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.webEngineView11 = QtWebEngineWidgets.QWebEngineView(self.tab_5)
        self.webEngineView11.setUrl(QtCore.QUrl("about:blank"))
        self.webEngineView11.setObjectName("webEngineView11")
        self.horizontalLayout_2.addWidget(self.webEngineView11)
        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab_6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.webEngineView12 = QtWebEngineWidgets.QWebEngineView(self.tab_6)
        self.webEngineView12.setUrl(QtCore.QUrl("about:blank"))
        self.webEngineView12.setObjectName("webEngineView12")
        self.horizontalLayout_3.addWidget(self.webEngineView12)
        self.tabWidget_2.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tab_7)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.webEngineView13 = QtWebEngineWidgets.QWebEngineView(self.tab_7)
        self.webEngineView13.setUrl(QtCore.QUrl("about:blank"))
        self.webEngineView13.setObjectName("webEngineView13")
        self.horizontalLayout_4.addWidget(self.webEngineView13)
        self.tabWidget_2.addTab(self.tab_7, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tab_8)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.webEngineView14 = QtWebEngineWidgets.QWebEngineView(self.tab_8)
        self.webEngineView14.setUrl(QtCore.QUrl("about:blank"))
        self.webEngineView14.setObjectName("webEngineView14")
        self.horizontalLayout_5.addWidget(self.webEngineView14)
        self.tabWidget_2.addTab(self.tab_8, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.tab_9)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.webEngineView15 = QtWebEngineWidgets.QWebEngineView(self.tab_9)
        self.webEngineView15.setUrl(QtCore.QUrl("about:blank"))
        self.webEngineView15.setObjectName("webEngineView15")
        self.horizontalLayout_6.addWidget(self.webEngineView15)
        self.tabWidget_2.addTab(self.tab_9, "")
        self.verticalLayout.addWidget(self.tabWidget_2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_12.addWidget(self.label_4)
        self.city21 = QtWidgets.QComboBox(self.tab_2)
        self.city21.setObjectName("city21")
        self.horizontalLayout_12.addWidget(self.city21)
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_12.addWidget(self.label_7)
        self.city22 = QtWidgets.QComboBox(self.tab_2)
        self.city22.setObjectName("city22")
        self.horizontalLayout_12.addWidget(self.city22)
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_12.addWidget(self.label_5)
        self.start2 = QtWidgets.QDateEdit(self.tab_2)
        self.start2.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 2, 1), QtCore.QTime(0, 0, 0)))
        self.start2.setMinimumDate(QtCore.QDate(2021, 2, 1))
        self.start2.setObjectName("start2")
        self.horizontalLayout_12.addWidget(self.start2)
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_12.addWidget(self.label_6)
        self.end2 = QtWidgets.QDateEdit(self.tab_2)
        self.end2.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 2, 1), QtCore.QTime(0, 0, 0)))
        self.end2.setMinimumDate(QtCore.QDate(2021, 2, 1))
        self.end2.setObjectName("end2")
        self.horizontalLayout_12.addWidget(self.end2)
        self.clear21 = QtWidgets.QPushButton(self.tab_2)
        self.clear21.setObjectName("clear21")
        self.horizontalLayout_12.addWidget(self.clear21)
        self.draw22 = QtWidgets.QPushButton(self.tab_2)
        self.draw22.setObjectName("draw22")
        self.horizontalLayout_12.addWidget(self.draw22)
        self.verticalLayout_2.addLayout(self.horizontalLayout_12)
        self.tabWidget_3 = QtWidgets.QTabWidget(self.tab_2)
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.tab_10)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.webEngineView21 = QtWebEngineWidgets.QWebEngineView(self.tab_10)
        self.webEngineView21.setUrl(QtCore.QUrl("about:blank"))
        self.webEngineView21.setObjectName("webEngineView21")
        self.horizontalLayout_7.addWidget(self.webEngineView21)
        self.tabWidget_3.addTab(self.tab_10, "")
        self.tab_11 = QtWidgets.QWidget()
        self.tab_11.setObjectName("tab_11")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.tab_11)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.webEngineView22 = QtWebEngineWidgets.QWebEngineView(self.tab_11)
        self.webEngineView22.setUrl(QtCore.QUrl("about:blank"))
        self.webEngineView22.setObjectName("webEngineView22")
        self.horizontalLayout_8.addWidget(self.webEngineView22)
        self.tabWidget_3.addTab(self.tab_11, "")
        self.tab_12 = QtWidgets.QWidget()
        self.tab_12.setObjectName("tab_12")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.tab_12)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.webEngineView23 = QtWebEngineWidgets.QWebEngineView(self.tab_12)
        self.webEngineView23.setUrl(QtCore.QUrl("about:blank"))
        self.webEngineView23.setObjectName("webEngineView23")
        self.horizontalLayout_9.addWidget(self.webEngineView23)
        self.tabWidget_3.addTab(self.tab_12, "")
        self.tab_13 = QtWidgets.QWidget()
        self.tab_13.setObjectName("tab_13")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.tab_13)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.webEngineView24 = QtWebEngineWidgets.QWebEngineView(self.tab_13)
        self.webEngineView24.setUrl(QtCore.QUrl("about:blank"))
        self.webEngineView24.setObjectName("webEngineView24")
        self.horizontalLayout_10.addWidget(self.webEngineView24)
        self.tabWidget_3.addTab(self.tab_13, "")
        self.tab_14 = QtWidgets.QWidget()
        self.tab_14.setObjectName("tab_14")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.tab_14)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.webEngineView25 = QtWebEngineWidgets.QWebEngineView(self.tab_14)
        self.webEngineView25.setUrl(QtCore.QUrl("about:blank"))
        self.webEngineView25.setObjectName("webEngineView25")
        self.horizontalLayout_11.addWidget(self.webEngineView25)
        self.tabWidget_3.addTab(self.tab_14, "")
        self.verticalLayout_2.addWidget(self.tabWidget_3)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_14.addWidget(self.label_9)
        self.start3 = QtWidgets.QDateEdit(self.tab_3)
        self.start3.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 2, 1), QtCore.QTime(0, 0, 0)))
        self.start3.setMinimumDate(QtCore.QDate(2021, 2, 1))
        self.start3.setObjectName("start3")
        self.horizontalLayout_14.addWidget(self.start3)
        self.clear31 = QtWidgets.QPushButton(self.tab_3)
        self.clear31.setObjectName("clear31")
        self.horizontalLayout_14.addWidget(self.clear31)
        self.draw31 = QtWidgets.QPushButton(self.tab_3)
        self.draw31.setObjectName("draw31")
        self.horizontalLayout_14.addWidget(self.draw31)
        self.verticalLayout_3.addLayout(self.horizontalLayout_14)
        self.tabWidget_4 = QtWidgets.QTabWidget(self.tab_3)
        self.tabWidget_4.setObjectName("tabWidget_4")
        self.tab_15 = QtWidgets.QWidget()
        self.tab_15.setObjectName("tab_15")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.tab_15)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.webEngineView31 = QtWebEngineWidgets.QWebEngineView(self.tab_15)
        self.webEngineView31.setUrl(QtCore.QUrl("about:blank"))
        self.webEngineView31.setObjectName("webEngineView31")
        self.horizontalLayout_13.addWidget(self.webEngineView31)
        self.tabWidget_4.addTab(self.tab_15, "")
        self.verticalLayout_3.addWidget(self.tabWidget_4)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tabWidget_5 = QtWidgets.QTabWidget(self.tab_4)
        self.tabWidget_5.setObjectName("tabWidget_5")
        self.tab_16 = QtWidgets.QWidget()
        self.tab_16.setObjectName("tab_16")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_16)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_8 = QtWidgets.QLabel(self.tab_16)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_15.addWidget(self.label_8)
        self.city31 = QtWidgets.QComboBox(self.tab_16)
        self.city31.setObjectName("city31")
        self.horizontalLayout_15.addWidget(self.city31)
        self.label_10 = QtWidgets.QLabel(self.tab_16)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_15.addWidget(self.label_10)
        self.start41 = QtWidgets.QDateEdit(self.tab_16)
        self.start41.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 2, 1), QtCore.QTime(0, 0, 0)))
        self.start41.setMaximumDate(QtCore.QDate(7777, 7, 1))
        self.start41.setMinimumDate(QtCore.QDate(2021, 2, 1))
        self.start41.setObjectName("start41")
        self.horizontalLayout_15.addWidget(self.start41)
        self.label_11 = QtWidgets.QLabel(self.tab_16)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_15.addWidget(self.label_11)
        self.end41 = QtWidgets.QDateEdit(self.tab_16)
        self.end41.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 2, 1), QtCore.QTime(0, 0, 0)))
        self.end41.setMinimumDate(QtCore.QDate(2021, 2, 1))
        self.end41.setObjectName("end41")
        self.horizontalLayout_15.addWidget(self.end41)
        self.feature = QtWidgets.QComboBox(self.tab_16)
        self.feature.setObjectName("feature")
        self.feature.addItem("")
        self.feature.addItem("")
        self.feature.addItem("")
        self.feature.addItem("")
        self.feature.addItem("")
        self.horizontalLayout_15.addWidget(self.feature)
        self.label_12 = QtWidgets.QLabel(self.tab_16)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_15.addWidget(self.label_12)
        self.q = QtWidgets.QLineEdit(self.tab_16)
        self.q.setObjectName("q")
        self.horizontalLayout_15.addWidget(self.q)
        self.clear41 = QtWidgets.QPushButton(self.tab_16)
        self.clear41.setObjectName("clear41")
        self.horizontalLayout_15.addWidget(self.clear41)
        self.draw41 = QtWidgets.QPushButton(self.tab_16)
        self.draw41.setObjectName("draw41")
        self.horizontalLayout_15.addWidget(self.draw41)
        self.verticalLayout_6.addLayout(self.horizontalLayout_15)
        self.tabWidget_6 = QtWidgets.QTabWidget(self.tab_16)
        self.tabWidget_6.setObjectName("tabWidget_6")
        self.tab_18 = QtWidgets.QWidget()
        self.tab_18.setObjectName("tab_18")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_18)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.webEngineView41 = QtWebEngineWidgets.QWebEngineView(self.tab_18)
        self.webEngineView41.setUrl(QtCore.QUrl("about:blank"))
        self.webEngineView41.setObjectName("webEngineView41")
        self.verticalLayout_5.addWidget(self.webEngineView41)
        self.tabWidget_6.addTab(self.tab_18, "")
        self.verticalLayout_6.addWidget(self.tabWidget_6)
        self.tabWidget_5.addTab(self.tab_16, "")
        self.tab_17 = QtWidgets.QWidget()
        self.tab_17.setObjectName("tab_17")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab_17)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_13 = QtWidgets.QLabel(self.tab_17)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_16.addWidget(self.label_13)
        self.city32 = QtWidgets.QComboBox(self.tab_17)
        self.city32.setObjectName("city32")
        self.horizontalLayout_16.addWidget(self.city32)
        self.label_14 = QtWidgets.QLabel(self.tab_17)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_16.addWidget(self.label_14)
        self.start42 = QtWidgets.QDateEdit(self.tab_17)
        self.start42.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 2, 1), QtCore.QTime(0, 0, 0)))
        self.start42.setMinimumDate(QtCore.QDate(2021, 2, 1))
        self.start42.setObjectName("start42")
        self.horizontalLayout_16.addWidget(self.start42)
        self.label_15 = QtWidgets.QLabel(self.tab_17)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_16.addWidget(self.label_15)
        self.end42 = QtWidgets.QDateEdit(self.tab_17)
        self.end42.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 2, 1), QtCore.QTime(0, 0, 0)))
        self.end42.setMinimumDate(QtCore.QDate(2021, 2, 1))
        self.end42.setObjectName("end42")
        self.horizontalLayout_16.addWidget(self.end42)
        self.clear42 = QtWidgets.QPushButton(self.tab_17)
        self.clear42.setObjectName("clear42")
        self.horizontalLayout_16.addWidget(self.clear42)
        self.draw42 = QtWidgets.QPushButton(self.tab_17)
        self.draw42.setObjectName("draw42")
        self.horizontalLayout_16.addWidget(self.draw42)
        self.verticalLayout_8.addLayout(self.horizontalLayout_16)
        self.tabWidget_7 = QtWidgets.QTabWidget(self.tab_17)
        self.tabWidget_7.setObjectName("tabWidget_7")
        self.tab_19 = QtWidgets.QWidget()
        self.tab_19.setObjectName("tab_19")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab_19)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.webEngineView42 = QtWebEngineWidgets.QWebEngineView(self.tab_19)
        self.webEngineView42.setUrl(QtCore.QUrl("about:blank"))
        self.webEngineView42.setObjectName("webEngineView42")
        self.verticalLayout_7.addWidget(self.webEngineView42)
        self.tabWidget_7.addTab(self.tab_19, "")
        self.verticalLayout_8.addWidget(self.tabWidget_7)
        self.tabWidget_5.addTab(self.tab_17, "")
        self.verticalLayout_4.addWidget(self.tabWidget_5)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_21 = QtWidgets.QWidget()
        self.tab_21.setObjectName("tab_21")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.tab_21)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.textEdit = QtWidgets.QTextEdit(self.tab_21)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_11.addWidget(self.textEdit)
        self.tabWidget.addTab(self.tab_21, "")
        self.verticalLayout_9.addWidget(self.tabWidget)

        self.retranslateUi(Air)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        self.tabWidget_4.setCurrentIndex(0)
        self.tabWidget_5.setCurrentIndex(0)
        self.tabWidget_6.setCurrentIndex(0)
        self.tabWidget_7.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Air)

    def retranslateUi(self, Air):
        _translate = QtCore.QCoreApplication.translate
        Air.setWindowTitle(_translate("Air", "空气质量"))
        self.auto_btn.setText(_translate("Air", "自动采集"))
        self.label_16.setText(_translate("Air", "城市名"))
        self.label_17.setText(_translate("Air", "起始时间"))
        self.start51.setDisplayFormat(_translate("Air", "yyyy-MM-dd"))
        self.label_18.setText(_translate("Air", "终止时间"))
        self.end51.setDisplayFormat(_translate("Air", "yyyy-MM-dd"))
        self.download.setText(_translate("Air", "手动采集"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_20), _translate("Air", "数据采集"))
        self.label.setText(_translate("Air", "城市名"))
        self.label_2.setText(_translate("Air", "起始时间"))
        self.start1.setDisplayFormat(_translate("Air", "yyyy-MM-dd"))
        self.label_3.setText(_translate("Air", "终止时间"))
        self.end1.setDisplayFormat(_translate("Air", "yyyy-MM-dd"))
        self.clear11.setText(_translate("Air", "重置"))
        self.draw11.setText(_translate("Air", "查询"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("Air", "AQI"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), _translate("Air", "PM2.5"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), _translate("Air", "PM10"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), _translate("Air", "SO2"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_9), _translate("Air", "NO2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Air", "城市查询"))
        self.label_4.setText(_translate("Air", "城市1"))
        self.label_7.setText(_translate("Air", "城市2"))
        self.label_5.setText(_translate("Air", "起始时间"))
        self.start2.setDisplayFormat(_translate("Air", "yyyy-MM-dd"))
        self.label_6.setText(_translate("Air", "终止时间"))
        self.end2.setDisplayFormat(_translate("Air", "yyyy-MM-dd"))
        self.clear21.setText(_translate("Air", "重置"))
        self.draw22.setText(_translate("Air", "查询"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_10), _translate("Air", "AQI"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_11), _translate("Air", "PM2.5"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_12), _translate("Air", "PM10"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_13), _translate("Air", "SO2"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_14), _translate("Air", "NO2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Air", "城市比较"))
        self.label_9.setText(_translate("Air", "时间"))
        self.start3.setDisplayFormat(_translate("Air", "yyyy-MM-dd"))
        self.clear31.setText(_translate("Air", "重置"))
        self.draw31.setText(_translate("Air", "查询"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_15), _translate("Air", "指标数据地图"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Air", "城市监控"))
        self.label_8.setText(_translate("Air", "城市名"))
        self.label_10.setText(_translate("Air", "起始时间"))
        self.start41.setDisplayFormat(_translate("Air", "yyyy-MM-dd"))
        self.label_11.setText(_translate("Air", "终止时间"))
        self.end41.setDisplayFormat(_translate("Air", "yyyy-MM-dd"))
        self.feature.setItemText(0, _translate("Air", "AQI"))
        self.feature.setItemText(1, _translate("Air", "PM2.5"))
        self.feature.setItemText(2, _translate("Air", "PM10"))
        self.feature.setItemText(3, _translate("Air", "SO2"))
        self.feature.setItemText(4, _translate("Air", "NO2"))
        self.label_12.setText(_translate("Air", "阈值"))
        self.clear41.setText(_translate("Air", "重置"))
        self.draw41.setText(_translate("Air", "查询"))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_18), _translate("Air", "表格图"))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_16), _translate("Air", "指标分析"))
        self.label_13.setText(_translate("Air", "城市名"))
        self.label_14.setText(_translate("Air", "起始时间"))
        self.start42.setDisplayFormat(_translate("Air", "yyyy-MM-dd"))
        self.label_15.setText(_translate("Air", "终止时间"))
        self.end42.setDisplayFormat(_translate("Air", "yyyy-MM-dd"))
        self.clear42.setText(_translate("Air", "重置"))
        self.draw42.setText(_translate("Air", "查询"))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_19), _translate("Air", "柱状图"))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_17), _translate("Air", "空气质量分析"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Air", "数据分析"))
        self.textEdit.setHtml(_translate("Air", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\"> 空气质量（air quality）的好坏反映了空气污染程度，它是依据空气中污染物浓度的高低来判断的。空气污染是一个复杂的现象，在特定时间和地点空气污染物浓度受到许多因素影响。来自固定和流动污染源的人为污染物排放大小是影响空气质量的最主要因素之一，其中包括车辆、船舶、飞机的尾气、工业企业生产排放、居民生活和取暖、垃圾焚烧等。城市的发展密度、地形地貌和气象等也是影响空气质量的重要因素。<br /> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">空气质量指数（Air Quality Index，简称AQI）是定量描述空气质量状况的无量纲指数，针对单项污染物的还规定了空气质量分指数，参与空气质量评价的主要污染物为细颗粒物、可吸入颗粒物、二氧化硫、二氧化氮、臭氧、一氧化碳等六项。</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_21), _translate("Air", "系统说明"))


from PyQt5 import QtWebEngineWidgets
