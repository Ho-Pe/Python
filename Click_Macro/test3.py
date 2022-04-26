# ================
# @brief 프롭 매크로
# @reporting date 21/12/19
# @last modified 21/12/19
# dev by Windows 10 (encoding : utf-8)
# ================

import pydirectinput as PI
import keyboard
import time

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
                keyboard.press('a')
                keyboard.release('a')
                keyboard.press('d')
                keyboard.release('d')
                time.sleep(0.0001)
    time.sleep(0.001)