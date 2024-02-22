# file: p08_review.py
# desc : review

# 2,3,5,6,10

#2
a = 13
print('a는', end='')
if a%2==0:
    print('짝수')
else:
    print('홀수')

#3
pin = "881120-1068234"
yyyymmdd = pin[:6]
num = pin[6:]
print(yyyymmdd)
print(num)

#5
a = "a:b:c:d"
b = a.replace(':','#')
print(b)

#6
a = [1, 3, 5, 4, 2]
a.sort()
a.sort(reverse=True)
print(a)

#10
a = {'A':90, 'B':80, 'C':70}
result = a.pop('B')
print(a)
print(result)
