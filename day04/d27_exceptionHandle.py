# file: d27_exceptionHandle.py
# desc: 예외처리2
# 비정상적인 종료를 막기 위한것

# while True:
#     try:
#         select = input('메뉴입력 1.저장, 2.검색, 3.종료 >')
#     except:
#         print('예외발생 입력을 정확히 하세요.')
#         continue

#     if select == '1':
#         print('입력')
#     elif select == '2':
#         print('검색')
#     elif select == '3':
#         break
#     else:
#         continue

class Chicken:
    def fly(self):
        raise NotImplementedError # 구현이 안되어 있기 떄문에 개발자에게 처리하라고 이야기하는 문구
    
koko = Chicken()
try:
    koko.fly()
except Exception as e:
    print('닭은 못날아요!', e.args) # NotImplementedError는 추가 예외메시지가 없음
