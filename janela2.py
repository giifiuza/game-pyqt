import sys
from time import sleep
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets, uic


class SubWindow(QWidget):
    def __init__(self, parent = None):
        super(SubWindow, self).__init__(parent)
        self.setGeometry(100, 100, 600, 400)
        self.labels()

    def labels(self):
        self.label1 = QLabel(self)
        self.label1.setText("Rock Paper Scissors")
        self.label1.move(130, 40)
        self.label1.setStyleSheet('QLabel {font:bold;font-family: Arial;font-size:20px;color:"#40128B"}')
        self.label1.resize(250, 20)

        self.label2 = QLabel(self)
        self.label2.setText("What's your name?")
        self.label2.move(140, 100)
        self.label2.setStyleSheet('QLabel {font:bold;font-family: Arial;font-size:20px;color:"#000000"}')
        self.label2.resize(250, 20)

        self.caixa_texto = QLineEdit(self)
        self.caixa_texto.setStyleSheet('QLabel {font:bold;font-family: Arial;font-size:20px;color:"#000000", background: #ffffff}')
        self.caixa_texto.move(150, 180)
        self.caixa_texto.resize(150, 35)

    def closeEvent(self, event):
        event.ignore()


class MainWindow(QWidget):
    def __init__(self, parent = None):

        super(MainWindow, self).__init__(parent)
        self.setGeometry(100, 100, 450, 350)
        self.setStyleSheet("background-color: #cedeff;")
        self.Button()
        self.labels()
        self.show()

    def Button(self):
        button = QPushButton("ENTER", self)
        button.setGeometry(170, 270, 20, 40)
        button.clicked.connect(self.openSub)
        button.clicked.connect(self.read)
        button.setStyleSheet("border-radius: 30px; "
                             "background-color: #40128B; "
                             "color: #ffffff;"
                             "font-weight: bold;"
                             "font-family: Arial;"
                             "font-size: 20px")
        button.resize(120, 60)

    def labels(self):
        self.label1 = QLabel(self)
        self.label1.setText("Rock Paper Scissors")
        self.label1.move(130, 40)
        self.label1.setStyleSheet('QLabel {font:bold;font-family: Arial;font-size:20px;color:"#40128B"}')
        self.label1.resize(250, 20)

        self.label2 = QLabel(self)
        self.label2.setText("What's your name?")
        self.label2.move(140, 100)
        self.label2.setStyleSheet('QLabel {font:bold;font-family: Arial;font-size:20px;color:"#000000"}')
        self.label2.resize(250, 20)

        self.caixa_texto = QLineEdit(self)
        self.caixa_texto.setStyleSheet(
            'QLabel {font:bold;font-family: Arial;font-size:20px;color:"#000000", background: #ffffff}')
        self.caixa_texto.move(150, 180)
        self.caixa_texto.resize(150, 35)

    def read(self):
        texto = self.caixa_texto.text()
        self.caixa_texto.setText("")
        print(texto)

    def openSub(self):
        self.sub = SubWindow()
        self.sub.show()

    def closeEvent(self,event):
        widgetList = QApplication.topLevelWidgets()
        numWindows = len(widgetList)
        if numWindows > 1:
            event.accept()
        else:
            event.ignore()


app = QApplication(sys.argv)
mainWin =MainWindow()
mainWin.show()
sys.exit(app.exec_())