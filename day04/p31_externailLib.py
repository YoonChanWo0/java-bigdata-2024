# file: p31_externailLib.py
# desc: 외부 라이브러리 사용법

# > pip install LibName
# Successfully installed / Requirement satisfied가 나와야 함
# > pip uninstall LibName
# Successfully uninstalled 나와야 함

from faker import Faker

fake = dummy = Faker('ko-KR') # 한국어 설정
print(fake.name()) # 가짜데이터를 만들어줌
print(fake.address()) # 가짜데이터를 만들어줌
# print(fake.profile()) # 가짜데이터를 만들어줌

dummyData = [(fake.profile())for _ in range(10)]
print(dummyData)

## urllib3 외부 웹페이지 분석 모듈
import requests # pip install requests 로 다운받기
from bs4 import BeautifulSoup # pip install beautifulsoup4로 다운받기

# res = requests.get('https://www.naver.com')
# print(res.status_code)
# print(res.content)# 내용가져오기 / 이거 말고 print(res.text) 이걸로 내용 가져오기 content는 안됨

res = requests.get('https://www.naver.com')

if res.status_code == 200:
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)