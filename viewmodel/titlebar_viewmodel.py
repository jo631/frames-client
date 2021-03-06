from typing import Callable
from client.view.titlebar_view import TitleBarLayout
from PyQt5 import QtWidgets
from client.config.config import *

import time

class TitleBarViewModel:
    view : TitleBarLayout
    
    Btn_setting : QtWidgets.QPushButton
    Btn_exit : QtWidgets.QPushButton

    Btn_test : QtWidgets.QPushButton

    closeFunc : Callable

    def __init__(self, view : TitleBarLayout, settingFunc, closeFunc, config):
        self.view = view
        self.Btn_setting = view.getBtnSetting()
        self.Btn_exit = view.getBtnExit()
        self.closeFunc = closeFunc
        self.config : Config = config
        self.connectEvent(settingFunc)
        self.changeLabel()

    def connectEvent(self,settingFunc):
        self.Btn_exit.clicked.connect(lambda: self.event_BTN_exit())
        self.Btn_setting.clicked.connect(settingFunc)

    def event_BTN_exit(self):
        self.closeFunc()
        time.sleep(1)
        self.view.parent().parent().close()

    def changeLabel(self):
        self.view.LB_fNum.setText("건물 번호: " + str(self.config.getFacilityNum()))
        self.view.LB_fName.setText(self.config.getFacilityName())
        state = self.config.getState()
        text = "기기를 등록해주세요"
        if state==State.IN:
            text="입장"
        elif state==State.OUT:
            text="퇴장"

        self.view.LB_fState.setText(text)
            

    # def evnet_BTN_test(self):
    #     view = QRWindow()
    #     self.view.Btn_Test.clicked.connect(lambda: QRViewModel(view, "https://naver.com"))