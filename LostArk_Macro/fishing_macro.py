# ==
# @brief 로스트아크 낚시 완전 자동
# @reporting date 21/09/28
# @last modified 21/09/28
# dev by Windows 10
# ==

import sys
import os
import time
import fishing_alarm as fg
import pyautogui as pg
from playsound import playsound
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
from config import *

# ==
# @Thread class
# @brief 이미지 검출 스레드
# @details 쓰레드를 실행시키면 이미지 범위 설정, 이미지 검출이 시작된다.
# @param QThread
# @last modified 21/09/28
# ==
class Thread1(QtCore.QThread):
    def __init__(self, parent):
        super().__init__(parent)
        
    # == 
    # @brief 스레드 실행
    # @param self
    # @last modified 21/09/28
    # --
    def run(self):
        self.working = True
        self.width = FISHING_WIDTH
        self.height = FISHING_HEIGHT
        
        self.region = fg.makeRegion(fg.getCenterOfScreen(), self.width, self.height)
        
        while self.working:
            self.result = fg.findImageRoop("fishing_point.png", self.region, 0.5)
            time.sleep(0.1)
            if self.result != None:
                pg.press('w')
                sound_path = os.path.dirname(os.path.realpath(__file__)) + '\\' + 'alarm.mp3'
                playsound(sound_path)
                # self.recorded = keyboard.record(until = 'w')
                time.sleep(5)
                # keyboard.play(self.recorded, speed_factor=3)
                pg.press('w')

            
    # == 
    # @brief 스레드 중지
    # @param self
    # @last modifeid 21/09/28
    # ==
    def stop(self):
        self.working = False
        self.quit()
        
# ==
# @class
# @brief 메인윈도우 클래스
# @details 기본 화면
# ==
class Main_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.thread = Thread1(self)
        
        self.initUI()

    # ==
    # @brief 기본 UI 창 설정
    # @param self
    # @last modified 21/09/28
    # ==
    def initUI(self):
        self.setWindowTitle('로스트아크 낚시 알리미')
        self.setGeometry(0, 0, 300, 100)
        self.setFixedSize(300, 100)
        self.setStyleSheet("QMainWindow{background-color: rgb(205, 209, 255);}")
        self.icon_path = os.path.dirname(os.path.realpath(__file__)) + '\\' + 'fishing.ico'
        self.setWindowIcon(QIcon(self.icon_path))
        
        # ==
        # @brief PushButton - 알림 활성 버튼
        # @last modified 21/09/28
        # ==
        self.Btn = QPushButton("", self)
        self.Btn.setGeometry(20, 10, 100, 80)
        self.Btn_path = os.path.dirname(os.path.realpath(__file__)) + '\\' + 'img' + '\\' + 'lostark.png'
        self.Btn.setIcon(QtGui.QIcon(self.Btn_path))
        self.Btn.setIconSize(QSize(120, 120))
        self.Btn.setCheckable(True)
        self.Btn.clicked.connect(self.Btn_Clicked)
        
        # ==
        # @brief ON/OFF 표시
        # @last modified 21/09/28
        # --
        self.Label = QLabel(self)
        self.Label.setFont(QtGui.QFont('HY견고딕', 10, weight=QtGui.QFont.Bold))
        self.Label.setText("Off")
        self.Label.setGeometry(190, 5, 100, 100)
        
        self.update()
        self.show()

    # ==
    # @brief Btn 클릭 이벤트
    # @parma selfz
    # @last modified 21/09/28
    # == 
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