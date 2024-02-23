# file : p22_carClass.py
# desc : 객체지향 클래스 학습

class Car:
    __carNum = '' # __변수를 지정하면 private, 그냥쓰면 public
    company = ''
    releaseYear = 1960     # 출시년도
    color = '흰색'
    carType = ''
    fuelType = '가솔린'
  
    ## __ 언더바 2개 = 매직메서드 : 여러가지 내장함수를 사용할 수 있게 만들어 놓은것
    def __init__(self) -> None: # 생성자 / None = 아무것도 리턴을 안한다. = void(java)
        print('Car 객체를 생성합니다.')

    def __str__(self) -> str: # 객체변수를 print() 할때 출력 커스터마이징 함수
        return f'내차는 {self.company}, {self.__carNum} 입니다!' # f뒤에 스페이스바 눌러서 띄우면 안된다!

    def getCarColor(self):
        print(f'{self.__carNum}은(는) {self.color}입니다.')

    def start(self):
        print(f'{self.__carNum}시동을 겁니다')

    def accel(self):
        print(f'{self.__carNum}은(는) 엑셀을 밟습니다.')

    def brake(self):
        print(f'{self.__carNum}은(는) 브레이크를 밟습니다.')

    def turnLeft(self):
        print(f'{self.__carNum}은(는) 좌회전입니다.')

    def turnRight(self):
        print(f'{self.__carNum}은(는) 우회전합니다.')#

    