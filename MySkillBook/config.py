# =================
# @brief 숙련도 저장 모듈
# @reporting date 21/11/24
# @last modified 21/11/29
# dev by Windows (encodig : utf-8)
# =================

import os
import math
import configparser
import time
import Time_calc as TC

# =================
# @brief 스킬 파일 읽는 모듈
# @last modified 21/11/27
# =================
def config_output():
    config_file = os.path.dirname(os.path.realpath(__file__)) + '\\' + 'config.ini'
    config = configparser.ConfigParser()
    config.read(config_file, 'utf-8')
    
    sections = config.sections()
    
    for section in sections:
        cnt = 0
        print(f'[{section}', end='')
        for key, value in config.items(section):
            if cnt == 0:
                print(' - ' + value + ']')
            elif cnt == 1:
                print('숙련도 : ' + value + '%')
            else:
                time = math.trunc(int(config[section]['시간']) / 60)
                m = int(config[section]['시간']) % 60
                print('시간 : ', end='')
                print(time, end='')
                print('시간 ', end='')
                print(m, end='')
                print('분')
            cnt = cnt + 1
        print('--------------------------------\n')
        

# =================
# @brief 스킬 추가 모듈
# @last modified 21/11/27
# =================
def config_add(name):
    config_file = os.path.dirname(os.path.realpath(__file__)) + '\\' + 'config.ini'
    config = configparser.ConfigParser()

    config[name] = {}
    config[name]['타이틀'] = '초심자'
    config[name]['숙련도'] = '0'
    config[name]['시간'] = '0'
    
    print('[스킬이름 : ' + name + ' | 타이틀 : 초심자 | 숙련도 : 0%] 추가완료 되었습니다.\n\n')
    
    with open('config.ini', 'a', encoding='utf-8') as config_file:
        config.write(config_file)

# =================
# @brief 숙련도 추가 모듈
# @last modified 21/11/29
# =================
def config_up(name):
    config_file = os.path.dirname(os.path.realpath(__file__)) + '\\' + 'config.ini'
    config = configparser.ConfigParser()
    config.read(config_file, 'utf-8')
    
    sections = config.sections()
    print('스킬 [' + name + '] 검색...')
    time.sleep(2)
    
    for section in sections:
        try:
            if config[name] == config[section]:
                os.system('cls')
                print('[!!!!!!!!!!!!!!!]\n')
                print('스킬 [' + name + ']을 찾았습니다. 시간측정을 시작합니다.\n')
                delta_Time = TC.time_calc()
                config_Time = int(config[name]['시간'])
                config_Time = config_Time + delta_Time
                config[name]['시간'] = str(config_Time)
                
                with open('config.ini', 'w', encoding='utf-8') as config_file:
                    config.write(config_file)
                
                input()
                os.system('cls')
                
        except KeyError:
            print('없는 스킬입니다.', end='')
            input()
            break    
