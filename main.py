import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
import re
import datetime
from lib.test1_layout import Ui_MainWindow
from PyQt5 import QtWebEngineWidgets
from lib.AuthDialog import AuthDialog
from PyQt5.QtCore import pyqtSlot
# form_class=uic.loadUiType('D:/section5/ui/test1.ui')[0]
#
# class TestForm(QMainWindow, form_class):
# #생성자
#     def __init__(self):
#         super().__init__()#부모의 생성자 함수 호출
#         self.setupUi(self)#함수 선언

class TestForm(QMainWindow, Ui_MainWindow):
#생성자
    def __init__(self):
        super().__init__()#부모의 생성자 함수 호출
        #초기화
        self.setupUi(self)#함수 선언
        #인증버튼 이벤트 전
        self.initAuthLock()
        #setupUI 로그인창 ? 인증창 ?



        #인증버튼 이벤트 후
        self.initAuthActive()
        #시그널 초기화
        self.initSignal()

        #로그인 관련 변수 선언
        self.user_id=None
        self.user_pw=None


    #기본 UI 비활성화
    def initAuthLock(self):
        self.previewButton.setEnabled(False)
        self.fileNavButton.setEnabled(False)
        self.streamComboBox.setEnabled(False)
        self.startButton.setEnabled(False)
        self.urlTextEdit.setEnabled(False)
        self.calendarWidget.setEnabled(False)
        self.pathTextEdit.setEnabled(False)
        self.showStatusMsg("인증안됨")

    def initAuthActive(self):
        self.previewButton.setEnabled(True)
        self.fileNavButton.setEnabled(True)
        self.streamComboBox.setEnabled(True)
        self.startButton.setEnabled(True)
        self.urlTextEdit.setEnabled(True)
        self.calendarWidget.setEnabled(True)
        self.pathTextEdit.setEnabled(True)
        self.showStatusMsg("인증완료")



    def showStatusMsg(self,msg):
        self.statusbar.showMessage(msg)
    #시그널 초기화
    def initSignal(self):
        self.loginButton.clicked.connect(self.authCheck)


    @pyqtSlot() #명시적 표현 (책갈피)
    def authCheck(self):
        pass

if __name__ == "__main__":
    app=QApplication(sys.argv)
    window=TestForm()
    window.show()
    app.exec_()
