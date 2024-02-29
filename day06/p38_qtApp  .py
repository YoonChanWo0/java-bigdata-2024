# file: p38_qtApp.py(계속)
# desc: PyQt5, QtDesinger를 같이 사용

'''
설치 > pip install PyQt5
설치 > pip install PyQt5Designer
'''
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class qtApp(QWidget): #Qwidget이 가지고 있는 속성, 변수 함수를 다 사용가능. (클래스를 상속)
    def __init__(self) -> None: 
        super().__init__() # 생성자, 부모클래스의 생성자 함수도 실행되어야 한다. 반드시 필요!
        self.initUi()

    def initUi(self):

        self.setGeometry((1920-300)//2, (1000-300)//2, 320, 230) # 해상도 1920x1080에서 정중앙에 위치
        self.setWindowTitle('네번째 qt앱')
        uic.loadUi('./day06/firstApp.ui', self)
        self.setWindowIcon(QIcon('./images/windows.png'))
        # 버튼 시그널처리
        self.btnMsg.clicked.connect(self.btnMsgClicked) # ui 파일내 위잿은 자동완성x
        self.show() # 윈도우창 그려!

    def btnMsgClicked(self):
        QMessageBox.about(self, 'Qt디자이너', '클릭하였습니다!')
        self.label.setText('What the F*')

    def btn1Clicked(self):
        QMessageBox.about(self, '버튼클릭',' 버튼을 눌렀습니다!!')   

    def closeEvent(self, QcloseEvent) -> None: # 우리식으로 내용을 오버라이드(재정의)
        re = QMessageBox.question(self, '종료확인', '종료할래?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes: # 진짜 닫음
            QcloseEvent.accept()
        else:
            QcloseEvent.ignore() # 무시
        

app = QApplication(sys.argv) #
inst = qtApp() # 객체생성
app.exec_() # 실행
