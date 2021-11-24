# ==
# @brief 로스트아크 낚시 알림 GUI
# @reporting date 21/07/12
# @last modified 21/07/12
# dev by Windows 10
# ==

import sys
import os
import time
import fishing_alarm as fg
from playsound import playsound
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
from config import *

class Thread1(QtCore.QThread):
    def __init__(self, parent):
        super().__init__(parent)
    def run(self):
        self.working = True
        self.width = FISHING_WIDTH
        self.height = FISHING_HEIGHT
            
        self.region = fg.makeRegion(fg.getCenterOfScreen(), self.width, self.height)
        
        while self.working:
            self.result = fg.findImageRoop("five.png", self.region, 0.8)
            time.sleep(0.1)
            
            if self.result != None:
                playsound("alarm.mp3")
                time.sleep(3)
            
    def stop(self):
        self.working = False
        self.quit()
        

# ==
# @class - 1
# @brief 메인윈도우 클래스
# @details 기본 화면
# ==
class Main_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.thread = Thread1(self)
        
        self.initUI()

# ==
# @brief 1 - 기본 UI 창 설정
# @param self
# @last modified 21/07/12
# ==
    def initUI(self):
        self.setWindowTitle('로스트아크 낚시 알리미')
        self.setGeometry(0, 0, 700, 200)
        self.setFixedSize(700, 300)
        self.setStyleSheet("QMainWindow{background-color: rgb(205, 209, 255);}")
        
        # ==
        # @brief PushButton - 알림 활성 버튼
        # @last modified 21/07/12
        # ==
        self.Btn = QPushButton("", self)
        self.Btn.setGeometry(60, 50, 160, 170)
        self.Btn.setStyleSheet("background-image : url(./img/lostark.png);")
        self.Btn.setCheckable(True)
        self.Btn.clicked.connect(self.Btn_Clicked)
        
        # ==
        # @brief ON/OFF 표시
        # @last modified 21/07/12
        # --
        self.Label = QLabel(self)
        self.Label.setStyleSheet("font : 20pt \"HY견고딕\"; font-weight : bold;")
        self.Label.setText("Off")
        self.Label.setGeometry(400, 80, 500, 100)
        
        self.update()
        self.show()

        
    def Btn_Clicked(self):
        if self.Btn.isChecked():
            self.Label.setText("On")
            self.thread.start()
        else:
            self.Label.setText("Off")
            self.thread.stop()
        
# ==
# @mainpage
# @brief 메인
# @details 화면 출력
# ==
if __name__ == '__main__':
    app = QApplication(sys.argv)
    output = Main_Window()
    app.exec_()