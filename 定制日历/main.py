import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtSql import QSqlDatabase  , QSqlQueryModel , QSqlQuery
from Ui_weather import Ui_Weather
from lcnar_transform import *
from DataBase import  DataBase
import random
import os
import pygame
pygame.init()

class NewDialog(QDialog):
    def closeEvent(self, event):
        result = QMessageBox.question(self, "提示", "你确定要退出吗?", 
                                        QMessageBox.Yes | QMessageBox.No)
        if(result == QMessageBox.Yes):
            pygame.mixer.music.stop()
            event.accept()
        else:
            event.ignore()
            
class Weather(NewDialog):
    
    def __init__(self):
        super(Weather,self).__init__()
        self.wea=Ui_Weather()
        self.wea.setupUi(self)
        self.db=DataBase()
        self.first()
        self.wea.query.clicked.connect(self.search)
        self.init_timer()
        self.wea.calendarWidget.clicked[QDate].connect(self.showDate)
        self.wea.calendarWidget.clicked[QDate].connect(self.note)
        self.wea.font.clicked.connect(self.select_font)
        self.wea.color.clicked.connect(self.select_color)
        self.play=True
        self.color=''
        self.font=QFont()
        self.icon = QIcon()
        self.musicList=[]
        datanames = os.listdir('music')
        for dataname in datanames:
            if os.path.splitext(dataname)[1] == '.mp3':
                self.musicList.append('music/'+dataname)
        pygame.mixer.music.load(random.choice(self.musicList))
        pygame.mixer.music.play(0)
        for i in range(len(self.musicList)):
            pygame.mixer.music.queue(random.choice(self.musicList))
        self.time=0.0
        self.wea.pushButton.clicked.connect(self.play_music)
    
    def play_music(self):
        if self.play==False:
            pygame.mixer.music.set_pos(self.time)
            pygame.mixer.music.unpause()
            self.play=True
            self.icon.addPixmap(QPixmap("img/暂停.png"), QIcon.Normal, QIcon.Off)
            self.wea.pushButton.setIcon(self.icon)
            self.wea.pushButton.setIconSize(QSize(20, 20))
        else:
            pygame.mixer.music.pause()
            self.time=pygame.mixer.music.get_pos()/1000
            self.play=False
            self.icon.addPixmap(QPixmap("img/播放.png"), QIcon.Normal, QIcon.Off)
            self.wea.pushButton.setIcon(self.icon)
            self.wea.pushButton.setIconSize(QSize(20, 20))
    
        
    def Warn(self):
        date=datetime.date.today()
        if self.db.getDate(str(date)):
            msg=self.db.getoneMsg(date)
            replay=QMessageBox.information(self,'提示',msg)
    
    def select_color(self):
        color=QColorDialog.getColor()
        if color.isValid():
            self.color=color.name()
            self.wea.widget_2.setStyleSheet('')
            self.wea.widget_2.setFont(self.font)
            self.wea.groupBox.setFont(self.font)
            self.wea.widget_2.setStyleSheet('QWidget {background-color:%s}'%self.color)
            
    
    def select_font(self):
        self.font,ok=QFontDialog.getFont()
        if ok:
            self.wea.widget_2.setStyleSheet('')
            self.wea.widget_2.setFont(self.font)
            self.wea.groupBox.setFont(self.font)
            self.wea.widget_2.setStyleSheet('QWidget {background-color:%s}'%self.color)
            
    def note(self):
        date1=datetime.date.today()
        date2=self.wea.calendarWidget.selectedDate()
        if str(date1)>=date2.toString('yyyy-MM-dd'):
            return 
        if self.db.getDate(date2.toString('yyyy-MM-dd')):
            messageBox = QMessageBox()
            messageBox.setWindowTitle('提示')
            messageBox.setText('已存在备忘录，是否删除重新创建')
            messageBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            buttonY = messageBox.button(QMessageBox.Yes)
            buttonY.setText('删除')
            buttonN = messageBox.button(QMessageBox.No)
            buttonN.setText('创建')
            messageBox.exec_()
            if messageBox.clickedButton() == buttonY:
                self.db.deleteMsg(date2.toString('yyyy-MM-dd'))
                replay=QMessageBox.information(self,'提示','删除备忘录成功')
                self.showMsg()
                return
            else:
                msg,ok=QInputDialog.getText(self,'输入','输入您的备忘录内容')
                if ok:
                    self.db.deleteMsg(date2.toString('yyyy-MM-dd'))
                    self.db.insertMsg(date2.toString('yyyy-MM-dd'), msg)
                    replay=QMessageBox.information(self,'提示','创建新的备忘录成功')
                    self.showMsg()
                    return
        replay=QMessageBox.information(self,'提示','是否创建备忘录',QMessageBox.Yes|QMessageBox.No)
        if replay==QMessageBox.Yes:
            msg,ok=QInputDialog.getText(self,'输入','输入您的备忘录内容')
            if ok:
                self.db.insertMsg(date2.toString('yyyy-MM-dd'), msg)
                replay=QMessageBox.information(self,'提示','创建备忘录成功')
                self.showMsg()
    
    def showMsg(self):
        date=datetime.date.today()
        result=self.db.getMsg(str(date))
        msg=''
        if result=='':
            self.wea.remember.setPlainText(result)
        else:
            for i in result:
                msg+=i[0]+'  '+i[1]+'\n'
            self.wea.remember.setPlainText(msg)
        
    def search(self):
        city=self.wea.city.text()
        result=WeaApi(city)
        self.wea.temp.setText('温度:'+result['temperature']+'℃  湿度：'+result['humidity'])
        weather=result['weather']
        self.wea.weather.setText(weather+' '+result['lim'])
        self.wea.wind.setText('风向:'+result['winddirection']+"  风力"+result['windpower'])
        path=insertPic(weather)
        self.wea.pic.setPixmap(QPixmap(path))
        
    def showDate(self):
        date=self.wea.calendarWidget.selectedDate()
        self.wea.week.setText(date.toString('dddd'))
        year,day,holiday,desc=trans(date.toString('yyyy-MM-dd'))
        self.wea.nongli.setText(str(year))
        self.wea.month.setText('农历'+str(day))
        self.wea.festival.setText(holiday)
        self.wea.tip.setText(desc)
        
    def first(self):
        self.showDate()
        self.wea.city.setText('宜春')
        result=WeaApi(self.wea.city.text())
        self.wea.temp.setText('温度:'+result['temperature']+'℃  湿度：'+result['humidity'])
        weather=result['weather']
        self.wea.weather.setText(weather+' '+result['lim'])
        self.wea.wind.setText('风向:'+result['winddirection']+"  风力"+result['windpower'])
        path=insertPic(weather)
        self.wea.pic.setPixmap(QPixmap(path))
        self.showMsg()
        self.Warn()
        
    def init_timer(self):
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.start()
        self.timer.timeout.connect(self.update_time)
 
    def update_time(self):
        self.wea.dateTimeEdit.setDateTime(QDateTime.currentDateTime())



#主程序
class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.ui=Weather()
        self.ui.show()
    
#启动程序
if __name__=="__main__":
    app=QApplication(sys.argv)
    win=Main()
    sys.exit(app.exec_())
