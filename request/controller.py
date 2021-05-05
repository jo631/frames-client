from PyQt5 import QtWidgets

from client.request.view import RequestLayout

from client.request.requests import Request
from client.request.resultQueue import ResultQueue

from client.request.state_stylesheet import StateStyleSheet

import threading

class RequestController:
    resultQueue = ResultQueue()

    LB_title : QtWidgets.QLabel
    LB_subtitle : QtWidgets.QLabel
    GB_labelBox : QtWidgets.QGroupBox

    cssDict : dict

    def __init__(self,view: RequestLayout, vd, tp, config):
        self.cssDict = StateStyleSheet()
        self.LB_title = view.getLB_title()
        self.LB_subtitle = view.getLB_subtitle()
        self.GB_labelBox = view.getGB_labelBox()
        self._initRequestModule(vd,tp, config)


    def _initRequestModule(self, vd, tp,config ):       
        request = Request(vd,tp, self.resultQueue, config)
        request.reqSendFrame(sendCycle=1,timeout=3)
        self._checkQueue()

    def _checkQueue(self):
        th = threading.Thread(target=self.__checkQueue)
        th.start()
    
    def __checkQueue(self):
        while True:
            if self.resultQueue.isExistData():
                self._updateView(self.resultQueue.getData())


    def _updateView(self, data):
        state, title, subtitle = data
        #위는 32 아래는 28
        self.__changeStyleSheet(state)

        self.LB_title.setText(title)
        self.LB_subtitle.setText(subtitle)
    
    def __changeStyleSheet(self, state):
        self.GB_labelBox.setStyleSheet(self.cssDict[state])
        self.LB_subtitle.setStyleSheet("font-size: 28px;")