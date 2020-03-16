import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets,QtCore


class TestForm(QMainWindow): #PyQt5.QtWidgets에서 상속됨
    #생성자
    def __init__(self):
        super().__init__()#부모의 생성자
        self.setupUI()#함수 선언
    def setupUI(self):
        self.setWindowTitle("파이큐티 테스트")
        self.setGeometry(800,400,500,500) # 창크기  앞쪽 두개는 윈도우 위치  뒤쪽 두개는 윈도우창 크기

        label1=QLabel("입력 테스트",self)
        label1.move(20,20)

        label2=QLabel("출력 테스트",self)
        label2.move(20,60)

        self.lineEdit=QLineEdit("",self) #default값
        self.plainEdit=QtWidgets.QPlainTextEdit(self)
        self.plainEdit.setReadOnly(True) #쓰기방지

        self.lineEdit.move(100,20)
        self.plainEdit.setGeometry(QtCore.QRect(20,90,260,200))

        self.lineEdit.textChanged.connect(self.lineEditChanged)
        self.lineEdit.returnPressed.connect(self.lineEditEnter)

        #상태바
        self.statusBar=QStatusBar(self)
        self.setStatusBar(self.statusBar)

    def lineEditChanged(self):
        self.statusBar.showMessage(self.lineEdit.text())

    def lineEditEnter(self):
        self.plainEdit.appendPlainText(self.lineEdit.text())
        self.lineEdit.clear() # 메모리 해제


if __name__ == "__main__":
    app=QApplication(sys.argv)
    window=TestForm()
    window.show()
    app.exec_()
