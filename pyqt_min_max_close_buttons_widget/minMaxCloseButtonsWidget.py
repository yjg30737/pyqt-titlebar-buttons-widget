from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton


class MinMaxCloseButtonsWidget(QWidget):
    def __init__(self, hint: list = ['min', 'max', 'close']):
        super().__init__()
        self.__initVal()
        self.__initUi(hint)

    def __initVal(self):
        self._closeBtn = QPushButton()
        self._minimizeBtn = QPushButton()
        self._maximizeBtn = QPushButton()
        self._fullScreenBtn = QPushButton()
        self._helpBtn = QPushButton()
        self._foldBtn = QPushButton()
        self._fixBtn = QPushButton()

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