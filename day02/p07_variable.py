# file: p07_variable.py
# desc: 변수에 대하여
from copy import copy # 분리할때 사용하는 함수 copy

a = [1,2,3]
print(id(a))

b = a
print(id(b))

c=1
d=c
print(id(c))
print(id(d))

del b[2]
print(a)

d = copy(a)
print(id(d))
del d[2]
print(a)

