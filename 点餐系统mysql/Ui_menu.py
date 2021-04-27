# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from DataBase import DataBase
from Ui_select import Ui_have_select
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
class Ui_Menu(object):
    def setupUi(self, Menu,R=[0,0,0,0],S=[0,0,0,0,0],Pizza=[0,0,0,0,0,0],P=[0,0,0,0,0],D=[0,0,0,0,0,0]):
        Menu.setObjectName("Menu")
        Menu.resize(808, 554)
        self.layoutWidget = QtWidgets.QWidget(Menu)
        self.layoutWidget.setGeometry(QtCore.QRect(600, 490, 158, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.order_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.order_btn.setObjectName("order_btn")
        self.horizontalLayout_7.addWidget(self.order_btn)
        self.over_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.over_btn.setObjectName("over_btn")
        self.horizontalLayout_7.addWidget(self.over_btn)
        
        self.layoutWidget_2 = QtWidgets.QWidget(Menu)
        self.layoutWidget_2.setGeometry(QtCore.QRect(360, 20, 201, 215))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.pic2 = QtWidgets.QLabel(self.layoutWidget_2)
        self.pic2.setText("")
        self.pic2.setPixmap(QtGui.QPixmap("./source/面饭/面饭5.jpg"))
        self.pic2.setObjectName("pic2")
        self.verticalLayout_5.addWidget(self.pic2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.name2 = QtWidgets.QLabel(self.layoutWidget_2)
        self.name2.setObjectName("name2")
        self.verticalLayout_3.addWidget(self.name2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.delete2 = QtWidgets.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.delete2.setFont(font)
        self.delete2.setObjectName("delete2")
        self.horizontalLayout_2.addWidget(self.delete2)
        self.number2 = QtWidgets.QLCDNumber(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.number2.setFont(font)
        self.number2.setDigitCount(5)
        self.number2.setObjectName("number2")
        self.horizontalLayout_2.addWidget(self.number2)
        self.add2 = QtWidgets.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.add2.setFont(font)
        self.add2.setObjectName("add2")
        self.horizontalLayout_2.addWidget(self.add2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.layoutWidget_3 = QtWidgets.QWidget(Menu)
        self.layoutWidget_3.setGeometry(QtCore.QRect(140, 250, 201, 215))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.pic4 = QtWidgets.QLabel(self.layoutWidget_3)
        self.pic4.setText("")
        self.pic4.setPixmap(QtGui.QPixmap("./source/面饭/面饭8.jpg"))
        self.pic4.setObjectName("pic4")
        self.verticalLayout_7.addWidget(self.pic4)
        self.name4 = QtWidgets.QLabel(self.layoutWidget_3)
        self.name4.setObjectName("name4")
        self.verticalLayout_7.addWidget(self.name4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.delete4 = QtWidgets.QPushButton(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.delete4.setFont(font)
        self.delete4.setObjectName("delete4")
        self.horizontalLayout_3.addWidget(self.delete4)
        self.number4 = QtWidgets.QLCDNumber(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.number4.setFont(font)
        self.number4.setDigitCount(5)
        self.number4.setObjectName("number4")
        self.horizontalLayout_3.addWidget(self.number4)
        self.add4 = QtWidgets.QPushButton(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.add4.setFont(font)
        self.add4.setObjectName("add5")
        self.horizontalLayout_3.addWidget(self.add4)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.verticalLayout_6.addLayout(self.verticalLayout_7)
        self.layoutWidget_4 = QtWidgets.QWidget(Menu)
        self.layoutWidget_4.setGeometry(QtCore.QRect(360, 250, 201, 215))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.pic5 = QtWidgets.QLabel(self.layoutWidget_4)
        self.pic5.setText("")
        self.pic5.setPixmap(QtGui.QPixmap(""))
        self.pic5.setObjectName("pic5")
        self.verticalLayout_9.addWidget(self.pic5)
        self.name5 = QtWidgets.QLabel(self.layoutWidget_4)
        self.name5.setObjectName("name5")
        self.verticalLayout_9.addWidget(self.name5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.delete5 = QtWidgets.QPushButton(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.delete5.setFont(font)
        self.delete5.setObjectName("delete5")
        self.horizontalLayout_4.addWidget(self.delete5)
        self.number5 = QtWidgets.QLCDNumber(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.number5.setFont(font)
        self.number5.setDigitCount(5)
        self.number5.setObjectName("number5")
        self.horizontalLayout_4.addWidget(self.number5)
        self.add5 = QtWidgets.QPushButton(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.add5.setFont(font)
        self.add5.setObjectName("add5")
        self.horizontalLayout_4.addWidget(self.add5)
        self.verticalLayout_9.addLayout(self.horizontalLayout_4)
        self.verticalLayout_8.addLayout(self.verticalLayout_9)
        self.layoutWidget_5 = QtWidgets.QWidget(Menu)
        self.layoutWidget_5.setGeometry(QtCore.QRect(570, 20, 201, 215))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.layoutWidget_5)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.pic3 = QtWidgets.QLabel(self.layoutWidget_5)
        self.pic3.setText("")
        self.pic3.setPixmap(QtGui.QPixmap("./source/面饭/面饭6.jpg"))
        self.pic3.setObjectName("pic3")
        self.verticalLayout_10.addWidget(self.pic3)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.name3 = QtWidgets.QLabel(self.layoutWidget_5)
        self.name3.setObjectName("name3")
        self.verticalLayout_11.addWidget(self.name3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.delete3 = QtWidgets.QPushButton(self.layoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.delete3.setFont(font)
        self.delete3.setObjectName("delete3")
        self.horizontalLayout_5.addWidget(self.delete3)
        self.number3 = QtWidgets.QLCDNumber(self.layoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.number3.setFont(font)
        self.number3.setDigitCount(5)
        self.number3.setObjectName("number3")
        self.horizontalLayout_5.addWidget(self.number3)
        self.add3 = QtWidgets.QPushButton(self.layoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.add3.setFont(font)
        self.add3.setObjectName("add3")
        self.horizontalLayout_5.addWidget(self.add3)
        self.verticalLayout_11.addLayout(self.horizontalLayout_5)
        self.verticalLayout_10.addLayout(self.verticalLayout_11)
        self.layoutWidget_6 = QtWidgets.QWidget(Menu)
        self.layoutWidget_6.setGeometry(QtCore.QRect(570, 250, 201, 215))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.layoutWidget_6)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.pic6 = QtWidgets.QLabel(self.layoutWidget_6)
        self.pic6.setText("")
        self.pic6.setPixmap(QtGui.QPixmap(""))
        self.pic6.setObjectName("pic6")
        self.verticalLayout_12.addWidget(self.pic6)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.name6 = QtWidgets.QLabel(self.layoutWidget_6)
        self.name6.setObjectName("name6")
        self.verticalLayout_13.addWidget(self.name6)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.delete6 = QtWidgets.QPushButton(self.layoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.delete6.setFont(font)
        self.delete6.setObjectName("delete6")
        self.horizontalLayout_6.addWidget(self.delete6)
        self.number6 = QtWidgets.QLCDNumber(self.layoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.number6.setFont(font)
        self.number6.setDigitCount(5)
        self.number6.setObjectName("number6")
        self.horizontalLayout_6.addWidget(self.number6)
        self.add6 = QtWidgets.QPushButton(self.layoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.add6.setFont(font)
        self.add6.setObjectName("add6")
        self.horizontalLayout_6.addWidget(self.add6)
        self.verticalLayout_13.addLayout(self.horizontalLayout_6)
        self.verticalLayout_12.addLayout(self.verticalLayout_13)
        self.widget = QtWidgets.QWidget(Menu)
        self.widget.setGeometry(QtCore.QRect(140, 20, 201, 215))
        self.widget.setObjectName("widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pic1 = QtWidgets.QLabel(self.widget)
        self.pic1.setText("")
        self.pic1.setPixmap(QtGui.QPixmap("./source/面饭/面饭7.jpg"))
        self.pic1.setObjectName("pic1")
        self.verticalLayout_4.addWidget(self.pic1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.name1 = QtWidgets.QLabel(self.widget)
        self.name1.setObjectName("name1")
        self.verticalLayout.addWidget(self.name1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.delete1 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.delete1.setFont(font)
        self.delete1.setObjectName("delete1")
        self.horizontalLayout.addWidget(self.delete1)
        self.number1 = QtWidgets.QLCDNumber(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.number1.setFont(font)
        self.number1.setDigitCount(5)
        self.number1.setObjectName("number1")
        self.horizontalLayout.addWidget(self.number1)
        self.add1 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.add1.setFont(font)
        self.add1.setObjectName("add1")
        self.horizontalLayout.addWidget(self.add1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.widget1 = QtWidgets.QWidget(Menu)
        self.widget1.setGeometry(QtCore.QRect(30, 130, 77, 196))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_14.addWidget(self.label)
        self.rice_btn = QtWidgets.QPushButton(self.widget1)
        self.rice_btn.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.rice_btn.setObjectName("rice_btn")
        self.verticalLayout_14.addWidget(self.rice_btn)
        self.steak_btn = QtWidgets.QPushButton(self.widget1)
        self.steak_btn.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.steak_btn.setObjectName("steak_btn")
        self.verticalLayout_14.addWidget(self.steak_btn)
        self.pizza_btn = QtWidgets.QPushButton(self.widget1)
        self.pizza_btn.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pizza_btn.setObjectName("pizza_btn")
        self.verticalLayout_14.addWidget(self.pizza_btn)
        self.package_btn = QtWidgets.QPushButton(self.widget1)
        self.package_btn.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.package_btn.setObjectName("package_btn")
        self.verticalLayout_14.addWidget(self.package_btn)
        self.drink_btn = QtWidgets.QPushButton(self.widget1)
        self.drink_btn.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.drink_btn.setObjectName("drink_btn")
        self.verticalLayout_14.addWidget(self.drink_btn)
        self.other_btn = QtWidgets.QPushButton(self.widget1)
        self.other_btn.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.other_btn.setObjectName("other_btn")
        self.verticalLayout_14.addWidget(self.other_btn)
        
        self.db=DataBase()
        self.retranslateUi(Menu)
        QtCore.QMetaObject.connectSlotsByName(Menu)
        self.rice_btn.clicked.connect(self.showR)
        self.steak_btn.clicked.connect(self.showS)
        self.pizza_btn.clicked.connect(self.showPizza)
        self.package_btn.clicked.connect(self.showP)
        self.drink_btn.clicked.connect(self.showD)
        self.other_btn.clicked.connect(self.showO)
        self.add1.clicked.connect(lambda:self.add(1))
        self.add2.clicked.connect(lambda:self.add(2))
        self.add3.clicked.connect(lambda:self.add(3))
        self.add4.clicked.connect(lambda:self.add(4))
        self.add5.clicked.connect(lambda:self.add(5))
        self.add6.clicked.connect(lambda:self.add(6))
        self.delete1.clicked.connect(lambda:self.delete(1))
        self.delete2.clicked.connect(lambda:self.delete(2))
        self.delete3.clicked.connect(lambda:self.delete(3))
        self.delete4.clicked.connect(lambda:self.delete(4))
        self.delete5.clicked.connect(lambda:self.delete(5))
        self.delete6.clicked.connect(lambda:self.delete(6))
        self.order_btn.clicked.connect(self.showOrder)
        self.ui='面饭'
        self.R=R
        self.P=P
        self.D=D
        self.Pizza=Pizza
        self.S=S
        self.showR()
        self. setFalse()
    
    def showOrder(self):
        data=[]
        result=self.db.get_mesg('面饭')
        for i in range(len(self.R)):
            if self.R[i]==0:
                pass
            else:
                data.append([result[i][1],result[i][2],self.R[i],self.R[i]*result[i][2]])
        result=self.db.get_mesg('牛排')
        for i in range(len(self.S)):
            if self.S[i]==0:
                pass
            else:
                data.append([result[i][1],result[i][2],self.S[i],self.S[i]*result[i][2]])            
        result=self.db.get_mesg('披萨')
        for i in range(len(self.Pizza)):
            if self.Pizza[i]==0:
                pass
            else:
                data.append([result[i][1],result[i][2],self.Pizza[i],self.Pizza[i]*result[i][2]])  
        result=self.db.get_mesg('套餐')
        for i in range(len(self.P)):
            if self.P[i]==0:
                pass
            else:
                data.append([result[i][1],result[i][2],self.P[i],self.P[i]*result[i][2]])
        result=self.db.get_mesg('饮料')
        for i in range(len(self.D)):
            if self.D[i]==0:
                pass
            else:
                data.append([result[i][1],result[i][2],self.D[i],self.D[i]*result[i][2]])
        self.db.insert_order(data)
        self.keep()
        
    def keep(self):
        self.db.insert_parameters([str(self.R),str(self.S),str(self.Pizza),str(self.P),str(self.D)])

    def add(self,n):
        if self.ui=='R':
            num=eval('self.number'+str(n)).value()
            num+=1
            self.R[n-1]=num
            eval('self.number'+str(n)).display(num)
        elif self.ui=='S':
            num=eval('self.number'+str(n)).value()
            num+=1
            self.S[n-1]=num
            eval('self.number'+str(n)).display(num)
        elif self.ui=='P':
            num=eval('self.number'+str(n)).value()
            num+=1
            self.P[n-1]=num
            eval('self.number'+str(n)).display(num)
        elif self.ui=='Pizza':
            num=eval('self.number'+str(n)).value()
            num+=1
            self.Pizza[n-1]=num
            eval('self.number'+str(n)).display(num)
        elif self.ui=='D':
            num=eval('self.number'+str(n)).value()
            num+=1
            self.D[n-1]=num
            eval('self.number'+str(n)).display(num)
        self. setFalse()
            
    
    def delete(self,n):
        num=eval('self.number'+str(n)).value()
        if self.ui=='R':
            num=eval('self.number'+str(n)).value()
            num-=1
            self.R[n-1]=num
            eval('self.number'+str(n)).display(num)
        elif self.ui=='S':
            num=eval('self.number'+str(n)).value()
            num-=1
            self.S[n-1]=num
            eval('self.number'+str(n)).display(num)
        elif self.ui=='P':
            num=eval('self.number'+str(n)).value()
            num-=1
            self.P[n-1]=num
            eval('self.number'+str(n)).display(num)
        elif self.ui=='Pizza':
            num=eval('self.number'+str(n)).value()
            num-=1
            self.Pizza[n-1]=num
            eval('self.number'+str(n)).display(num)
        elif self.ui=='D':
            num=eval('self.number'+str(n)).value()
            num-=1
            self.D[n-1]=num
            eval('self.number'+str(n)).display(num)
        self. setFalse()
        
    
    def setFalse(self):
        for i in range(1,7):
            if eval('self.number'+str(i)).value()==0:
                eval('self.delete'+str(i)).setEnabled(False)
            else:
                eval('self.delete'+str(i)).setEnabled(True)
        
    
    def show_init(self):
        self.name1.setText('')
        self.name2.setText('')
        self.name3.setText('')
        self.name4.setText('')
        self.name5.setText('')
        self.name6.setText('')
        self.pic1.setPixmap(QtGui.QPixmap(''))
        self.pic2.setPixmap(QtGui.QPixmap(''))
        self.pic3.setPixmap(QtGui.QPixmap(''))
        self.pic4.setPixmap(QtGui.QPixmap(''))
        self.pic5.setPixmap(QtGui.QPixmap(''))
        self.pic6.setPixmap(QtGui.QPixmap(''))
    
    def showR(self):
        
        self.ui='R'
        self.show_init()
        result=self.db.get_mesg('面饭')
        for i in range(len(result)):
            eval('self.name'+str(i+1)).setText(result[i][1]+"           "+str(result[i][2])+'元')
            eval('self.pic'+str(i+1)).setPixmap(QtGui.QPixmap("./source/面饭/"+
                result[i][0]))
        
        for i in range(len(self.R)):
            eval('self.number'+str(i+1)).display(self.R[i])
            
            
    def showS(self):
        self.ui='S'
        self.show_init()
        result=self.db.get_mesg('牛排')
        for i in range(len(result)):
            eval('self.name'+str(i+1)).setText(result[i][1]+"           "+str(result[i][2])+'元')
            eval('self.pic'+str(i+1)).setPixmap(QtGui.QPixmap("./source/牛排/"+
                result[i][0]))
        for i in range(len(self.S)):
            eval('self.number'+str(i+1)).display(self.S[i])
    def showPizza(self):
        self.ui='Pizza'
        self.show_init()
        result=self.db.get_mesg('披萨')
        for i in range(len(result)):
            eval('self.name'+str(i+1)).setText(result[i][1]+"           "+str(result[i][2])+'元')
            eval('self.pic'+str(i+1)).setPixmap(QtGui.QPixmap("./source/披萨/"+
                result[i][0]))
        for i in range(len(self.Pizza)):
            eval('self.number'+str(i+1)).display(self.Pizza[i])
    def showP(self):
        self.ui='P'
        self.show_init()
        result=self.db.get_mesg('套餐')
        for i in range(len(result)):
            eval('self.name'+str(i+1)).setText(result[i][1]+"           "+str(result[i][2])+'元')
            eval('self.pic'+str(i+1)).setPixmap(QtGui.QPixmap("./source/套餐/"+result[i][0])) 
        for i in range(len(self.P)):
            eval('self.number'+str(i+1)).display(self.P[i])
    def showD(self):
        self.ui='D'
        self.show_init()
        result=self.db.get_mesg('饮料')
        for i in range(len(result)):
            eval('self.name'+str(i+1)).setText(result[i][1]+"           "+str(result[i][2])+'元')
            eval('self.pic'+str(i+1)).setPixmap(QtGui.QPixmap("./source/饮料/"+result[i][0]))
        for i in range(len(self.D)):
            eval('self.number'+str(i+1)).display(self.D[i])
    def showO(self):
        pass
        
        

    def retranslateUi(self, Menu):
        _translate = QtCore.QCoreApplication.translate
        Menu.setWindowTitle(_translate("Menu", "菜品界面"))
        self.order_btn.setText(_translate("Menu", "订单"))
        self.over_btn.setText(_translate("Menu", "选择完毕"))
        self.name2.setText(_translate("Menu", ""))
        self.delete2.setText(_translate("Menu", "-"))
        self.add2.setText(_translate("Menu", "+"))
        self.name4.setText(_translate("Menu", ""))
        self.delete4.setText(_translate("Menu", "-"))
        self.add4.setText(_translate("Menu", "+"))
        self.name5.setText(_translate("Menu", ""))
        self.delete5.setText(_translate("Menu", "-"))
        self.add5.setText(_translate("Menu", "+"))
        self.name3.setText(_translate("Menu", ""))
        self.delete3.setText(_translate("Menu", "-"))
        self.add3.setText(_translate("Menu", "+"))
        self.name6.setText(_translate("Menu", ""))
        self.delete6.setText(_translate("Menu", "-"))
        self.add6.setText(_translate("Menu", "+"))
        self.name1.setText(_translate("Menu", ""))
        self.delete1.setText(_translate("Menu", "-"))
        self.add1.setText(_translate("Menu", "+"))
        self.label.setText(_translate("Menu", "菜类"))
        self.rice_btn.setText(_translate("Menu", "面饭"))
        self.steak_btn.setText(_translate("Menu", "牛排"))
        self.pizza_btn.setText(_translate("Menu", "披萨"))
        self.package_btn.setText(_translate("Menu", "套餐"))
        self.drink_btn.setText(_translate("Menu", "饮料"))
        self.other_btn.setText(_translate("Menu", "其他"))


    

import source.apprcc_rc
import sys
if __name__=='__main__':
    app=QtWidgets.QApplication(sys.argv)
    win=Ui_Menu()
    menu=QtWidgets.QMainWindow()
    win.setupUi(menu)
    menu.show()
    sys.exit(app.exec_())