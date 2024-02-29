# file: p36_qtApp.py(계속)
# desc: PyQt5 앱 만들기
'''
pyQt -> Qt를 파이썬에서 쓸수 있도록 만든 라이브러리
Qt -> C,  C++ 에서 사용할 GUI(WindowApp) 프레임워크(멀티플랫폼)

설치 > pip install PyQt5
'''
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
# QApplication : 만들앱의 전체를 관리하는 클래스, Qwidget 메뉴가 없는 윈도우앱,  QMainWindow 메뉴가 있는 윈도우 앱 
# from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow #QtWidgets #QLabel 안에 있는것을 가지고 온다 
from PyQt5.QtWidgets import *
# QMainWindow, QLabel, QPushButton 등은 QWidget을 상속한 자식 클래스(부모 클래스의 능렧들을 다 사용할 수 있음)


class qtApp(QWidget): #Qwidget이 가지고 있는 속성, 변수 함수를 다 사용가능. (클래스를 상속)
    def __init__(self) -> None: 
        super().__init__() # 생성자, 부모클래스의 생성자 함수도 실행되어야 한다. 반드시 필요!
        self.initUi()

    def initUi(self):
        label = QLabel() # 라벨위젯.라벨컨트롤(NFC, C#, Java Fx, Android) / <-(2개 같은말) 
        

        self.setGeometry(300, 300, 800, 400) # 바탕화면 정해진 위체에 넓이와 높이로 그림 설정. 반드시 필요! (오른쪽으로 이동(중앙으로 옮김), 오른쪽 하단으로 이동, 가로로 넓게 설정,  세로로 넓게 설정)
        self.setWindowTitle('두번째 qt앱')
        self.setWindowIcon(QIcon('./images/windows.png'))
        self.text='What a wonderful day...'
        label.setText(self.text)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet(('color: red;'
                             'background-color: black;')) # 라벨의 색상스타일 설정 html css와 완전 동일

        font = label.font()
        font.setFamily('Bauhaus 93')
        font.setPointSize(40)
        

        label.setFont(font)

        layout = QVBoxLayout()
        layout.addWidget(label)

        self.setLayout(layout)
        self.show() # 윈도우창 그려!

    def paintEvent(self, event) -> None: # 라벨 만드는 첫번쨰 방법
        paint = QPainter() # 윈도우 창 위에 그림을 그리는 객체 = self에다가 그림 그리는것을 시작하겠다. 라는 의미
        paint.begin(self) # 그림을 그리기 시작하면
        paint.setPen(QColor(200, 0, 0)) #rgb로 나타낸다. red, green, blue 순서대로 작성. 포토샵 생각하기!
        paint.setFont(QFont('Bauhaus 93',40)) #Bauhaus = 글자체 
        paint.drawText(250, 400//2, 'Hello PyQt!')
        paint.end() # 반드시 마지막에 닫아줘야한다.



app = QApplication(sys.argv) #
inst = qtApp() # 객체생성
app.exec_() # 실행
