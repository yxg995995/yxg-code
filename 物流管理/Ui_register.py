# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Register(object):
    def setupUi(self, Register):
        Register.setObjectName("Register")
        Register.resize(322, 364)
        self.gridLayout_2 = QtWidgets.QGridLayout(Register)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(Register)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_9 = QtWidgets.QLabel(Register)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(Register)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)
        self.addr = QtWidgets.QTextEdit(Register)
        self.addr.setObjectName("addr")
        self.gridLayout.addWidget(self.addr, 7, 2, 1, 1)
        self.sex = QtWidgets.QComboBox(Register)
        self.sex.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.sex.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.sex.setObjectName("sex")
        self.sex.addItem("")
        self.sex.addItem("")
        self.gridLayout.addWidget(self.sex, 4, 2, 1, 1)
        self.email = QtWidgets.QLineEdit(Register)
        self.email.setObjectName("email")
        self.gridLayout.addWidget(self.email, 6, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(Register)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)
        self.username = QtWidgets.QLineEdit(Register)
        self.username.setObjectName("username")
        self.gridLayout.addWidget(self.username, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(Register)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.password = QtWidgets.QLineEdit(Register)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.gridLayout.addWidget(self.password, 1, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(Register)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(Register)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(Register)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.trueName = QtWidgets.QLineEdit(Register)
        self.trueName.setInputMask("")
        self.trueName.setObjectName("trueName")
        self.gridLayout.addWidget(self.trueName, 5, 2, 1, 1)
        self.phone = QtWidgets.QLineEdit(Register)
        self.phone.setObjectName("phone")
        self.gridLayout.addWidget(self.phone, 3, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(Register)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.cp = QtWidgets.QLineEdit(Register)
        self.cp.setEchoMode(QtWidgets.QLineEdit.Password)
        self.cp.setObjectName("cp")
        self.gridLayout.addWidget(self.cp, 2, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ok = QtWidgets.QPushButton(Register)
        self.ok.setObjectName("ok")
        self.horizontalLayout.addWidget(self.ok)
        self.cancel = QtWidgets.QPushButton(Register)
        self.cancel.setObjectName("cancel")
        self.horizontalLayout.addWidget(self.cancel)
        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.retranslateUi(Register)
        self.cancel.clicked.connect(Register.close)
        QtCore.QMetaObject.connectSlotsByName(Register)
        Register.setTabOrder(self.username, self.password)
        Register.setTabOrder(self.password, self.cp)
        Register.setTabOrder(self.cp, self.phone)
        Register.setTabOrder(self.phone, self.sex)
        Register.setTabOrder(self.sex, self.trueName)
        Register.setTabOrder(self.trueName, self.email)
        Register.setTabOrder(self.email, self.addr)
        Register.setTabOrder(self.addr, self.ok)
        Register.setTabOrder(self.ok, self.cancel)

    def retranslateUi(self, Register):
        _translate = QtCore.QCoreApplication.translate
        Register.setWindowTitle(_translate("Register", "注册界面"))
        self.label.setText(_translate("Register", "注册界面"))
        self.label_9.setText(_translate("Register", "确认密码"))
        self.label_7.setText(_translate("Register", "邮箱"))
        self.addr.setPlaceholderText(_translate("Register", "选填"))
        self.sex.setItemText(0, _translate("Register", "男"))
        self.sex.setItemText(1, _translate("Register", "女"))
        self.email.setPlaceholderText(_translate("Register", "选填"))
        self.label_8.setText(_translate("Register", "地址"))
        self.username.setPlaceholderText(_translate("Register", "必填"))
        self.label_3.setText(_translate("Register", "密码"))
        self.password.setPlaceholderText(_translate("Register", "必填"))
        self.label_4.setText(_translate("Register", "手机号"))
        self.label_5.setText(_translate("Register", "性别"))
        self.label_6.setText(_translate("Register", "真实姓名"))
        self.trueName.setPlaceholderText(_translate("Register", "选填"))
        self.phone.setPlaceholderText(_translate("Register", "必填"))
        self.label_2.setText(_translate("Register", "用户名"))
        self.cp.setPlaceholderText(_translate("Register", "必填"))
        self.ok.setText(_translate("Register", "确认"))
        self.cancel.setText(_translate("Register", "取消"))


