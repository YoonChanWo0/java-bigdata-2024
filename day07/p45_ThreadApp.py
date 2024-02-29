# file: p45_ThreadApp.py
# desc: PyQt5, QtDesinger를 같이 사용

import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class BackgroundWorker(QThread): # PyQt용 스레드
    initUiSignal = pyqtSignal(int) # 스레드 진행시 UI에서 초기화부분 시그널 전달 
    setPgbSignal = pyqtSignal(int) # 스레드 진행시 변경되는 숫자를 UI로 전달
    setTxbSignal = pyqtSignal(str) # 스레드 진행시 화면에 출력될 문자열 UI쪽으로 전달


    def __init__(self, parent) -> None: # 부모는 atApp 클래스
        super().__init__(parent)
        self.parent = parent #

    def run(self) -> None:
        maxVal = 1_000_000
        self.initUiSignal.emit(maxVal) # 나는 값을 보내니 UI쪽(qtApp)에서 받아서 처리해줘

        for i in range(maxVal):
            print(f'쓰레드 진행 >> {i}')
            self.setPgbSignal.emit(i)
            self.setTxbSignal.emit(f'쓰레드 진행>>{i}' )
            # self.pgbTask.setValue(i) # UI 스레드의 권한을 백그라운드스레드에 주지 않는다
            # self.txbLog.append(f'쓰레드 진행 >>{i}')
 
class qtApp(QWidget): #Qwidget이 가지고 있는 속성, 변수 함수를 다 사용가능. (클래스를 상속)
    def __init__(self) -> None: 
        super().__init__() # 생성자, 부모클래스의 생성자 함수도 실행되어야 한다. 반드시 필요!
        self.initUi()

    def initUi(self):
        uic.loadUi('./day07/testThread.ui', self)
        self.setWindowTitle('쓰레드앱')
        self.setWindowIcon(QIcon('./images/windows.png'))
        # 버튼 시그널처리
        self.btnStart.clicked.connect(self.btnStartClicked) # ui 파일내 위잿은 자동완성x

        self.show() # 윈도우창 그려!

    def btnStartClicked(self):
        self.btnStart.setDisabled(True)
        th = BackgroundWorker(self) #atApp이 부모클래스라고 선언
        th.start() # 스레드 내 run() 함수 실행
        th.initUiSignal.connect(self.initPgbTask)
        th.setPgbSignal.connect(self.setPgbTask)
        th.setTxbSignal.connect(self.setTxbLog)

        self.btnStart.setEnabled(True)

    @pyqtSlot(str)
    def setTxbLog(self, msg):
        self.txbLog.append(msg)    

    @pyqtSlot(int)
    def setPgbTask(self, val):
        self.pgbTask.setValue(val)    

    @pyqtSlot(int) # pyqtSignal에서 넘어온 값을 처리해주는
    def initPgbTask(self, maxVal):
        self.pgbTask.setValue(0)
        self.pgbTask.setRange(0, maxVal-1)

    def closeEvent(self, QcloseEvent) -> None: # 우리식으로 내용을 오버라이드(재정의)
        re = QMessageBox.question(self, '종료확인', '종료할래?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes: # 진짜 닫음
            QcloseEvent.accept()
        else:
            QcloseEvent.ignore() # 무시
        

app = QApplication(sys.argv) #
inst = qtApp() # 객체생성
app.exec_() # 실행
