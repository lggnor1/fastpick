# cd C:\Users\User\OneDrive\문서\1111111111111\vsc\valorant_fastpick 
# pyinstaller --onefile --icon=icon.png main.py


import questionary
import pyautogui as a
import time
import keyboard

running = True
should_break = False

def on_break_hotkey():
    global should_break
    should_break = True
    print("\n[중지] Ctrl+Shift+D 감지")

def on_exit_hotkey():
    global running, should_break
    running = False
    should_break = True 
    print("\n[종료] Ctrl+Shift+Q 감지")
    keyboard.unhook_all()
    exit()

keyboard.add_hotkey('ctrl+shift+d', on_break_hotkey)
keyboard.add_hotkey('ctrl+shift+q', on_exit_hotkey)

while running:
    should_break = False
    
    name = questionary.select(
        message="select agent:",
        choices=[
            'jett',
            'neon',
            'reyna',
            'iso',
            'clove',
            'omen',
            'chamber',
            'cyhper',
            'killjoy',
            'sage',
            'sova',
            'test',
            'exit'
        ]
    ).ask()

    if name == "jett":
        time.sleep(0.3)
        while not should_break:
            a.click(400,550)
            a.click(950, 760)
            time.sleep(0.0001)

    if name == "neon":
        while not should_break:
            a.click(280,640)
            a.click(950, 760)
            time.sleep(0.0001)
    
    if name == "reyna":
        while not should_break:
            a.click(285,745)
            a.click(950, 760)
            time.sleep(0.0001)
    
    if name == "iso":
        while not should_break:
            a.click(290,550)
            a.click(950, 760)
            time.sleep(0.0001)
    
    if name == "clove":
        while not should_break:
            a.click(400,550)
            a.click(950, 760)
            time.sleep(0.0001)
    
    if name == "omen":
        while not should_break:
            a.click(390,640)
            a.click(950, 760)
            time.sleep(0.0001)
    
    if name == "chamber":
        while not should_break:
            a.click(385,350)
            a.click(950, 760)
            time.sleep(0.0001)
    
    if name == "cyhper":
        while not should_break:
            a.click(180,440)
            a.click(950, 760)
            time.sleep(0.0001)
    
    if name == "killjoy":
        while not should_break:
            a.click(185, 640) 
            a.click(950, 760)
            time.sleep(0.0001)
    
    if name == "sage":
        while not should_break:
            a.click(380, 745)
            a.click(950, 760)
            time.sleep(0.0001)
    
    if name == "sova":
        while not should_break:
            a.click(180, 845)
            a.click(950, 760)
            time.sleep(0.0001)
            
    if name == "test":
        while not should_break:
            print("test")
            time.sleep(1)

    if name == "exit":
        exit()
        keyboard.unhook_all()