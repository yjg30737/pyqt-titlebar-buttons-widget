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

        self._btn_dict = {'min': [self._minimizeBtn], 'max': [self._maximizeBtn], 'close': [self._closeBtn],
                          'full_screen': [self._fullScreenBtn], 'help': [self._helpBtn], 'fold': [self._foldBtn],
                          'fix': [self._fixBtn]}

    def __initUi(self, hint: list):
        lay = QHBoxLayout()
        lay.setContentsMargins(0, 0, 0, 0)

        for k in hint:
            lay.addWidget(self._btn_dict[k])

        self.setLayout(lay)
        # raise - helps the button widget not to be blocked by something else
        self.raise_()

    def setMinimizedBtn(self, btn):
        self._minimizeBtn = btn

    def setMaximizedBtn(self, btn):
        self._maximizeBtn = btn

    def setCloseBtn(self, btn):
        self._closeBtn = btn

    def setFullScreenBtn(self,  btn):
        self._fullScreenBtn = btn

    def setFixBtn(self, btn):
        self._fixBtn = btn

    def setFoldBtn(self, btn):
        self._foldBtn = btn

    def setHelpBtn(self, btn):
        self._helpBtn = btn

    def getMinimizedBtn(self):
        return self._minimizeBtn

    def getMaximizedBtn(self):
        return self._maximizeBtn

    def getCloseBtn(self):
        return self._closeBtn

    def getFullScreenBtn(self):
        return self._fullScreenBtn

    def getFixBtn(self):
        return self._fixBtn

    def getFoldBtn(self):
        return self._foldBtn

    def getHelpBtn(self):
        return self._helpBtn