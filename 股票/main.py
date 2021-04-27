import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import QUrl
from Ui_stock import Ui_Stock
from StockSpider import Spider
import time
from Draw import Drawing
class Stock_GUI(QWidget):
    def __init__(self,parent=None):
        super(Stock_GUI, self).__init__(parent)
        #加载界面
        self.stock=Ui_Stock()
        self.stock.setupUi(self)
        #导入画图的类
        self.draw=Drawing()
        #按钮点击后触发事件
        self.stock.draw.clicked.connect(self.begin)
        self.stock.dayK.clicked.connect(self.Draw_day)
        self.stock.weekK.clicked.connect(self.Draw_week)
        self.stock.monthK.clicked.connect(self.Draw_month)
        self.stock.clear.clicked.connect(self.clearAll)
        
    #开始爬取数据画图
    def begin(self):
        #当前时间
        now=time.strftime("%Y%m%d", time.localtime())
        #判断股票代码框输入是否为空,为空就报错
        if self.stock.stock_id.text()=='':
            #报错弹出报错框
            reply=QMessageBox.warning(self,'警告','请勿搜索空值')
            #清空输入框内容
            self.stock.stock_id.clear()
            return
        #判断终止时间是否超过当前时间
        if self.stock.end.text()>=now:
            #同上
            reply=QMessageBox.warning(self,'警告','终止时间请勿超过当天')
            self.stock.end.clear()
            return
        else:
            #爬虫开始爬取数据
            self.spider=Spider(self.stock.stock_id.text())
            #获取当前输入的起始时间
            start=self.stock.start.text()
            #获取当前的终止时间
            end=self.stock.end.text()
            #判断股票是否为空或者已经退市
            if self.spider.daySpider(start, end):
                #画三类K图
                self.draw.dayK()
                self.draw.weekK()
                self.draw.monthK()
                #完成后提示成功
                reply=QMessageBox.information(self,'成功','制作完成')
                #默认成功后显示日K线图
                #设置加载页面的路径
                self.url='D:/UI/股票/日K线图.html'
                #展示加载的页面
                self.stock.webEngineView.load(QUrl(self.url))
                #设置按钮可以点击
                self.stock.dayK.setEnabled(True)
                self.stock.weekK.setEnabled(True)
                self.stock.monthK.setEnabled(True)
            else:
                reply=QMessageBox.warning(self,'警告','股票代码不存在或者已退市')
                return
            
    def clearAll(self):
        #清空所有
        self.url=''
        self.stock.webEngineView.load(QUrl(self.url))
        self.stock.dayK.setEnabled(False)
        self.stock.weekK.setEnabled(False)
        self.stock.monthK.setEnabled(False)
    
    def Draw_day(self):
        self.url='D:/UI/股票/日K线图.html'
        self.stock.webEngineView.load(QUrl(self.url))
    
    def Draw_week(self):
        self.url='D:/UI/股票/周K线图.html'
        self.stock.webEngineView.load(QUrl(self.url))
    
    def Draw_month(self):
        self.url='D:/UI/股票/月K线图.html'
        self.stock.webEngineView.load(QUrl(self.url))

if __name__=='__main__':
    app=QApplication(sys.argv)
    win=Stock_GUI()
    win.show()
    sys.exit(app.exec_())