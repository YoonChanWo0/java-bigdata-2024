# file : P24_ionic.py
# desc : 클래스 상속

from p22_carClass import Car

class ionic(Car): # 상속. Car클래스를 상속받아서 ionic
    __fuelRate = 0.0 # 연비

    def setFuelRate(rate):
        self.__FuelRate = rate

        def getFulRate(self) -> float:
            return self.__fuelRate
        
        def getCarNum(self) -> str: # g함수 오버라이딩(재정의)
            return f'소중한 제차는 {self.__carNum}에요~!!'

myCar = ionic('54라 9337')
myCar.company = '기아자동차'
myCar.setFuelRate(23.5)
print(myCar)
print(f'내차의 연비는 {myCar.getFuelRate()} km/1 입니다.')
print(myCar.getCarNum())