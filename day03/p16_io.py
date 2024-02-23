# file: p16_io.py
# desc: 입출력 학습

#input() 함수 기본
# res = input('인사말을 적으세요 > ')
# print(res)

# num = input('곱할 수를 적으세요 >')
# print(type(num))
# input()으로 받는 값은 모두 문자열
# num = int(num)
# print(num*2)
# 숫자를 입력받아서 계산을 할떄는 형변환이 필요

#print(num)
#num -= 10 # 문자열 연산은 +,* 2가지 밖에 안되서 오류 발생

# num = int(input('2로 곱하 숫자 입력'))
# print(num*2)

## 여러값 입력
# int(40.2) # 40
# int('50') # 50
# int('40.2') # x
# int(('40.2')) # x 튜플 바로 int로 변경할 수 있는 방법이 x


# 튜플의 괄호중 할당을 받는 쪽의 괄호()는 생략 가능
# (a1, a2, a3) = input('합산할 3개 값을 입력(구분자 space) >').split('')
(a1, a2, a3) = map(int, input('합산할 3개 값을 입력(구분자 space) >').split(' '))
print(a1, a2, a3)
a1 = int(a1)
a2 = int(a2)
a3 = int(a3)
sum = a1+a2+a3
print(f'합계는{sum}')