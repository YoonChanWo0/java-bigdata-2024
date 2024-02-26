# file: p25_usingModule.py
# desc: 모듈 사용

# 모듈은 중괄호로 표시한다!
# import calc as c# 나는 clac.py를 사용할래 c 로 이름을 바꿔서
# result = c.mul(10,7)
# print(result)

from calc import mul as mult# mul() 함수명만 쓰면 됨 / 단 여러개의 모듈을 사용할 떄는 충돌이나서 사용하지 못한다(ex. 같은 이름의 mul()이 있을경우 충돌 방생!!).

# import Math
from Math import Math # from Math는 모듈(파일이름) import Math는 클래스 이름

from day03.p22_carClass import Car # 디렉토리(모듈묶음:패키지).모듈명

if __name__ ==  '__main__': # 안에 들어가는 코드들이 tab안에 들어감 / java void main()과 동일함

    result = mult(10,7)
    print(result)

    print(__name__) # __main__ = 나는 메인 엔트리야

    # myMath = Math.Math() # Math라는 모듈, 클래스 이름을 두개 다 써줘야 된다.(import 안할경우)
    myMath = Math()
    print(myMath.solv(10))