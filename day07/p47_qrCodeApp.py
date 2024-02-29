# file: p47_qrCodeApp.py
# desc: PyQt QR코드앱

'''
설치 > pip install qrcode
'''
import qrcode
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
        uic.loadUi('./day07/qrApp.ui', self)
        self.setWindowTitle('QR코드 생성기')
        self.setWindowIcon(QIcon('./images/windows.png'))
        # 버튼 시그널처리
        self.btnGenerate.clicked.connect(self.btnGenerateClicked) # ui 파일내 위잿은 자동완성x

        self.show() # 윈도우창 그려!

    def btnGenerateClicked(self):
        data = self.txtQrData.text()

        if len(data.strip()) == 0:
            QMessageBox.about(self, '경고', '데이터 좀 입력해라')
            return
        else:
            imgPath = './day07/qr.png'
            qrImage = qrcode.make(data)
            qrImage.save(imgPath)
            self.lblQrCode.setPixmap(QPixmap(imgPath).scaledToWidth(300))
            

    def closeEvent(self, QcloseEvent) -> None: # 우리식으로 내용을 오버라이드(재정의)
        re = QMessageBox.question(self, '종료확인', '종료할래?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes: # 진짜 닫음
            QcloseEvent.accept()
        else:
            QcloseEvent.ignore() # 무시
        

app = QApplication(sys.argv) #
inst = qtApp() # 객체생성
app.exec_() # 실행
