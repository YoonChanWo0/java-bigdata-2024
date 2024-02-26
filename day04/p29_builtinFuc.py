# file: p29_builtinFuc.py
# desc: 내장함수

## abs(absoult) 절대값
print(abs(-5))

## all 현재 컬렉션 데이터의 조건, 값이 참인값만 있는지 확인
print(all([1,2,3,(4<2),5]))
# 결과값 : false

## chr() 아스키나 유니코드 값을 받아서 글자로 변경
print(chr(97)) # 결과값 :a
print(chr(44032)) # 결과값 : 가
## ascii() 영문자, 문자를 아스키 숫자와 유니코드 숫자로 변경
print(ascii('가')) # 결과값 : '\uac00'

## dir() 객체가 지닌 변수, 함수를 알려주는 함수
print(dir(list()))
print(dir(dict())) # 객체에 어떤 함수가 있는지 알려주는 함수

## divmod() 나누기의 몫, 나머지를 한번에 구해주는 함수
print(divmod(7,2)) # (3,1) 앞에값이 몫, 뒤의값이 나머지

## ★ enumerate() : 인덱스와 데이터로 나누어 열거한다라는 뜻, 데이터 포함 인덱스를 같이 생성해주는 역할
for i in ['Hello', 'World', 'Python']:
    print(i)
    
for i in enumerate['Hello', 'World', 'Python']:
    print(i)

for (i, data) in enumerate(['Hello', 'World', 'Python']): 
    print(f'{i}번쨰 값은 {data}입니다.')
    
## eval(uate) 실행함수, 문자열로 된 수식, 함수를 실행해주는 역할
print(eval('divmod(10,3)'))

## hex : 10진수를 16진수로
print(hex(255).upper()) # 출력값 0xff, .upper() : 대문자로 출력할떄 사용

## map : 여러값을 한꺼번에 같은 조건으로 변경할떄 사용
def ttime(x):
    return x*2

print(list(map(ttime, [1,3,5,7,9]))) # map을 써서 반복데이터를 ttime() 함수로 처리하라. 출력값 : [2, 6, 10, 14, 18]
print(list(map(int,[1.3,2.3,3.0,4.4]))) # map을 써서 반복데이터를 int로 바꾸어라. 출력값 : [1, 2, 3, 4]

## max()
print(max([3, 9, 99]))
print(min([3, 9, 99]))

## oct() 8진수
print(oct(34))

##ord() == ascii()
print(ord('A'))
print(ord('가'))

## round() 반올림(이상징후 4.5도 4로 나옴)
print(round(4.51)) # 4.5 != 5
print(round(4.45, 1))

## sum() 반복되는 컬렉션 자료
print(sum([1,2,3,4,5])) # 값  :15
print(sum(range(1,101))) # 값 : 5050

## tuple() 다른 컬렉션을 튜플자료형으로 변경
print(tuple([1,2,3,4,5])) # 값 : (1,2,3,4,5)

## type() 변수, 데이터의 타입 리턴
print(type('Hello')) # <class 'str'>
aa = [1,2,3,4] # 출력값 : <class 'str'>
print(type(aa)) # 출력값 : <class 'list'>

## zip() 동일한 개수로 데이터를 묶어서 리턴
## 둘의 갯수가 일치하지 않으면 일치하는 것까지만 묶어줌. 나머지는 버림
odd = [1,3,5,7,9]
even = [2,4,6,8,10]
norm = [1,2,3,4,5]

total = list(zip(odd, even, norm))
print(total) # 출력값 :[(1, 2, 1), (3, 4, 2), (5, 6, 3), (7, 8, 4), (9, 10, 5)]