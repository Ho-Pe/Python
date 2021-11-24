# =================
# @brief MySkillBook
# @reporting date 21/11/24
# @last modified 21/11/24
# dev by Windows 10 (encoding : utf-8)
# =================

import os
import sys
import config as CF

# =================
# @brief 화면 출력
# @last modified 21/11/24
# =================
def screen_output():
    os.system('cls')
    print('\n--------------------')
    print('My Skill Book Open')
    print('--------------------')
    print('---------------------------[스킬목록]---------------------------')
    print('\n\n1번 - 스킬 추가')
    print('2번 - 숙련도 업')
    print('3번 - 끝내기\n\n')

# =================
# @brief 총괄 모듈
# @param 
# @return 
# @last modified 21/11/24
# =================
def generator():
    screen_output()
    while True:
        menu_input = input('뭘 하시겠습니까? - ')
        if menu_input == '1':
            CF.config_add()
        # elif menu_input == '2':
        elif menu_input == '3':
            os.system('cls')
            print('\n--------------------')
            print('My Skill Book Closed')
            print('--------------------')
            sys.exit()
        else:
            print('다시 입력행!\n\n')
    

# =================
# @mainpage
# @brief 메인
# =================
if __name__ == "__main__":
    generator()