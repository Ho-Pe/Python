# ==
# @brief 로스트아크 낚시 알림
# @reporting date 21/07/11
# @last modified 21/07/13
# dev by Windows 10
# ==

import os
from playsound import playsound
import time
import sys
import pyautogui as pg

# == 
# @brief 화면 정중앙 좌표 체크
# @return size_Screen(화면 중앙 좌표)
# @last modified 21/07/11
# ==
def getCenterOfScreen():
    size_Screen = pg.size()
    size_Screen = (int(size_Screen[0]/2), int(size_Screen[1]/2))
    
    return size_Screen
    
# == 
# @brief 이미지 검출 영역 지정
# @param center$화면 중앙 좌표, width$"init.txt"파일의 width, height$"init.txt"파일의 height
# @return region$이미지 검출 영역
# @last modified 21/07/11
# ==
def makeRegion(center, width, height):
    x = center[0]
    y = center[1]
    
    startPos = (x - width, y - height)
    region = (startPos[0], startPos[1], 2*width, 2*height)
    
    return region
    
# ==
# @brief 이미지 검출
# @param fileName$이미지 파일 이름, startPos$makeRegion$리턴값, confidence$신뢰도
# @return result$검출된 이미지 좌표
# @last modified 21/07/14
# ==
def findImage(fileName, startPos, confidence):
    file_path = os.path.dirname(os.path.realpath(__file__)) + '\\' + 'img' + '\\' + fileName
    
    result = pg.locateOnScreen(file_path, confidence = confidence, region = startPos)
    
    return result
    
# ==
# @brief 이미지 검출 반복하기 위한 것
# @param fileName$이미지 파일 이름, startPos$makeRegion 리턴값, confidence$신뢰도
# @return img_Pos$findLocationWithImage의 리턴값인 검출된 이미지 좌표
# @last modified 21/07/13
# ==
def findImageRoop(fileName, startPos, confidence):
    result = findImage(fileName, startPos, confidence = confidence)
    
    return result
    
# ==
# @mainpage
# @brief 함수 실행 (테스트용)
# @details width와 height 값 가져오기, 영역 지정, 이미지 검출
# == 
# if __name__ == "__main__":        
    # width = FISHING_WIDTH
    # height = FISHING_HEIGHT
    
    # region = makeRegion(getCenterOfScreen(), width, height)
    
    # while True:
        # result = findImageRoop("five.png", region, 60, 0.8, 0.1)

        
        # if result != None:
            # playsound("alarm.mp3")
        # else:
            # print('못찾음')
            # break