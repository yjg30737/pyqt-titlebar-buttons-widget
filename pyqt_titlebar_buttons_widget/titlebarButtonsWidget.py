from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QWidget, QHBoxLayout
from pyqt_svg_button import SvgButton


class TitlebarButtonsWidget(QWidget):
    def __init__(self, base_widget=None, hint: list = ['min', 'max', 'close']):
        super().__init__()
        self.__initVal(base_widget, hint)
        self.__initUi()

    def __initVal(self, base_widget, hint):
        self._closeBtn = SvgButton(base_widget)
        self._minimizeBtn = SvgButton(base_widget)
        self._maximizeBtn = SvgButton(base_widget)

        self._fullScreenBtn = SvgButton(base_widget)
        self._fullScreenBtn.setIcon('ico/full_screen.svg')

        self._helpBtn = SvgButton(base_widget)
        self._helpBtn.setIcon('ico/help.svg')

        self._foldBtn = SvgButton(base_widget)
        self._foldBtn.setIcon('ico/fold.svg')

        self._fixBtn = SvgButton(base_widget)
        self._fixBtn.setIcon('ico/tack.svg')

        self._btn_dict = {'min': self._minimizeBtn, 'max': self._maximizeBtn, 'close': self._closeBtn,
                          'full_screen': self._fullScreenBtn, 'help': self._helpBtn, 'fold': self._foldBtn,
                          'fix': self._fixBtn}

        self._base_widget = base_widget
        self.__window = self._base_widget.window()
        self.__window.installEventFilter(self)
        self._hint = hint

    def __initUi(self):
        lay = QHBoxLayout()
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(0)

        for k in self._hint:
            # hint str
            if k in self._btn_dict:
                lay.addWidget(self._btn_dict[k])
            # widget
            else:
                lay.addWidget(k)

        self.setLayout(lay)

        self._styleInit()

        # raise - helps the button widget not to be blocked by something else
        self.raise_()

    def _styleInit(self):
        # fill the button's background with color
        background_color = self._base_widget.palette().color(QPalette.Base).name()
        for btn in self._btn_dict.values():
            btn.setBackground(background_color)

    def event(self, e):
        if e.type() == 100:
            self._styleInit()
        return super().event(e)

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

    def setButtonIcon(self, hint: str, icon_filename: str):
        self._btn_dict[hint].setIcon(icon_filename)

    def setButtonSize(self, w, h):
        for k, v in self._btn_dict.items():
            if v.text():
                f = v.font()
                f.setPointSize(w // 1.75)
                v.setFont(f)
            elif v.icon():
                v.setIconSize(QSize(w, h))
            v.setFixedSize(w, h)
