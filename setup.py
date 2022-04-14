from setuptools import setup, find_packages

setup(
    name='pyqt-min-max-close-buttons-widget',
    version='0.0.2',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='PyQt modern min/max/close buttons widget for title bar or menu bar',
    url='https://github.com/yjg30737/pyqt-min-max-close-buttons-widget.git',
    install_requires=[
        'PyQt5>=5.8'
    ]
)