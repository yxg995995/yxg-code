# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Login):
        #总体界面的样式
        Login.setObjectName("Login")
        Login.resize(483, 310)
        Login.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Login.setStyleSheet("")
        #垂直排版
        self.splitter = QtWidgets.QSplitter(Login)
        self.splitter.setGeometry(QtCore.QRect(100, 20, 281, 241))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        #系统名字
        self.label = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        #分页控件
        self.tabWidget = QtWidgets.QTabWidget(self.splitter)
        self.tabWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        #分页控件栅格栏排版
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        #用户名标签
        self.label_2 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        #密码标签
        self.label_3 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        #用于输入密码的密码框
        self.password = QtWidgets.QLineEdit(self.tab)
        self.password.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.gridLayout.addWidget(self.password, 1, 1, 1, 1)
        #用于输入用户名的用户框
        self.user = QtWidgets.QLineEdit(self.tab)
        self.user.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.user.setObjectName("user")
        self.gridLayout.addWidget(self.user, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)
        #水平排版
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        #登陆按钮
        self.login_btn = QtWidgets.QPushButton(self.tab)
        self.login_btn.setObjectName("login_btn")
        self.horizontalLayout.addWidget(self.login_btn)
        #注册按钮
        self.to_register = QtWidgets.QPushButton(self.tab)
        self.to_register.setObjectName("to_register")
        self.horizontalLayout.addWidget(self.to_register)
        self.gridLayout_4.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        #分页控件第二页（管理员登陆界面）排版样式同用户一样
        self.tabWidget.addTab(self.tab, "")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.Admin = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Admin.setFont(font)
        self.Admin.setStyleSheet("")
        self.Admin.setText("")
        self.Admin.setObjectName("Admin")
        self.gridLayout_2.addWidget(self.Admin, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        self.admin_password = QtWidgets.QLineEdit(self.widget)
        self.admin_password.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.admin_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.admin_password.setObjectName("admin_password")
        self.gridLayout_2.addWidget(self.admin_password, 1, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.login_admin = QtWidgets.QPushButton(self.widget)
        self.login_admin.setObjectName("login_admin")
        self.horizontalLayout_2.addWidget(self.login_admin)
        self.register_amin = QtWidgets.QPushButton(self.widget)
        self.register_amin.setObjectName("register_amin")
        self.horizontalLayout_2.addWidget(self.register_amin)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.tabWidget.addTab(self.widget, "")

        self.retranslateUi(Login)
        #当前页面
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Login)
        #设置tab顺序
        Login.setTabOrder(self.user, self.password)
        Login.setTabOrder(self.password, self.login_btn)
        Login.setTabOrder(self.login_btn, self.to_register)
        Login.setTabOrder(self.to_register, self.tabWidget)
        Login.setTabOrder(self.tabWidget, self.Admin)
        Login.setTabOrder(self.Admin, self.admin_password)
        Login.setTabOrder(self.admin_password, self.login_admin)
        Login.setTabOrder(self.login_admin, self.register_amin)
    
    #转换控件属性，设置中文等
    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "登录界面"))
        self.label.setText(_translate("Login", "校园点餐系统"))
        self.label_2.setText(_translate("Login", "用户名"))
        self.label_3.setText(_translate("Login", "密码"))
        self.login_btn.setText(_translate("Login", "登陆"))
        self.to_register.setText(_translate("Login", "注册"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Login", "用户"))
        self.label_4.setText(_translate("Login", "管理员"))
        self.label_5.setText(_translate("Login", "密码"))
        self.login_admin.setText(_translate("Login", "登陆"))
        self.register_amin.setText(_translate("Login", "注册"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), _translate("Login", "管理员"))


