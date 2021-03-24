from PyQt5.QtWidgets import (QWidget , QHBoxLayout , QVBoxLayout , QApplication, 
                             QPushButton, QLineEdit ,QLabel , QSplitter ,  QTableView , 
                             QHeaderView , QMessageBox )
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.Qt import *
from PyQt5.QtSql import QSqlDatabase  , QSqlQueryModel , QSqlQuery

class Ui_out_orderWindow(object):
    def setupUi(self, out_orderWindow):
        out_orderWindow.setObjectName("out_orderWindow")
        out_orderWindow.resize(622, 504)
        self.centralwidget = QtWidgets.QWidget(out_orderWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(90, 10, 426, 25))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.prevButton = QtWidgets.QPushButton(self.layoutWidget_2)
        self.prevButton.setObjectName("prevButton")
        self.horizontalLayout.addWidget(self.prevButton)
        self.nextButton = QtWidgets.QPushButton(self.layoutWidget_2)
        self.nextButton.setObjectName("nextButton")
        self.horizontalLayout.addWidget(self.nextButton)
        self.label = QtWidgets.QLabel(self.layoutWidget_2)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.switch_line = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.switch_line.setObjectName("switch_line")
        self.horizontalLayout.addWidget(self.switch_line)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.switchPageButton = QtWidgets.QPushButton(self.layoutWidget_2)
        self.switchPageButton.setObjectName("switchPageButton")
        self.horizontalLayout.addWidget(self.switchPageButton)
        self.total = QtWidgets.QLabel(self.centralwidget)
        self.total.setGeometry(QtCore.QRect(20, 450, 80, 20))
        self.total.setText("")
        self.total.setAlignment(QtCore.Qt.AlignCenter)
        self.total.setObjectName("total")
        self.current = QtWidgets.QLabel(self.centralwidget)
        self.current.setGeometry(QtCore.QRect(150, 450, 80, 20))
        self.current.setText("")
        self.current.setAlignment(QtCore.Qt.AlignCenter)
        self.current.setObjectName("current")
        self.record = QtWidgets.QLabel(self.centralwidget)
        self.record.setGeometry(QtCore.QRect(510, 450, 80, 20))
        self.record.setText("")
        self.record.setAlignment(QtCore.Qt.AlignCenter)
        self.record.setObjectName("record")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(93, 40, 421, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.splitter = QtWidgets.QSplitter(self.layoutWidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.search_line = QtWidgets.QLineEdit(self.splitter)
        self.search_line.setObjectName("search_line")
        self.feature = QtWidgets.QComboBox(self.splitter)
        self.feature.setObjectName("feature")
        self.feature.addItem("")
        self.feature.addItem("")
        self.feature.addItem("")
        self.feature.addItem("")
        self.horizontalLayout_2.addWidget(self.splitter)
        self.searchButton = QtWidgets.QPushButton(self.layoutWidget)
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout_2.addWidget(self.searchButton)
        self.clear = QtWidgets.QPushButton(self.layoutWidget)
        self.clear.setObjectName("clear")
        self.horizontalLayout_2.addWidget(self.clear)
        self.Table_widget = QtWidgets.QWidget(self.centralwidget)
        self.Table_widget.setGeometry(QtCore.QRect(0, 60, 611, 381))
        self.Table_widget.setObjectName("Table_widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.Table_widget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tableView = QtWidgets.QTableView(self.Table_widget)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setCascadingSectionResizes(False)
        self.horizontalLayout_3.addWidget(self.tableView)
        out_orderWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(out_orderWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 622, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        out_orderWindow.setMenuBar(self.menubar)
        self.actionadd = QtWidgets.QAction(out_orderWindow)
        self.actionadd.setObjectName("actionadd")
        self.actiondelete = QtWidgets.QAction(out_orderWindow)
        self.actiondelete.setObjectName("actiondelete")
        self.menu.addSeparator()
        self.menu.addAction(self.actionadd)
        self.menu.addAction(self.actiondelete)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(out_orderWindow)
        self.clear.clicked.connect(self.search_line.clear)
        QtCore.QMetaObject.connectSlotsByName(out_orderWindow)
        out_orderWindow.setTabOrder(self.switch_line, self.switchPageButton)
        out_orderWindow.setTabOrder(self.switchPageButton, self.search_line)
        out_orderWindow.setTabOrder(self.search_line, self.feature)
        out_orderWindow.setTabOrder(self.feature, self.searchButton)
        out_orderWindow.setTabOrder(self.searchButton, self.clear)
        out_orderWindow.setTabOrder(self.clear, self.prevButton)
        out_orderWindow.setTabOrder(self.prevButton, self.nextButton)
        
        self.queryModel = None
        self.currentPage = 0
        self.totalPage = 0
        self.totalRecrodCount = 0
        self.PageRecordCount  = 10
        
        self.setTableView()
        self.prevButton.clicked.connect(self.onPrevButtonClick)
        self.nextButton.clicked.connect(self.onnextButtonClick)
        self.switchPageButton.clicked.connect(self.onSwitchPageButtonClick)
        self.searchButton.clicked.connect(self.onSearch)
        self.clear.clicked.connect(self.onClear)
        
        self.totalPage=self.getPageCount()
        #刷新状态
        self.updateStatus()
		# 设置总页数文本
        self.setTotalPageLabel()
		# 设置总记录数
        self.setTotalRecordLabel()
        
        
    def onClear(self):
        self.setTableView()
    
    def onSearch(self):
        feature=self.feature.currentText()
        key="'%"+self.search_line.text()+"%'"
        q="select * from out_order where "+feature+" like %s"
        query=(q%key)
        self.queryModel.setQuery(query)
        self.totalRecrodCount=self.queryModel.rowCount()
        self.currentPage = 1
        self.totalPage=self.getPageCount()
        self.updateStatus()
        self.setTotalPageLabel()
        self.setTotalRecordLabel()
        
        
    def onPrevButtonClick(self):
        limitIndex=(self.currentPage-2)*self.PageRecordCount
        self.recordQuery(limitIndex)
        self.currentPage-=1
        self.updateStatus()
    
    def onnextButtonClick(self):
        if self.totalPage==1:
            QMessageBox.information(self.Table_widget, "提示", "已经是最后一页了" )
            self.nextButton.setEnabled(False)
            return
        if self.currentPage==self.totalPage:
            QMessageBox.information(self.Table_widget, "提示", "已经是最后一页了" )
            self.nextButton.setEnabled(False)
            return
        limitIndex=self.currentPage*self.PageRecordCount
        self.recordQuery(limitIndex)
        self.currentPage+=1
        self.updateStatus()
    
    
    def onSwitchPageButtonClick(self):
        to_page=self.switch_line.text()
        #判断是否为空
        if to_page=="":
            QMessageBox.information(self.Table_widget, "提示" , "请输入跳转页面" )
            return 
        if not to_page.isdigit():
            QMessageBox.information(self.Table_widget, "提示", "请输入数字" )
            return
        page_index=eval(to_page)
        if page_index > self.totalPage or page_index < 1 :
            QMessageBox.information(self.Table_widget, "提示", "没有指定的页面，请重新输入" )
            return
        limitIndex = (page_index-1) * self.PageRecordCount
        self.recordQuery(limitIndex)
        self.currentPage=page_index
        self.updateStatus()
    #获取总记录数
    def getTotalRecord(self):
        self.queryModel.setQuery("select * from out_order")
        rowCount = self.queryModel.rowCount()
        return rowCount
    
    #获取页数
    def getPageCount(self):
        if self.totalRecrodCount % self.PageRecordCount == 0:
            return(self.totalRecrodCount/self.PageRecordCount)
        else:
            return(int(self.totalRecrodCount/self.PageRecordCount)+1)
            
    
    def setTotalPageLabel(self):
        szPageCountText  = ("总共%d页" % self.totalPage )
        self.total.setText(szPageCountText)
    
    def setTotalRecordLabel(self):
        szTotalRecordText  = ("共%d条" % self.totalRecrodCount )
        self.record.setText(szTotalRecordText)
    
    def updateStatus(self):
        szCurrentText = ("当前第%d页" % self.currentPage )
        self.current.setText(szCurrentText)
        
		#设置按钮是否可用
        if self.currentPage== 1 :
            self.prevButton.setEnabled( False )
            self.nextButton.setEnabled(True)
        else:
            self.prevButton.setEnabled( True )
            self.nextButton.setEnabled( True )
        
    def setTableView(self):
        self.db=QSqlDatabase.addDatabase('QMYSQL')
        self.db.setHostName('localhost')
        self.db.setDatabaseName('inventorydb')
        self.db.setUserName('yxg')
        self.db.setPassword('yxg579521..')
        self.db.open()
        self.queryModel=QSqlQueryModel(self.Table_widget)
        self.currentPage = 1
        self.totalRecrodCount = self.getTotalRecord()
        self.totalPage=self.getPageCount()
        self.updateStatus()
        self.setTotalPageLabel()
        self.setTotalRecordLabel()
        self.recordQuery(0)
        self.tableView.setModel(self.queryModel)
        self.queryModel.setHeaderData(0, Qt.Horizontal, "出库单编号")
        self.queryModel.setHeaderData(1, Qt.Horizontal, "出库时间")
        self.queryModel.setHeaderData(2, Qt.Horizontal, "经办人")
        self.queryModel.setHeaderData(3, Qt.Horizontal, "联系电话")


        
    def recordQuery(self,limitIndex):
        szQuery = ("select * from out_order limit %s,%s" %(limitIndex , self.PageRecordCount))

    def retranslateUi(self, out_orderWindow):
        _translate = QtCore.QCoreApplication.translate
        out_orderWindow.setWindowTitle(_translate("out_orderWindow", "出库表"))
        self.prevButton.setText(_translate("out_orderWindow", "前一页"))
        self.nextButton.setText(_translate("out_orderWindow", "后一页"))
        self.label.setText(_translate("out_orderWindow", "前往"))
        self.label_2.setText(_translate("out_orderWindow", "页"))
        self.switchPageButton.setText(_translate("out_orderWindow", "go"))
        self.feature.setItemText(0, _translate("out_orderWindow", "out_orderNo"))
        self.feature.setItemText(1, _translate("out_orderWindow", "out_date"))
        self.feature.setItemText(2, _translate("out_orderWindow", "operator"))
        self.feature.setItemText(3, _translate("out_orderWindow", "phone"))
        self.searchButton.setText(_translate("out_orderWindow", "搜索"))
        self.clear.setText(_translate("out_orderWindow", "更新"))
        self.menu.setTitle(_translate("out_orderWindow", "功能"))
        self.actionadd.setText(_translate("out_orderWindow", "add"))
        self.actionadd.setShortcut(_translate("out_orderWindow", "Ctrl+N"))
        self.actiondelete.setText(_translate("out_orderWindow", "delete"))


