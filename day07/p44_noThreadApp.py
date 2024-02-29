# file: p44_noThreadApp.py
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
        uic.loadUi('./day07/testThread.ui', self)
        self.setWindowTitle('노쓰레드앱')
        self.setWindowIcon(QIcon('./images/windows.png'))
        # 버튼 시그널처리
        self.btnStart.clicked.connect(self.btnStartClicked) # ui 파일내 위잿은 자동완성x

        self.show() # 윈도우창 그려!

    def btnStartClicked(self):
        self.pgbTask.setValue(0) # 재설정
        self.pgbTask.setRange(0, 999_999) # 프로그레스바 범위설정
        self.btnStart.setDisabled(True)
        # UI(메인)스레드가 화면을 그릴 수 있는 여유가 없음(응답없음 발생)
        for i in range(0, 1_000_000): # 0~999,999
            print(f'노쓰레드 진행 >> {i}')
            self.pgbTask.setValue(i)
            self.txbLog.append(f'노쓰레드 진행 >> {i}')

        self.btnStart.setEnabled(True)

    def closeEvent(self, QcloseEvent) -> None: # 우리식으로 내용을 오버라이드(재정의)
        re = QMessageBox.question(self, '종료확인', '종료할래?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes: # 진짜 닫음
            QcloseEvent.accept()
        else:
            QcloseEvent.ignore() # 무시
        

app = QApplication(sys.argv) #
inst = qtApp() # 객체생성
app.exec_() # 실행
