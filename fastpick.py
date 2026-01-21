# pyinstaller --onefile  fastpick.py


import questionary
import pyautogui as a
import time
import keyboard
import random as r

running = True
should_break = False

def on_break_hotkey():
    global should_break
    should_break = True
    print("\n[break] Ctrl+Shift+S detected")

def on_exit_hotkey():
    global running, should_break
    running = False
    should_break = True 
    print("\n[exit] Ctrl+Shift+Q detected")
    keyboard.unhook_all()
    exit()

keyboard.add_hotkey('ctrl+shift+s', on_break_hotkey)
keyboard.add_hotkey('ctrl+shift+q', on_exit_hotkey)


class Korean:
    def run(self):
        # 여기에 한국어 버전 코드 작성
        pass


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
                    'Exit'
                ]
            ).ask()

            if name == "Random":
                n = r.randrange(1, 29)
                
                if n == 1:  # Astra
                    while not should_break:
                        a.click(90, 350)
                        a.click(950, 760)
                        time.sleep(0.0001)
                
                if n == 2:  # Breach
                    while not should_break:
                        a.click(180, 350)
                        a.click(950, 760)
                        time.sleep(0.0001)
                
                if n == 3:  # Brimstone
                    while not should_break:
                        a.click(300, 350)
                        a.click(950, 760)
                        time.sleep(0.0001)
                
                if n == 4:  # Chamber
                    while not should_break:
                        a.click(400, 350)
                        a.click(950, 760)
                        time.sleep(0.0001)
                
                if n == 5:  # Clove
                    while not should_break:
                        a.click(90, 450)
                        a.click(950, 760)
                        time.sleep(0.0001)
                
                if n == 6:  # Cypher
                    while not should_break:
                        a.click(180, 450)
                        a.click(950, 760)
                        time.sleep(0.0001)
                
                if n == 7:  # Deadlock
                    while not should_break:
                        a.click(300, 450)
                        a.click(950, 760)
                        time.sleep(0.0001)
                
                if n == 8:  # Fade
                    while not should_break:
                        a.click(400, 450)
                        a.click(950, 760)
                        time.sleep(0.0001)
                
                if n == 9:  # Gekko
                    while not should_break:
                        a.click(90, 550)
                        a.click(950, 760)
                        time.sleep(0.0001)
                
                if n == 10:  # Harbor
                    while not should_break:
                        a.click(180, 550)
                        a.click(950, 760)
                        time.sleep(0.0001)
                
                if n == 11:  # Iso
                    while not should_break:
                        a.click(300, 550)
                        a.click(950, 760)
                        time.sleep(0.0001)
                
                if n == 12:  # Jett
                    while not should_break:
                        a.click(400, 550)
                        a.click(950, 760)
                        time.sleep(0.0001)
                
                if n == 13:  # KAY/O
                    while not should_break:
                        a.click(90, 650)
                        a.click(950, 760)
                        time.sleep(0.0001)
                
                if n == 14:  # Killjoy
                    while not should_break:
                        a.click(180, 650)
                        a.click(950, 760)
                        time.sleep(0.0001)
                
                if n == 15:  # Neon
                    while not should_break:
                        a.click(300, 650)
                        a.click(950, 760)
                        time.sleep(0.0001)
                
                if n == 16:  # Omen
                    while not should_break:
                        a.click(400, 650)
                        a.click(950, 760)
                        time.sleep(0.0001)
                
                if n == 17:  # Phoenix
                    while not should_break:
                        a.click(90, 750)
                        a.click(950, 760)
                        time.sleep(0.0001)
                
                if n == 18:  # Raze
                    while not should_break:
                        a.click(180, 750)
                        a.click(950, 760)
                        time.sleep(0.0001)
                
                if n == 19:  # Reyna
                    while not should_break:
                        a.click(300, 750)
                        a.click(950, 760)
                        time.sleep(0.0001)
                
                if n == 20:  # Sage
                    while not should_break:
                        a.click(400, 750)
                        a.click(950, 760)
                        time.sleep(0.0001)
                
                if n == 21:  # Skye
                    while not should_break:
                        a.click(90, 850)
                        a.click(950, 760)
                        time.sleep(0.0001)
                
                if n == 22:  # Sova
                    while not should_break:
                        a.click(180, 850)
                        a.click(950, 760)
                        time.sleep(0.0001)
                
                if n == 23:  # Tejo
                    while not should_break:
                        a.click(300, 850)
                        a.click(950, 760)
                        time.sleep(0.0001)
                
                if n == 24:  # Veto
                    while not should_break:
                        a.click(400, 850)
                        a.click(950, 760)
                        time.sleep(0.0001)
                
                if n == 25:  # Viper
                    while not should_break:
                        a.click(90, 850)
                        a.click(950, 760)
                        time.sleep(0.0001)
                
                if n == 26:  # Vyse
                    while not should_break:
                        a.click(180, 850)
                        a.click(950, 760)
                        time.sleep(0.0001)
                
                if n == 27:  # Waylay
                    while not should_break:
                        a.click(300, 850)
                        a.click(950, 760)
                        time.sleep(0.0001)
                
                if n == 28:  # Yoru
                    while not should_break:
                        a.click(400, 850)
                        a.click(950, 760)
                        time.sleep(0.0001)

            if name == "Astra":
                while not should_break:
                    a.click(90, 350)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "Breach":
                while not should_break:
                    a.click(180, 350)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "Brimstone":
                while not should_break:
                    a.click(300, 350)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "Chamber":
                while not should_break:
                    a.click(400,350)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "Clove":
                while not should_break:
                    a.click(90, 450)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "Cypher":
                while not should_break:
                    a.click(180, 450)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "Deadlock":
                while not should_break:
                    a.click(300, 450)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "Fade":
                while not should_break:
                    a.click(400, 450)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "Gekko":
                while not should_break:
                    a.click(90, 550)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "Harbor":
                while not should_break:
                    a.click(180, 550)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "Iso":
                while not should_break:
                    a.click(300,550)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "Jett":
                while not should_break:
                    a.click(400,550)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "KAY/O":
                while not should_break:
                    a.click(90, 650)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "Killjoy":
                while not should_break:
                    a.click(180, 650) 
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "Neon":
                while not should_break:
                    a.click(300, 650)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "Omen":
                while not should_break:
                    a.click(400, 650)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "Phoenix":
                while not should_break:
                    a.click(90, 750)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "Raze":
                while not should_break:
                    a.click(180, 750)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "Reyna":
                while not should_break:
                    a.click(300, 750)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "Sage":
                while not should_break:
                    a.click(400, 750)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "Skye":
                while not should_break:
                    a.click(90, 850)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "Sova":
                while not should_break:
                    a.click(180, 850)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "Tejo":
                while not should_break:
                    a.click(300, 850)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "Veto":
                while not should_break:
                    a.click(400, 850)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "Viper":
                while not should_break:
                    a.moveTo(250, 500)
                    a.scroll(-300)  
                    a.click(90, 850)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "Vyse":
                while not should_break:
                    a.moveTo(250, 500)
                    a.scroll(-300)  
                    a.click(180, 850)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "Waylay":
                while not should_break:
                    a.moveTo(250, 500)
                    a.scroll(-300)  
                    a.click(300, 850)
                    a.click(950, 760)
                    time.sleep(0.0001)

            if name == "Yoru":
                while not should_break:
                    a.moveTo(250, 500)
                    a.scroll(-300)  
                    a.click(400, 850)
                    a.click(950, 760)
                    time.sleep(0.0001)
            
            
            
            if name == "exit":
                exit()
                keyboard.unhook_all()


# 언어 선택
language = questionary.select(
    message="Select language:",
    choices=['English', 'Korean']
).ask()

if language == 'English':
    English().run()
elif language == 'Korean':
    Korean().run()
