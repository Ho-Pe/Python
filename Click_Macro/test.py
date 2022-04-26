# ================
# @brief 마우스 클릭 매크로
# @reporting date 21/12/17
# @last modified 21/12/19
# dev by Windows 10 (encoding : utf-8)
# ================

import pydirectinput as PI
import mouse
import keyboard
import time
import win32api

while True:
    if keyboard.is_pressed('x'):
        keyboard.write('')
        print('on')
        while True:
            if keyboard.is_pressed('x'):
                keyboard.write('')
                print('off')
                break
            else:
                PI.click()
                time.sleep(0.001)
                
    time.sleep(0.001)