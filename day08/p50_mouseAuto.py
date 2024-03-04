# file : p50_mouseAuto.py
# desc: PyuseGui로 마우스 조작

'''
파이썬 모듈 설치시는 명령 프롬프트보다 VSCode 내 터미널에서 설치를 추천
PyAutoGui 모듈 설치
> pip install pyautogui
'''

import pyautogui as auto

print(auto.size()) # 모니터 해상도 정보 Size(width=1920, height=1080)
print(auto.position())

# pyautogui 마우스 설정창
# pillow 모듈이 같이 설치되어야 색상 표시가능
#auto.mouseInfo()


## 마우스 이동(절대좌표)
auto.moveTo(100.51) #(0,0) 이후 이동이 안됨
auto.moveTo(615, 51, duration=1.0) # x축 678. y축 51로 1.0초동안 이동하라
auto.moveTo(1210,568, duration=0.1)

## 마우스 이동(상대좌표)
#auto.move(505,505, duration=1.5) # 현재위치에서 x축 500, y축 500으로 1.5초동안 이동하라

## 마우스 클릭
#auto.leftClick(x=615, y=51) # 해당위치로 가서 바로 왼쪽버튼 클리
#auto.rightClick(x=700, y=300)
auto.click(clicks=2, interval=0.1, button='left') # 왼쪽버튼을 소스코드 에디터에서 네번 선택하면 모든 글들을 전체선택

## 마우스 드래그
auto.leftClick(x=1422, y=168, duration=1.0) # 1422, 168에서 왼쪽마우스 클릭후 1초 대기했다가
auto.dragTo(x=983, y=550, duration=2.0, button='left')
auto.dragRel(500, 400, duration=2.0, button='left')# 현재위치에서 50, 400으로 1초 동안 드래그하라.

## 마우스 힐
auto.scroll(1000) # 양수는 위로
auto.scroll(-100) # 음수는 아래로 스크롤








