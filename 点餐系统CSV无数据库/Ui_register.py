# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Register(object):
    def setupUi(self, Register):
        #界面总体大小样式
        Register.setObjectName("Register")
        Register.resize(557, 400)
        Register.setStyleSheet("")
        #注册标签
        self.register_title = QtWidgets.QLabel(Register)
        self.register_title.setGeometry(QtCore.QRect(190, 20, 171, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.register_title.setFont(font)
        self.register_title.setStyleSheet("QLabel{border:None}")
        self.register_title.setAlignment(QtCore.Qt.AlignCenter)
        self.register_title.setObjectName("register_title")
        #垂直排版布局
        self.layoutWidget = QtWidgets.QWidget(Register)
        self.layoutWidget.setGeometry(QtCore.QRect(180, 260, 161, 58))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        #注册按钮
        self.register_ok = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.register_ok.setFont(font)
        self.register_ok.setObjectName("register_ok")
        self.verticalLayout.addWidget(self.register_ok)
        #取消按钮
        self.cancle = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.cancle.setFont(font)
        self.cancle.setObjectName("cancle")
        self.verticalLayout.addWidget(self.cancle)
        self.layoutWidget1 = QtWidgets.QWidget(Register)
        self.layoutWidget1.setGeometry(QtCore.QRect(130, 80, 291, 141))
        self.layoutWidget1.setObjectName("layoutWidget1")
        #栅格栏布局
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        #确认密码框
        self.cp = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cp.setFont(font)
        self.cp.setMaxLength(12)
        self.cp.setEchoMode(QtWidgets.QLineEdit.Password)
        self.cp.setObjectName("cp")
        self.gridLayout.addWidget(self.cp, 2, 1, 1, 1)
        self.register_user = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        #用户名框
        self.register_user.setFont(font)
        self.register_user.setStyleSheet("")
        self.register_user.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.register_user.setObjectName("register_user")
        self.gridLayout.addWidget(self.register_user, 0, 0, 1, 1)
        self.userName = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.userName.setFont(font)
        self.userName.setObjectName("userName")
        self.gridLayout.addWidget(self.userName, 0, 1, 1, 1)
        self.password = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        #密码框
        self.password.setFont(font)
        self.password.setMaxLength(12)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.gridLayout.addWidget(self.password, 1, 1, 1, 1)
        self.register_repassword = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.register_repassword.setFont(font)
        self.register_repassword.setObjectName("register_repassword")
        self.gridLayout.addWidget(self.register_repassword, 2, 0, 1, 1)
        self.register_password = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.register_password.setFont(font)
        self.register_password.setObjectName("register_password")
        self.gridLayout.addWidget(self.register_password, 1, 0, 1, 1)

        self.retranslateUi(Register)
        #按钮绑定事件，点击按钮就会触发事件
        #clear 清空文本框
        self.cancle.clicked.connect(self.userName.clear)
        self.cancle.clicked.connect(self.password.clear)
        self.cancle.clicked.connect(self.cp.clear)
        
        QtCore.QMetaObject.connectSlotsByName(Register)
        #tab顺序
        Register.setTabOrder(self.userName, self.password)
        Register.setTabOrder(self.password, self.cp)
        Register.setTabOrder(self.cp, self.register_ok)
        Register.setTabOrder(self.register_ok, self.cancle)

    def retranslateUi(self, Register):
        _translate = QtCore.QCoreApplication.translate
        Register.setWindowTitle(_translate("Register", "注册界面"))
        self.register_title.setText(_translate("Register", "用户注册"))
        self.register_ok.setText(_translate("Register", "注册"))
        self.cancle.setText(_translate("Register", "取消"))
        self.register_user.setText(_translate("Register", "用户名："))
        self.register_repassword.setText(_translate("Register", "确认密码："))
        self.register_password.setText(_translate("Register", "密码："))

