# file : p55_KatalkAuto.py
# desc : 카톡PC에서 자동으로 메시지 보내기

import pyautogui as auto
import pyperclip as clip
import os
import time

katalkLoc = auto.locateOnScreen('./day08/findLoc.png')
print(katalkLoc)
clickPos = auto.center(katalkLoc)
auto.click(clickPos)
time.sleep




