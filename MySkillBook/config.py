# =================
# @brief 숙련도 저장 모듈
# @reporting date 21/11/24
# @last modified 21/11/24
# dev by Windows (encodig : utf-8)
# =================

import os
import configparser

# =================
# @brief 스킬 추가 모듈
# @last modified 21/11/24
# =================
def config_add():
    config_file = os.path.dirname(os.path.realpath(__file__)) + '\\' + 'skills.ini'
    config = configparser.ConfigParser()

    name = input('스킬이름 : ')
    config[name] = {}
    config[name]['title'] = '초심자'
    config[name]['proficiency'] = '0'
    
    print('[스킬이름 : ' + name + ' | 타이틀 : 초심자] 추가완료 되었습니다.\n\n')
    
    with open('config.ini', 'a', encoding='utf-8') as configfile:
        config.write(configfile)

# =================
# @brief 숙련도 추가 모듈
# last modified
# =================
