# file : p54_capWeather.py
# desc : 네이버 날씨화면 캡쳐

import pyautogui as auto
import pyperclip as clip
import time

regions= ['서울', '강원', '대전', '대구', '부산'] 
# auto.mouseInfo()
for region in regions :
    auto.moveTo(258, 150, duration=0.5)
    auto.leftClick()
    for _ in range(5):
        auto.press('backspace')
    time.sleep(0.2)

    clip.copy(f'{region}날씨')
    auto.hotkey('ctrl','v')# 붙여넣기
    time.sleep(0.2)

    auto.press('\n') # enter도 가능
    time.sleep(1.0)
    # 75,264 / 746,911

    startX, startY = 30,276
    endX, endY = 700, 921
    # auto.screenshot() 만 사용하면 macos에서 동작 안함
    auto.screenshot(f'./day08/{region}날씨.png', 
                    region=(startX, startY, endX-startX, endY-startY))

    print('저장완료!')
