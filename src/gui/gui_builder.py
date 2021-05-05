from PyQt5 import QtCore, QtWidgets, QtGui

class GuiBuilder:
    def __init__(self):
        pass

    @staticmethod
    def makeBoxLayoutIn(parent, isVertical : bool):
        box : QtWidgets.QBoxLayout = None
        
        if isinstance(parent, QtWidgets.QLayout):
            if isVertical:
                box = QtWidgets.QVBoxLayout()
            else:
                box = QtWidgets.QHBoxLayout()

            parent.addLayout(box)

        elif isinstance(parent, QtWidgets.QWidget):
            if isVertical:
                box = QtWidgets.QVBoxLayout(parent)
            else:
                box = QtWidgets.QHBoxLayout(parent)

        if box is None:
            return 
        
        box.setSpacing(5)
        box.setContentsMargins(5,5,5,5)
        return box

    @staticmethod
    def makeLabelIn(parent : QtWidgets.QLayout , text , alignFlag : QtCore.Qt.AlignmentFlag):
        label = QtWidgets.QLabel(text)
        label.setAlignment(alignFlag)
        parent.addWidget(label)

        return label

    @staticmethod
    def makePushButtonIn(parent, stretch, imagePath, text):
        btn = QtWidgets.QPushButton(QtGui.QIcon(imagePath), text)
        btn.setSizePolicy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding)
        parent.addWidget(btn, stretch = stretch)

        return btn

    @staticmethod
    def makeLineEditIn(parent, stretch, text):
        lineEdit = QtWidgets.QLineEdit(text)
        parent.addWidget(lineEdit, stretch = stretch)
        return lineEdit

    @staticmethod
    def makeRadioButton(parent, text):
        btn = QtWidgets.QRadioButton(f"{text} ")
        btn.setStyleSheet('''
        QRadioButton { font: 15pt;} 
        QRadioButton::indicator { width: 0px; height: 0px; }
        QRadioButton::checked{
            background-color: gray; 
            border : 2px solid black; 
        }
        QRadioButton::unchecked{ 
            background-color: light gray; 
            border : 2px solid black; }
        ''')

        parent.addWidget(btn)
        return btn

    @staticmethod
    def makeGroupBoxIn(parent):
        gb = QtWidgets.QGroupBox()
        parent.addWidget(gb)

        return gb