# file: p30_standardLib.py
# desc: 표준 라이브러리(빌트인) 학습

import datetime
import time
import random

print(datetime.date(2024, 2, 26)) # 현재의 OS에 맞춰서 날짜형으로 변경

## 정말 많이 씀
curr = datetime.datetime.now() # 현재의 년월일시분초를 알려줌
print(curr)

print(curr.weekday()) # 0 월요일 ~ 6 일요일
print(curr.year)
print(curr.month)
print(curr.day)
print(curr.hour)
print(curr.minute)
print(curr.second)

print(f'{curr.year}년 {curr.month:02d}월 {curr.day}일 {curr.hour}시 {curr.minute}분')

curr2 = time.localtime() # time으로 찾는 locatime() 잘 안쓰임.
print(curr2)

## 많이 쓰임(sleep)
for i in range(5):
    print(f'{i} 출력')
    # time.sleep(2) # 2초씩 잠시 멈춤


## random
print(random.random()) # 0~1사이의 소수점 랜덤수
print(random.randint(1, 45)) # 1부터 45까지 임의로 숫자를 출력

## 로또
result = []
total = []
for i in range(5):
    while True: # 무한루프 시작
        val = random.randint(1, 45)
        while val not in result: # 중복된 번호를 생성하지 않도록 합
            result.append(val)

        if len(result) == 6: break # result 리스트에 번호가 6개가 되면 종료. 한줄의 로또번호 생성
           
    result.sort() # 숫자를 정렬
    total.append(result) # result 리스트를 total리스트에 추가. 
                         #한줄의 로또 번호를 모두 생성한 후 해당 번호를 total리스트에 추가
    result = [] # result 리스트 초기화. 다음 로또번호를 생성 준비

print(total)

## 내부 라이브러리중 웹사이트 분석용
#import urllib
# 요청(request > 응답(response))
from urllib.request import Request, urlopen

req = Request('https://www.naver.com')
res = urlopen(req)

print(res.status) # 응답코드 200 : ok
print(res.read()) # 내용가져오기 : html 소스코드를 가져옴. 전부 가지고 오지는 못해서 잘림


