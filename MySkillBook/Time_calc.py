# =================
# @brief 시간 계산 모듈
# @reporting date 21/11/24
# @last modified 21/11/30
# dev by Windows 10 (encoding : utf-8)
# =================

import os
import keyboard
import math
import configparser
import time
from datetime import datetime as DT

# =================
# @brief 시간 계산
# @return 시간의 분차이
# @last modified 21/11/29
# =================
def time_calc():
    start = DT.now()
    sign = input('끝났을떄 "end"를 입력하십시오.\n')
    if sign == 'end' or sign == 'END':
        end = DT.now()
    else:
        print('입력이 잘못되었습니다. 측정을 강제종료합니다.\n')
    delta_Time = end - start
    hour_delta_Time = math.trunc(delta_Time.seconds/3600)
    min_delta_Time = math.trunc(math.trunc(delta_Time.seconds%3600) / 60)
    
    if hour_delta_Time != 0:
        if min_delta_Time != 0:
            print('\n총 ', end='')
            print(hour_delta_Time, end='')
            print('시간 ', end='')
            print(min_delta_Time, end='')
            print('분이 측정되어 추가되었습니다.')
            
            return (hour_delta_Time*60) + min_delta_Time
            
        else:
            print('\n총 ', end='')
            print(hour_delta_Time, end='')
            print('시간이 측정되어 추가되었습니다.')
            
            return hour_delta_Time*60
    else:
        print('\n총 ', end='')
        print(min_delta_Time, end='')
        print('분이 측정되어 추가되었습니다.')
        
        return min_delta_Time
        
    # time_file = os.path.dirname(os.path.realpath(__file__)) + '\\' + 'time.ini'
    # time = configparser.ConfigParser()
    # time.read(time_file, 'utf-8')
    
    # if time_num == '1':
        # time['시간']['start'] = str(DT.now())
    # elif time_num == '2':
        # time['시간']['end'] = str(DT.now())

    # with open('time.ini', 'w', encoding='utf-8') as time_file:
        # time.write(time_file)

    # if time['시간']['start'] != '0' and time['시간']['end'] != '0':
       # start = int(time['시간']['start'])
       # print(start)
        
# delta_Time = end_Time - start_Time

# print(start_Time)
# print(end_Time)
# print(delta_Time)
# print('Min delta :', round(delta_Time.seconds/60))