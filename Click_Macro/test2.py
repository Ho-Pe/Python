# ================
# @brief 마우스 클릭 매크로 2
# @reporting date 21/12/17
# @last modified 21/12/18
# dev by Windows 10 (encoding : utf-8)
# ================

import pydirectinput as PI
import keyboard
import time
import win32api
import mouse

while True:
    if keyboard.is_pressed('x'):
        keyboard.write('')
        print('on')
        while True:
            if mouse.is_pressed('right') and mouse.is_pressed('left'):
            # if win32api.GetKeyState(0x02) <0:
                while True:
                    if win32api.GetKeyState(0x02) >= 0:
                        break
                    else:
                        PI.click()
                        time.sleep(0.001)
            if mouse.is_pressed('left'):
                while True:
                    if win32api.GetKeyState(0x02) < 0:
                        break
                        
                    else:
                        PI.click()
                        time.sleep(0.01)
            if keyboard.is_pressed('x'):
                keyboard.write('')
                print('off')
                break
                
            time.sleep(0.001)
    time.sleep(0.001)