import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from Ui_weather import Ui_form
from spider import Spider

class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        self.spider=Spider()
        super(MainWindow, self).__init__(parent)
        self.ui=Ui_form()
        self.ui.setupUi(self)
    
    def onActivatedpushButton_ok(self):
        # 取当前索引
        province_index =self.ui.provinceComboBox.currentIndex()
        city_index = self.ui.citycomboBox.currentIndex()
        town_index = self.ui.towncomboBox.currentIndex()
        # 取当前省市县名称
        province= self.ui.provinceComboBox.itemText(province_index)
        city= self.ui.citycomboBox.itemText(city_index)
        town = self.ui.towncomboBox.itemText(town_index)
        result=self.spider.tempSpider(province, city, town)
        self.ui.resultText.setText(result)

if __name__=="__main__":
    app=QApplication(sys.argv)
    win=MainWindow()
    win.show()
    sys.exit(app.exec_())
        
    
        
