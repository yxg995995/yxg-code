# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Stock.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Stock(object):
    def setupUi(self, Stock):
        Stock.setObjectName("Stock")
        Stock.setEnabled(True)
        Stock.resize(1021, 659)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Stock.sizePolicy().hasHeightForWidth())
        Stock.setSizePolicy(sizePolicy)
        Stock.setMinimumSize(QtCore.QSize(850, 600))
        Stock.setStyleSheet("background-color: rgb(255, 206, 233);")
        #窗口总布局 
        self.verticalLayout = QtWidgets.QVBoxLayout(Stock)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        #请输入股票组件
        self.label = QtWidgets.QLabel(Stock)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        #将组件添加入布局中
        self.horizontalLayout.addWidget(self.label)
        #输入股票id的输入框
        self.stock_id = QtWidgets.QLineEdit(Stock)
        self.stock_id.setObjectName("stock_id")
        #将组件添加入布局中
        self.horizontalLayout.addWidget(self.stock_id)
        #开始时间
        self.label_2 = QtWidgets.QLabel(Stock)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        #输入起始时间输入框
        self.start = QtWidgets.QLineEdit(Stock)
        self.start.setObjectName("start")
        self.horizontalLayout.addWidget(self.start)
        #end时间组件
        self.label_3 = QtWidgets.QLabel(Stock)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        #end时间输入框
        self.end = QtWidgets.QLineEdit(Stock)
        self.end.setObjectName("end")
        self.horizontalLayout.addWidget(self.end)
        #画图按钮
        self.draw = QtWidgets.QPushButton(Stock)
        self.draw.setObjectName("draw")
        self.horizontalLayout.addWidget(self.draw)
        #清空按钮
        self.clear = QtWidgets.QPushButton(Stock)
        self.clear.setObjectName("clear")
        self.horizontalLayout.addWidget(self.clear)
        #日K线按钮
        self.dayK = QtWidgets.QPushButton(Stock)
        self.dayK.setObjectName("dayK")
        self.horizontalLayout.addWidget(self.dayK)
        #周k线按钮
        self.weekK = QtWidgets.QPushButton(Stock)
        self.weekK.setObjectName("weekK")
        self.horizontalLayout.addWidget(self.weekK)
        #月K线按钮
        self.monthK = QtWidgets.QPushButton(Stock)
        self.monthK.setObjectName("monthK")
        self.horizontalLayout.addWidget(self.monthK)
        self.verticalLayout.addLayout(self.horizontalLayout)
        #加载图片的组件
        self.frame = QtWidgets.QFrame(Stock)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(self.frame)
        self.webEngineView.setObjectName("webEngineView")
        self.gridLayout.addWidget(self.webEngineView, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        #输入框提示
        self.start.setPlaceholderText('类似20001212')
        self.end.setPlaceholderText('同起始时间一样')
        #设置按钮不可点击
        self.dayK.setEnabled(False)
        self.weekK.setEnabled(False)
        self.monthK.setEnabled(False)
        
        #按钮点击后会触发的事件
        self.retranslateUi(Stock)
        #清空输入框的内容
        self.clear.clicked.connect(self.stock_id.clear)
        self.clear.clicked.connect(self.start.clear)
        self.clear.clicked.connect(self.end.clear)
        QtCore.QMetaObject.connectSlotsByName(Stock)
    
    #翻译或者是重新设置名字
    def retranslateUi(self, Stock):
        _translate = QtCore.QCoreApplication.translate
        Stock.setWindowTitle(_translate("Stock", "空气质量详解图"))
        self.label.setText(_translate("Stock", "输入股票代码"))
        self.label_2.setText(_translate("Stock", "起始时间"))
        self.label_3.setText(_translate("Stock", "终止时间"))
        self.draw.setText(_translate("Stock", "画图"))
        self.clear.setText(_translate("Stock", "清空"))
        self.dayK.setText(_translate("Stock", "日K线"))
        self.weekK.setText(_translate("Stock", "周K线"))
        self.monthK.setText(_translate("Stock", "月K线"))


from PyQt5 import QtWebEngineWidgets
