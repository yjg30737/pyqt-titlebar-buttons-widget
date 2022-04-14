from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton
from pyqt_svg_icon_pushbutton import SvgIconPushButton


class MinMaxCloseButtonsWidget(QWidget):
    def __init__(self, hint: list = ['min', 'max', 'close']):
        super().__init__()
        self.__initVal()
        self.__initUi(hint)

    def __initVal(self):
        self._closeBtn = QPushButton()
        self._minimizeBtn = QPushButton()
        self._maximizeBtn = QPushButton()

        self._fullScreenBtn = SvgIconPushButton()
        self._fullScreenBtn.setIcon('ico/full_screen.svg')

        self._helpBtn = SvgIconPushButton()
        self._helpBtn.setIcon('ico/help.svg')

        self._foldBtn = SvgIconPushButton()
        self._foldBtn.setIcon('ico/fold.svg')

        self._fixBtn = SvgIconPushButton()
        self._fixBtn.setIcon('ico/tack.svg')

    def __initUi(self, hint: list):
        lay = QHBoxLayout()
        lay.setContentsMargins(0, 0, 0, 0)

        if 'full_screen' in hint:
            lay.addWidget(self._fullScreenBtn)
        if 'help' in hint:
            lay.addWidget(self._helpBtn)
        if 'fold' in hint:
            lay.addWidget(self._foldBtn)
        if 'fix' in hint:
            lay.addWidget(self._fixBtn)
        if 'min' in hint:
            lay.addWidget(self._minimizeBtn)
        if 'max' in hint:
            lay.addWidget(self._maximizeBtn)
        if 'close' in hint:
            lay.addWidget(self._closeBtn)

        self.setLayout(lay)
        # raise - helps the button widget not to be blocked by something else
        self.raise_()

    def getMinimizedBtn(self):
        return self._minimizeBtn

    def getMaximizedBtn(self):
        return self._maximizeBtn

    def getCloseBtn(self):
        return self._closeBtn