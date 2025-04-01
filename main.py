import sys # 시스템 관련 기능을 사용하기 위한 모듈
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, 
							 QMessageBox, QPlainTextEdit, QHBoxLayout) # 필요한 위젯을 임포트

from PyQt5.QtGui import QIcon # 아이콘 관련 클래스를 임포트

class Calculator(QWidget): # Caculator 클래스를 QWidget을 상속받아서 클래스를 정의
	
	def __init__(self): # 생성자 (객체 초기화)
		super().__init__() # 부모 클래스(QWidget)의 생성자를 호출하여 초기화
		self.initUI() # UI 초기화 함수 호출

	def initUI(self): # UI를 초기화하는 함수
		self.te1 = QPlainTextEdit() # 읽기 전용 텍스트 입력 창 생성
		self.te1.setReadOnly(True) # 텍스트 입력 창을 읽기 전용으로 설정

		# "Message" 버튼 생성, 버튼 클릭 시 activateMessage 함수가 실행되도록 연결
		self.btn1 = QPushButton("Message", self)
		self.btn1.clicked.connect(self.activateMessage)

		# "Clear" 버튼 생성, 버튼 클릭 시 clearMessage 함수가 실행되도록 연결
		self.btn2 = QPushButton("Clear", self)
		self.btn2.clicked.connect(self.clearMessage)

		# 버튼등을 수평으로 배치할 수 있는 레이아웃 생성
		hbox = QHBoxLayout()
		hbox.addStretch(1) # 레이아웃에 여백 추가
		hbox.addWidget(self.btn1) # "Message" 버튼을 수평 레이아웃에 추가
		hbox.addWidget(self.btn2) # "Clear" 버튼을 수평 레이아웃에 추가

		# 수직 레이아웃을 생성하고, 텍스트 입력 창과 버튼 레이아웃을 추가
		vbox = QVBoxLayout()
		vbox.addWidget(self.te1)
		vbox.addLayout(hbox)
		vbox.addStretch(1)

		self.setLayout(vbox)

		self.setWindowTitle('Calculator')
		self.setWindowIcon(QIcon("icon.png"))
		self.resize(256, 256)
		self.show()

	def activateMessage(self):
		self.te1.appendPlainText("Button clicked!")
	
	def clearMessage(self):
		self.te1.clear()

if __name__ == '__main__':
	# pyqt는 애플리케이션 당 1개의 QApplication이 필요함
	app = QApplication(sys.argv)
	# QApplication 인스턴스 생성
	view = Calculator()
	# Calculator windows 인스턴스 생성
	sys.exit(app.exec_())
	# Application이 event 처리를 하도록 루프 생성
