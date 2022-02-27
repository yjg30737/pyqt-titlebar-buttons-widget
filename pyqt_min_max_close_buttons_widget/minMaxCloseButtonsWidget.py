from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton


class MinMaxCloseButtonsWidget(QWidget):
    def __init__(self, hint=Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint):
        super().__init__()
        self.__initVal()
        self.__initUi(hint)

    def __initVal(self):
        self._closeBtn = QPushButton()
        self._minimizeBtn = QPushButton()
        self._maximizeBtn = QPushButton()

    def __initUi(self, hint):
        lay = QHBoxLayout()
        lay.setContentsMargins(0, 0, 0, 0)

        if hint == Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint:
            lay.addWidget(self._minimizeBtn)
            lay.addWidget(self._maximizeBtn)
            lay.addWidget(self._closeBtn)
        elif hint == Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint:
            lay.addWidget(self._minimizeBtn)
            lay.addWidget(self._closeBtn)
        elif hint == Qt.WindowCloseButtonHint:
            lay.addWidget(self._closeBtn)
        else:
            # todo for another type of flags
            pass

        self.setLayout(lay)
        # raise - helps the button widget not to be blocked by something else
        self.raise_()

    def getMinimizedBtn(self):
        return self._minimizeBtn

    def getMaximizedBtn(self):
        return self._maximizeBtn

    def getCloseBtn(self):
        return self._closeBtn