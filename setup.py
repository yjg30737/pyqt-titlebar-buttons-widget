from setuptools import setup, find_packages

setup(
    name='pyqt-titlebar-buttons-widget',
    version='0.0.2',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'pyqt_titlebar_buttons_widget.ico': ['full_screen.svg', 'help.svg', 'tack.svg',
                                                            'fold.svg', 'unfold.svg']},
    description='PyQt buttons (e.g. min/max/close) widget for title bar or menu bar',
    url='https://github.com/yjg30737/pyqt-titlebar-buttons-widget.git',
    install_requires=[
        'PyQt5>=5.8',
        'pyqt-svg-icon-text-widget>=0.0.1'
    ]
)