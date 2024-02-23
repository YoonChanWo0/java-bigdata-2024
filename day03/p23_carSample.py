# file : p23_carSample.py
# desc : Car클래스 사용해보기

from p22_carClass import Car

myCar = Car() # 클래스를 사용, 객체를 하나 생성 = (= instance)
yourCar = Car()

# print(myCar)
# print(yourCar)
myCar.carNum = '123가 1234'
myCar.company = '현대차'
myCar.fuelType = '가솔린'
myCar.carType = '하이브리드'
myCar.color = '흰색'
myCar.releaseYear = 2018
yourCar.carNum = '87호 2459'
print(myCar)

myCar.start()
myCar.accel()
yourCar.start()
myCar.turnLeft()
myCar.turnRight()
myCar.brake()