# =================
# @brief 숙련도 저장 모듈
# @reporting date 21/11/24
# @last modified 21/11/30
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
# @param (str)name$사용자에게 입력받은 스킬 이름 by MySkillBook.py
# @last modified 21/11/30
# =================
def config_add(name):
    config_file = os.path.dirname(os.path.realpath(__file__)) + '\\' + 'config.ini'
    config = configparser.ConfigParser()
        
    config[name] = {}
    config[name]['타이틀'] = '초급'
    config[name]['숙련도'] = '0'
    config[name]['시간'] = '0'
    
    print('[스킬이름 : ' + name + ' | 타이틀 : 초급 | 숙련도 : 0%] 추가완료 되었습니다.', end='')
    input()
    
    with open('config.ini', 'a', encoding='utf-8') as config_file:
        config.write(config_file)

# =================
# @brief 숙련도 추가 모듈
# @param (str)name$사용자에게 입력받은 스킬 이름 by MySkillBook.py
# @last modified 21/11/30
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
                print('스킬 [' + name + '] 확인했습니다. 시간측정을 시작합니다.\n')
                delta_Time = TC.time_calc()
                config_Time = int(config[name]['시간'])
                config_Time = config_Time + delta_Time
                config[name]['시간'] = str(config_Time)
                
                be_config_pro = float(config[name]['숙련도'])
                
                if config[name]['타이틀'] == '초급':
                    be_config_pro = math.trunc(be_config_pro)
                    config_pro = math.trunc(config_Time/60)
                    print('숙련도가 ', end='')
                    print(config_pro - be_config_pro, end='')
                    print('% 증가하였습니다.')
                    if config_pro >= 100:
                        print('\n[!!!!!!!!!!!!!!!]')
                        print('숙련도가 ', end='')
                        print(config_pro, end='')
                        print('%를 달성하여 [' + name + ' - 중급]으로 진화하였습니다.')
                        config_pro = 0
                        config[name]['타이틀'] = '중급'
                        
                if config[name]['타이틀'] == '중급':
                    config_Time = config_Time - 6000
                    config_pro = math.trunc((config_Time / 60 * 0.1) * 10)/10
                    delta_config_pro = math.trunc((config_pro - be_config_pro)*10)/10
                    print('숙련도가 ', end='')
                    print(delta_config_pro, end='')
                    print('% 증가하였습니다.')
                    if config_pro >= 100.0:
                        print('\n[!!!!!!!!!!!!!!!]')
                        print('숙련도가 ', end='')
                        print(config_pro, end='')
                        print('%를 달성하여 [' + name + ' - 상급]으로 진화하였습니다.')
                        config_pro = 0
                        config[name]['타이틀'] = '상급'
                
                if config[name]['타이틀'] == '상급':
                    config_Time = config_Time - 66000
                    config_pro = math.trunc((config_Time / 60 * 0.1 / 3) * 10) / 10
                    delta_config_pro = math.trunc((config_pro - be_config_pro) * 10) / 10
                    print('숙련도가 ', end='')
                    print(delta_config_pro, end='')
                    print('% 증가하였습니다.')
                    
                config[name]['숙련도'] = str(config_pro)
                    
                with open('config.ini', 'w', encoding='utf-8') as config_file:
                    config.write(config_file)
                    
                input()
                os.system('cls')
                
        except KeyError:
            print('없는 스킬입니다.', end='')
            input()
            break

