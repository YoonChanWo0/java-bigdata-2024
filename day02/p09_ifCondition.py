# file: p09_ifCondition.py
# desc : if 제어문

money = 3000

if money >= 5000:
    # indentation(들여쓰기) tab == space + 4 
     print('택시타고 가')
     print('부럽네')
elif money < 500 and money >= 2500:
     print('기사님 홈플러스 앞까지만 가주세요')
     print('집까지 걸어감')

else:
     print('걸어가!')
     print('돈도 없는게...')
a,b,c,d  = 10, 5, 7, 9

print(a>=b) # True
print(c>d)# False

print(a>=b and c> d)#False
print(a >=b or c>d)#True 1 or 1 == 1 / 1 or 0 ==1
## and 80% / or 20%

print(not(a>=b)) #False

print(1 in [1,3,5,7,9])
print(6 in [1,3,5,7,9])

score = 60
# 파이썬에선 조건 연산자를 잘 안씀
# (score >= 60)? "success":"failure"
print('success' if score >= 60 else 'falure')
