#file: p06_bool.py
# desc: 불타입 학습

# 참/거짓

a = True # 자바에서는 true 소문자 사용, 파이썬은 앞들자 대문자.
b = False

print(a)
print(type(a)) # <class 'bool'>
print(type(1)) # <class 'int'>
print(type(3.14)) # <class 'float'>
print(type('Hi')) # <class 'str'>
print(type([1,2,3])) # <class 'list'>
print(type((1,2,3))) # <class 'tuple'>

print(a==b)
print(a == (not b)) 

print(bool('H')) # 0이외의 값은 true, 빈값은 false
# 참/거짓 구분 빈값, 0, None False 그외 True

# None 타입 / java로 생각하면 NULL
None 

c = None # none는 값을 더할 수 없다.
a = 1
b = 0
print(c)
print(a+b) # a True(1) False(0)

c = 3
print(c+a)