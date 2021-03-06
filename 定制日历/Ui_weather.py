# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'weather.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Weather(object):
    def setupUi(self, Weather):
        Weather.setObjectName("Weather")
        Weather.resize(441, 492)
        Weather.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(Weather)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtWidgets.QWidget(Weather)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.weather = QtWidgets.QLabel(self.widget_2)
        self.weather.setText("")
        self.weather.setObjectName("weather")
        self.gridLayout.addWidget(self.weather, 5, 0, 1, 1)
        self.festival = QtWidgets.QLabel(self.widget_2)
        self.festival.setText("")
        self.festival.setObjectName("festival")
        self.gridLayout.addWidget(self.festival, 5, 3, 1, 1)
        self.pic = QtWidgets.QLabel(self.widget_2)
        self.pic.setText("")
        self.pic.setObjectName("pic")
        self.gridLayout.addWidget(self.pic, 0, 0, 5, 1)
        self.wind = QtWidgets.QLabel(self.widget_2)
        self.wind.setText("")
        self.wind.setObjectName("wind")
        self.gridLayout.addWidget(self.wind, 4, 1, 1, 1)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.widget_2)
        self.dateTimeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateTimeEdit.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.gridLayout.addWidget(self.dateTimeEdit, 3, 3, 1, 1)
        self.week = QtWidgets.QLabel(self.widget_2)
        self.week.setText("")
        self.week.setObjectName("week")
        self.gridLayout.addWidget(self.week, 5, 4, 1, 1)
        self.city = QtWidgets.QLineEdit(self.widget_2)
        self.city.setObjectName("city")
        self.gridLayout.addWidget(self.city, 0, 1, 1, 1)
        self.temp = QtWidgets.QLabel(self.widget_2)
        self.temp.setText("")
        self.temp.setObjectName("temp")
        self.gridLayout.addWidget(self.temp, 3, 1, 1, 1)
        self.month = QtWidgets.QLabel(self.widget_2)
        self.month.setText("")
        self.month.setObjectName("month")
        self.gridLayout.addWidget(self.month, 4, 4, 1, 1)
        self.font = QtWidgets.QPushButton(self.widget_2)
        self.font.setObjectName("font")
        self.gridLayout.addWidget(self.font, 3, 4, 1, 1)
        self.nongli = QtWidgets.QLabel(self.widget_2)
        self.nongli.setText("")
        self.nongli.setObjectName("nongli")
        self.gridLayout.addWidget(self.nongli, 4, 3, 1, 1)
        self.query = QtWidgets.QPushButton(self.widget_2)
        self.query.setObjectName("query")
        self.gridLayout.addWidget(self.query, 0, 3, 1, 1)
        self.color = QtWidgets.QPushButton(self.widget_2)
        self.color.setObjectName("color")
        self.gridLayout.addWidget(self.color, 0, 4, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/暂停.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(20, 20))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 5, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.verticalLayout.addWidget(self.widget_2)
        self.calendarWidget = QtWidgets.QCalendarWidget(Weather)
        self.calendarWidget.setEnabled(True)
        self.calendarWidget.setStyleSheet("font: 12pt \"Arial\";")
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setSelectionMode(QtWidgets.QCalendarWidget.SingleSelection)
        self.calendarWidget.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.ShortDayNames)
        self.calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.ISOWeekNumbers)
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout.addWidget(self.calendarWidget)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tip = QtWidgets.QLabel(Weather)
        self.tip.setText("")
        self.tip.setObjectName("tip")
        self.verticalLayout_2.addWidget(self.tip)
        self.groupBox = QtWidgets.QGroupBox(Weather)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.remember = QtWidgets.QTextEdit(self.groupBox)
        self.remember.setObjectName("remember")
        self.horizontalLayout.addWidget(self.remember)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(Weather)
        QtCore.QMetaObject.connectSlotsByName(Weather)

    def retranslateUi(self, Weather):
        _translate = QtCore.QCoreApplication.translate
        Weather.setWindowTitle(_translate("Weather", "Dialog"))
        self.dateTimeEdit.setDisplayFormat(_translate("Weather", "yyyy-MM-dd HH:mm:ss"))
        self.font.setText(_translate("Weather", "更换字体"))
        self.query.setText(_translate("Weather", "查询"))
        self.color.setText(_translate("Weather", "更换背景颜色"))
        self.groupBox.setTitle(_translate("Weather", "备忘录"))


