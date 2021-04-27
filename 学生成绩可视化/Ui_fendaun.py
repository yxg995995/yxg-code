# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fenduan.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_fenduan(object):
    def setupUi(self, fenduan):
        fenduan.setObjectName("fenduan")
        fenduan.resize(760, 524)
        self.verticalLayout = QtWidgets.QVBoxLayout(fenduan)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(fenduan)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(self.splitter)
        self.label.setObjectName("label")
        self.Max = QtWidgets.QLineEdit(self.splitter)
        self.Max.setObjectName("Max")
        self.label_2 = QtWidgets.QLabel(self.splitter)
        self.label_2.setObjectName("label_2")
        self.Min = QtWidgets.QLineEdit(self.splitter)
        self.Min.setObjectName("Min")
        self.label_3 = QtWidgets.QLabel(self.splitter)
        self.label_3.setObjectName("label_3")
        self.distance = QtWidgets.QLineEdit(self.splitter)
        self.distance.setText("")
        self.distance.setObjectName("distance")
        self.fresh = QtWidgets.QPushButton(self.splitter)
        self.fresh.setObjectName("fresh")
        self.draw = QtWidgets.QPushButton(self.splitter)
        self.draw.setObjectName("draw")
        self.verticalLayout.addWidget(self.splitter)
        self.tabWidget = QtWidgets.QTabWidget(fenduan)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.webEngineView1 = QtWebEngineWidgets.QWebEngineView(self.tab)
        self.webEngineView1.setUrl(QtCore.QUrl("about:blank"))
        self.webEngineView1.setObjectName("webEngineView1")
        self.horizontalLayout.addWidget(self.webEngineView1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.webEngineView2 = QtWebEngineWidgets.QWebEngineView(self.tab_2)
        self.webEngineView2.setUrl(QtCore.QUrl("about:blank"))
        self.webEngineView2.setObjectName("webEngineView2")
        self.horizontalLayout_2.addWidget(self.webEngineView2)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.webEngineView3 = QtWebEngineWidgets.QWebEngineView(self.tab_3)
        self.webEngineView3.setUrl(QtCore.QUrl("about:blank"))
        self.webEngineView3.setObjectName("webEngineView3")
        self.horizontalLayout_3.addWidget(self.webEngineView3)
        self.tabWidget.addTab(self.tab_3, "")
        self.verticalLayout.addWidget(self.tabWidget)

        self.retranslateUi(fenduan)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(fenduan)

    def retranslateUi(self, fenduan):
        _translate = QtCore.QCoreApplication.translate
        fenduan.setWindowTitle(_translate("fenduan", "分段成绩界面"))
        self.label.setText(_translate("fenduan", "最高分"))
        self.label_2.setText(_translate("fenduan", "最低分"))
        self.label_3.setText(_translate("fenduan", "分段间隔"))
        self.fresh.setText(_translate("fenduan", "重置"))
        self.draw.setText(_translate("fenduan", "确定"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("fenduan", "直方图"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("fenduan", "饼图"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("fenduan", "表格"))


from PyQt5 import QtWebEngineWidgets
