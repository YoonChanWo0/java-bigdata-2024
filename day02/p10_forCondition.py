# file: p10_forCondition.py
# desc: for 반복문

#for item in 반복할객체 :
# ...

a= [1,3,5,7,9]
print(type(a)) #<class 'list'>


for i in ['one','two','three']:
    print(type(i))

b = [(1,2), (3,4), (5,6)]

for i in b:
    print(i)

for(first, second) in b:
    print(first, second)

# 평균 내기
    grade = [90, 80 ,70 ,50 ,10]
    sum =0
    for i in grade:
        sum += i
        print(sum)
        print(sum/len(grade))

# range()
print(range(10))
print(range(0, 10))

for i in range(0, 10): # 9+1
    print(i, end=',')
print()

print(list(range(0, 10)))

print(list(range(0, 10+1, 2))) # 0부터 짝수로 
print(list(range(1, 10, 2))) # 1부터 홀수로 

print(list(range(10, 0, -2)))

res = 0
for i in range(1, 101):
    res += i

print(res)

## list comprehension 리스트 내포
# list(range()) 만으로도 리스트를 생성할 수 있지만, 여러조건으로 리스트 생성할 떄는 print([num * 3 for num in range(1, 1001) if num % 3 == 0]) 와 같이 사용하는것이 좋다.
print([i for i in range(1, 101)])
print(list(range(1, 101)))

print([num * 3 for num in range(1, 1001) if num % 3 == 0])