# -*- coding: utf-8 -*-

# AQI implementation generated from reading ui file 'AQI.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AQI(object):
    def setupUi(self, AQI):
        AQI.setObjectName("AQI")
        AQI.resize(819, 621)
        self.verticalLayout = QtWidgets.QVBoxLayout(AQI)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(AQI)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.now_city = QtWidgets.QLineEdit(AQI)
        self.now_city.setObjectName("now_city")
        self.horizontalLayout_4.addWidget(self.now_city)
        self.label_6 = QtWidgets.QLabel(AQI)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.start1 = QtWidgets.QDateEdit(AQI)
        self.start1.setObjectName("start1")
        self.horizontalLayout_4.addWidget(self.start1)
        self.label_7 = QtWidgets.QLabel(AQI)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.end1 = QtWidgets.QDateEdit(AQI)
        self.end1.setObjectName("end1")
        self.horizontalLayout_4.addWidget(self.end1)
        self.now = QtWidgets.QPushButton(AQI)
        self.now.setObjectName("now")
        self.horizontalLayout_4.addWidget(self.now)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_8 = QtWidgets.QLabel(AQI)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8)
        self.city1 = QtWidgets.QLineEdit(AQI)
        self.city1.setObjectName("city1")
        self.horizontalLayout_5.addWidget(self.city1)
        self.label_11 = QtWidgets.QLabel(AQI)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_5.addWidget(self.label_11)
        self.city2 = QtWidgets.QLineEdit(AQI)
        self.city2.setObjectName("city2")
        self.horizontalLayout_5.addWidget(self.city2)
        self.label_9 = QtWidgets.QLabel(AQI)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_5.addWidget(self.label_9)
        self.start2 = QtWidgets.QDateEdit(AQI)
        self.start2.setObjectName("start2")
        self.horizontalLayout_5.addWidget(self.start2)
        self.label_10 = QtWidgets.QLabel(AQI)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_5.addWidget(self.label_10)
        self.end2 = QtWidgets.QDateEdit(AQI)
        self.end2.setObjectName("end2")
        self.horizontalLayout_5.addWidget(self.end2)
        self.compare = QtWidgets.QPushButton(AQI)
        self.compare.setObjectName("compare")
        self.horizontalLayout_5.addWidget(self.compare)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.tabWidget = QtWidgets.QTabWidget(AQI)
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
        self.webEngineView4 = QtWebEngineWidgets.QWebEngineView(self.NO2)
        self.webEngineView4.setGeometry(QtCore.QRect(9, 9, 702, 560))
        self.webEngineView4.setUrl(QtCore.QUrl("about:blank"))
        self.webEngineView4.setObjectName("webEngineView4")
        self.tabWidget.addTab(self.NO2, "")
        self.verticalLayout.addWidget(self.tabWidget)

        self.retranslateUi(AQI)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(AQI)

    def retranslateUi(self, AQI):
        _translate = QtCore.QCoreApplication.translate
        AQI.setWindowTitle(_translate("AQI", "AQI"))
        self.label_5.setText(_translate("AQI", "城市"))
        self.label_6.setText(_translate("AQI", "时间范围"))
        self.label_7.setText(_translate("AQI", "~"))
        self.now.setText(_translate("AQI", "监测曲线"))
        self.label_8.setText(_translate("AQI", "城市1"))
        self.label_11.setText(_translate("AQI", "城市2"))
        self.label_9.setText(_translate("AQI", "时间范围"))
        self.label_10.setText(_translate("AQI", "~"))
        self.compare.setText(_translate("AQI", "城市比较"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.AQI), _translate("AQI", "AQI"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.PM2), _translate("AQI", "PM2.5"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.PM10), _translate("AQI", "PM10"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.NO2), _translate("AQI", "NO2"))


from PyQt5 import QtWebEngineWidgets
