# pyinstaller --onefile  fastpick.py


import questionary
import pyautogui as a
import time
import keyboard
import random as r
import threading
import os

running = True
should_break = False

def on_break_hotkey():
    global should_break
    should_break = True
    time.sleep(0.5)
    os.system('cls')
    print("\n[break] Ctrl+Shift+Z detected")

def on_exit_hotkey():
    global running, should_break
    running = False
    should_break = True 
    print("\n[exit] Ctrl+Shift+Q detected")
    keyboard.unhook_all()
    exit()

keyboard.add_hotkey('ctrl+shift+z', on_break_hotkey)
keyboard.add_hotkey('ctrl+shift+q', on_exit_hotkey)


def auto_stop_timer(seconds=10):
    """지정된 초 후에 자동으로 정지"""
    global should_break
    time.sleep(seconds)
    if not should_break:
        should_break = True
        print(f"\n[auto-stop] {seconds}초 경과, 자동 정지됨")
        time.sleep(0,5)
    os.system('cls')


def start_auto_stop(seconds=10):
    """백그라운드에서 자동 정지 타이머 시작"""
    global should_break
    should_break = False
    t = threading.Thread(target=auto_stop_timer, args=(seconds,), daemon=True)
    t.start()


def random_pick():
    n = r.randrange(1, 29)
    start_auto_stop(10)
    
    if n == 1:
        while not should_break:
            a.click(90, 350)
            a.click(950, 760)
            time.sleep(0.0001)
    
    if n == 2:
        while not should_break:
            a.click(180, 350)
            a.click(950, 760)
            time.sleep(0.0001)
    
    if n == 3:
        while not should_break:
            a.click(300, 350)
            a.click(950, 760)
            time.sleep(0.0001)
    
    if n == 4:
        while not should_break:
            a.click(400, 350)
            a.click(950, 760)
            time.sleep(0.0001)
    
    if n == 5: 
        while not should_break:
            a.click(90, 450)
            a.click(950, 760)
            time.sleep(0.0001)
    
    if n == 6:  
        while not should_break:
            a.click(180, 450)
            a.click(950, 760)
            time.sleep(0.0001)
    
    if n == 7: 
        while not should_break:
            a.click(300, 450)
            a.click(950, 760)
            time.sleep(0.0001)
    
    if n == 8:
        while not should_break:
            a.click(400, 450)
            a.click(950, 760)
            time.sleep(0.0001)
    
    if n == 9:  
        while not should_break:
            a.click(90, 550)
            a.click(950, 760)
            time.sleep(0.0001)
    
    if n == 10: 
        while not should_break:
            a.click(180, 550)
            a.click(950, 760)
            time.sleep(0.0001)
    
    if n == 11:
        while not should_break:
            a.click(300, 550)
            a.click(950, 760)
            time.sleep(0.0001)
    
    if n == 12:
        while not should_break:
            a.click(400, 550)
            a.click(950, 760)
            time.sleep(0.0001)
    
    if n == 13: 
        while not should_break:
            a.click(90, 650)
            a.click(950, 760)
            time.sleep(0.0001)
    
    if n == 14:
        while not should_break:
            a.click(180, 650)
            a.click(950, 760)
            time.sleep(0.0001)
    
    if n == 15:
        while not should_break:
            a.click(300, 650)
            a.click(950, 760)
            time.sleep(0.0001)
    
    if n == 16:
        while not should_break:
            a.click(400, 650)
            a.click(950, 760)
            time.sleep(0.0001)
    
    if n == 17:
        while not should_break:
            a.click(90, 750)
            a.click(950, 760)
            time.sleep(0.0001)
    
    if n == 18: 
        while not should_break:
            a.click(180, 750)
            a.click(950, 760)
            time.sleep(0.0001)
    
    if n == 19:  
        while not should_break:
            a.click(300, 750)
            a.click(950, 760)
            time.sleep(0.0001)
    
    if n == 20:  
        while not should_break:
            a.click(400, 750)
            a.click(950, 760)
            time.sleep(0.0001)
    
    if n == 21:
        while not should_break:
            a.click(90, 850)
            a.click(950, 760)
            time.sleep(0.0001)
    
    if n == 22:
        while not should_break:
            a.click(180, 850)
            a.click(950, 760)
            time.sleep(0.0001)
    
    if n == 23: 
        while not should_break:
            a.click(300, 850)
            a.click(950, 760)
            time.sleep(0.0001)
    
    if n == 24: 
        while not should_break:
            a.click(400, 850)
            a.click(950, 760)
            time.sleep(0.0001)
    
    if n == 25:
        while not should_break:
            a.click(450, 850)
            time.sleep(0.01)
            a.click(90, 950)
            a.click(950, 760)
            time.sleep(0.0001)
    
    if n == 26:
        while not should_break:
            a.click(450, 850)
            time.sleep(0.01)
            a.click(180, 950)
            a.click(950, 760)
            time.sleep(0.0001)
    
    if n == 27:
        while not should_break:
            a.click(450, 850)
            time.sleep(0.01)
            a.click(300, 950)
            a.click(950, 760)
            time.sleep(0.0001)
    
    if n == 28:
        while not should_break:
            a.click(450, 850)
            time.sleep(0.01)
            a.click(400, 950)
            a.click(950, 760)
            time.sleep(0.0001)


class Korean:
    def run(self):
        global should_break
        while running:
            should_break = False
            
            name = questionary.select(
                message="select agent:",
                choices=[
                        '랜덤',
                        '게코', 
                        '네온',
                        '데드록',
                        '레이나',
                        '레이즈',
                        '바이퍼',
                        '바이스',
                        '브림스톤',
                        '브리치',
                        '비토'
                        '사이퍼',
                        '세이지',
                        '소바',
                        '스카이',
                        '아스트라',
                        '아이소',
                        '오멘',
                        '요루',
                        '웨이레이', 
                        '제트',
                        '체임버',
                        '클로브',
                        '킬조이',
                        '케이오',
                        '테호',
                        '페이드',
                        '피닉스',
                        '하버',
                        '뒤로가기/Back',
                        '나가기/Exit'
    
                ]
            ).ask()
            
            if name == "랜덤":
                random_pick()

            if name == "게코":
                start_auto_stop(10)
                while not should_break:
                    a.click(90, 350)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "네온":
                start_auto_stop(10)
                while not should_break:
                    a.click(180, 350)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "데드록":
                start_auto_stop(10)
                while not should_break:
                    a.click(300, 350)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "레이나":
                start_auto_stop(10)
                while not should_break:
                    a.click(400,350)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "레이즈":
                start_auto_stop(10)
                while not should_break:
                    a.click(90, 450)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "바이퍼":
                start_auto_stop(10)
                while not should_break:
                    a.click(180, 450)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "바이스":
                start_auto_stop(10)
                while not should_break:
                    a.click(300, 450)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "브림스톤":
                start_auto_stop(10)
                while not should_break:
                    a.click(400, 450)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "브리치":
                start_auto_stop(10)
                while not should_break:
                    a.click(90, 550)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "비토":
                start_auto_stop(10)
                while not should_break:
                    a.click(180, 550)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "사이퍼":
                start_auto_stop(10)
                while not should_break:
                    a.click(300,550)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "세이지":
                start_auto_stop(10)
                while not should_break:
                    a.click(400,550)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "소바":
                start_auto_stop(10)
                while not should_break:
                    a.click(90, 650)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "스카이":
                start_auto_stop(10)
                while not should_break:
                    a.click(180, 650) 
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "아스트라":
                start_auto_stop(10)
                while not should_break:
                    a.click(300, 650)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "아이소":
                start_auto_stop(10)
                while not should_break:
                    a.click(400, 650)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "오멘":
                start_auto_stop(10)
                while not should_break:
                    a.click(90, 750)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "요루":
                start_auto_stop(10)
                while not should_break:
                    a.click(180, 750)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "웨이레이":
                start_auto_stop(10)
                while not should_break:
                    a.click(300, 750)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "제트":
                start_auto_stop(10)
                while not should_break:
                    a.click(400, 750)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "체임버":
                start_auto_stop(10)
                while not should_break:
                    a.click(90, 850)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "클로브":
                start_auto_stop(10)
                while not should_break:
                    a.click(180, 850)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "킬조이":
                start_auto_stop(10)
                while not should_break:
                    a.click(300, 850)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "케이오":
                start_auto_stop(10)
                while not should_break:
                    a.click(400, 850)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "테호":
                start_auto_stop(10)
                while not should_break:
                    a.click(450, 850)
                    time.sleep(0.01)
                    a.click(90, 850)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "페이드":
                start_auto_stop(10)
                while not should_break:
                    a.click(450, 850)
                    time.sleep(0.01)
                    a.click(180, 850)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "피닉스":
                start_auto_stop(10)
                while not should_break:
                    a.click(450, 850)
                    time.sleep(0.01)
                    a.click(300, 850)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "하버":
                start_auto_stop(10)
                while not should_break:
                    a.click(450, 850)
                    time.sleep(0.01)
                    a.click(400, 850)
                    a.click(950, 760)
                    time.sleep(0.0001)
            
            
            if name == "뒤로가기/Back":
                language = questionary.select(
                    message="Select language:",
                    choices=['English', 'Korean']
                ).ask()

                if language == 'English':
                    English().run()
                elif language == 'Korean':
                    Korean().run()
            
            if name == "나가기/Exit":
                exit()
                keyboard.unhook_all()


class English:
    def run(self):
        global should_break
        while running:
            should_break = False
            
            name = questionary.select(
                message="select agent:",
                choices=[
                    'Random',
                    'Astra',
                    'Breach',
                    'Brimstone',
                    'Chamber',
                    'Clove',
                    'Cypher',
                    'Deadlock',
                    'Fade',
                    'Gekko',
                    'Harbor',
                    'Iso',
                    'Jett',
                    'KAY/O',
                    'Killjoy',
                    'Neon',
                    'Omen',
                    'Phoenix',
                    'Raze',
                    'Reyna',
                    'Sage',
                    'Skye',
                    'Sova',
                    'Tejo',
                    'Veto',
                    'Viper',
                    'Vyse',
                    'Waylay',
                    'Yoru',
                    'Back',
                    'Exit'
                ]
            ).ask()

            if name == "Random":
                random_pick()

            if name == "Astra":
                start_auto_stop(10)
                while not should_break:
                    a.click(90, 350)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "Breach":
                start_auto_stop(10)
                while not should_break:
                    a.click(180, 350)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "Brimstone":
                start_auto_stop(10)
                while not should_break:
                    a.click(300, 350)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "Chamber":
                start_auto_stop(10)
                while not should_break:
                    a.click(400,350)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "Clove":
                start_auto_stop(10)
                while not should_break:
                    a.click(90, 450)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "Cypher":
                start_auto_stop(10)
                while not should_break:
                    a.click(180, 450)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "Deadlock":
                start_auto_stop(10)
                while not should_break:
                    a.click(300, 450)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "Fade":
                start_auto_stop(10)
                while not should_break:
                    a.click(400, 450)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "Gekko":
                start_auto_stop(10)
                while not should_break:
                    a.click(90, 550)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "Harbor":
                start_auto_stop(10)
                while not should_break:
                    a.click(180, 550)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "Iso":
                start_auto_stop(10)
                while not should_break:
                    a.click(300,550)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "Jett":
                start_auto_stop(10)
                while not should_break:
                    a.click(400,550)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "KAY/O":
                start_auto_stop(10)
                while not should_break:
                    a.click(90, 650)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "Killjoy":
                start_auto_stop(10)
                while not should_break:
                    a.click(180, 650) 
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "Neon":
                start_auto_stop(10)
                while not should_break:
                    a.click(300, 650)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "Omen":
                start_auto_stop(10)
                while not should_break:
                    a.click(400, 650)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "Phoenix":
                start_auto_stop(10)
                while not should_break:
                    a.click(90, 750)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "Raze":
                start_auto_stop(10)
                while not should_break:
                    a.click(180, 750)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "Reyna":
                start_auto_stop(10)
                while not should_break:
                    a.click(300, 750)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "Sage":
                start_auto_stop(10)
                while not should_break:
                    a.click(400, 750)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "Skye":
                start_auto_stop(10)
                while not should_break:
                    a.click(90, 850)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "Sova":
                start_auto_stop(10)
                while not should_break:
                    a.click(180, 850)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "Tejo":
                start_auto_stop(10)
                while not should_break:
                    a.click(300, 850)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "Veto":
                start_auto_stop(10)
                while not should_break:
                    a.click(400, 850)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "Viper":
                start_auto_stop(10)
                while not should_break:
                    a.click(450, 850)
                    time.sleep(0.01)
                    a.click(90, 850)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "Vyse":
                start_auto_stop(10)
                while not should_break:
                    a.click(450, 850)
                    time.sleep(0.01)
                    a.click(180, 850)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "Waylay":
                start_auto_stop(10)
                while not should_break:
                    a.click(450, 850)
                    time.sleep(0.01)
                    a.click(300, 850)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "Yoru":
                start_auto_stop(10)
                while not should_break:
                    a.click(450, 850)
                    time.sleep(0.01)
                    a.click(400, 850)
                    a.click(950, 760)
                    time.sleep(0.0001)
            
            if name == "Back":
                language = questionary.select(
                    message="Select language:",
                    choices=['English', 'Korean']
                ).ask()

                if language == 'English':
                    English().run()
                elif language == 'Korean':
                    Korean().run()
            
            if name == "Exit":
                exit()
                keyboard.unhook_all()



language = questionary.select(
    message="Select language:",
    choices=['English', 'Korean']
).ask()

if language == 'English':
    English().run()
elif language == 'Korean':
    Korean().run()
