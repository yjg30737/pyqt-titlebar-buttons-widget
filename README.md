# pyqt-titlebar-buttons-widget
PyQt buttons (e.g. min/max/close) widget for title bar or menu bar 

## Requirements
* PyQt5 >= 5.8

## Setup
`python -m pip install pyqt-titlebar-buttons-widget`

## Included Packages
* <a href="https://github.com/yjg30737/pyqt-svg-icon-pushbutton.git">pyqt-svg-icon-pushbutton</a>

## Package Inherited by This
* <a href="https://github.com/yjg30737/pyqt-windows-min-max-close-buttons-widget.git">pyqt-windows-min-max-close-buttons-widget</a>
* <a href="https://github.com/yjg30737/pyqt-mac-min-max-close-buttons-widget.git">pyqt-mac-min-max-close-buttons-widget</a>

## Class, Methods Overview
* `TitlebarButtonsWidget(hint=['min, 'max', 'close'])` - Constructor.
* `getMinimizedBtn()`, `getMaximizedBtn()`, `getCloseBtn()`. I belive these three methods are quite self-explanatory.

## Note
This package was actually made for those two packages i mentioned. Reducing redundancy.

<b>=== 2022/5/11 ===</b>

I'm working on other features such as help/tack buttons.

I could be working on adding another widgets(e.g. search bar) beside the buttons. So far i'm only working on the button because that seems to be the most generic feature.
