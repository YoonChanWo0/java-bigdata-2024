#file: p17_fileIo.py
#desc : 파일 입출력 학습

# 컴퓨터에서 열면 무조건 닫아야 하는 것
# 1. 파일 open(), close() 파이썬에서만 안닫아도 크게 지장 x
# 2. 통신 open(), close() 
# 3. DB open(or connect), close()

# 언어체계 추가 ASCII(한글 cp949), 유니코드(UTF-8)
# 상대경로, 절대경로
f = open('./sample.txt',mode='w', encoding='utf-8')
# 파일쓰기 진행
f.write('안녕하세요. 파이썬.')
f.write('모두 화이팅!!.')

f.close() # 파이썬에서만 옵션. 다른언어에선 무조건 close()