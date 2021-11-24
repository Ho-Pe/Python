# =================
# @brief 시간 계산 모듈
# @reporting date 21/11/24
# @last modified 21/11/24
# dev by Windows 10 (encoding : utf-8)
# =================

from datetime import datetime as DT
import keyboard

while True:
    if keyboard.read_key() == 'w':
        start_Time = DT.now()
        break

while True:
    if keyboard.read_key() == 'e':
        end_Time = DT.now()
        break

delta_Time = end_Time - start_Time

print(start_Time)
print(end_Time)
print(delta_Time)
print('Min delta :', round(delta_Time.seconds/60))