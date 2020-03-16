import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class TestForm(QMainWindow): #PyQt5.QtWidgets에서 상속됨
    #생성자
    def __init__(self):
        super().__init__()#부모의 생성자
        self.setupUI()#함수 선언
    def setupUI(self):
        self.setWindowTitle("파이큐티 테스트")
        self.setGeometry(800,400,500,300) # 창크기  앞쪽 두개는 윈도우 위치  뒤쪽 두개는 윈도우창 크기

        btn_1=QPushButton("클릭1",self)
        btn_2=QPushButton("클릭2",self)
        btn_3=QPushButton("클릭3",self)

        btn_1.move(20,30)
        btn_2.move(120,30)
        btn_3.move(220,30)

        btn_1.clicked.connect(self.btn_1_clicked) # signal
        btn_2.clicked.connect(self.btn_2_clicked)
        btn_3.clicked.connect(QCoreApplication.instance().quit) # 시그널 & 슬롯

    def btn_1_clicked(self):
        QMessageBox.about(self,"메세지","클릭함1 ")# sloat ?  슬롯
    def btn_2_clicked(self):
        print("button2 clicked")


if __name__ == "__main__":
    app=QApplication(sys.argv)
    window=TestForm()
    window.show()
    app.exec_()
