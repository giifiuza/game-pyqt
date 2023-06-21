import sys
from time import sleep
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets, uic, QtCore


class MainWindow(QWidget):
    def __init__(self, parent = None):

        super(MainWindow, self).__init__(parent)
        self.setGeometry(100, 100, 450, 350)
        self.setStyleSheet("background-color: #cedeff;")
        self.setWindowTitle("Welcome")
        self.Button()
        self.labels()
        self.show()

    def Button(self):
        button = QPushButton("ENTER", self)
        button.setGeometry(170, 270, 20, 40)
        button.clicked.connect(self.openSub)
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
        self.label1.move(125, 40)
        self.label1.setStyleSheet('QLabel {font:bold;font-family: Arial;font-size:22px;color:"#40128B"}')
        self.label1.resize(250, 30)

        self.label2 = QLabel(self)
        self.label2.setText("What's your name?")
        self.label2.move(140, 150)
        self.label2.setStyleSheet('QLabel {font:bold;font-family: Arial;font-size:20px;color:"#000000"}')
        self.label2.resize(250, 20)

        self.label3 = QLabel(self)
        self.label3.setText("Enter your name to start playing")
        self.label3.move(75, 90)
        self.label3.setStyleSheet('QLabel {font:bold;font-family: Arial;font-size:20px;color:"#000000"}')
        self.label3.resize(310, 30)

        self.caixa_texto = QLineEdit(self)
        self.caixa_texto.setStyleSheet(
            'QLabel {font:bold;font-family: Arial;font-size:20px;color:"#000000", background: #ffffff}')
        self.caixa_texto.move(150, 200)
        self.caixa_texto.resize(150, 35)

    def read(self):
        self.texto = self.caixa_texto.text()
        self.caixa_texto.setText("")
        print(self.texto)

    def openSub(self):
        self.sub = SubWindow(self.caixa_texto.text())
        if self.sub.nome:  # Verifica se o nome não está vazio
            self.sub.show()
            self.caixa_texto.clear()

    def closeEvent(self,event):
        widgetList = QApplication.topLevelWidgets()
        numWindows = len(widgetList)
        if numWindows > 1:
            event.accept()
        else:
            event.ignore()


class SubWindow(QWidget):
    def __init__(self, name, parent = None):
        super(SubWindow, self).__init__(parent)
        self.setGeometry(100, 100, 750, 500)
        self.setStyleSheet("background-color: #cedeff;")
        self.setWindowTitle("Rules of the game")
        self.labels(name)
        self.nome = name

    def labels(self, name):
        self.label_rules = QLabel(self)
        self.label_rules.setText("Rules")
        self.label_rules.move(340, 40)
        self.label_rules.setStyleSheet('QLabel {font:bold;font-family: Poppins;font-size:24px;color:"#40128B"}')
        self.label_rules.resize(250, 20)



        self.label_text = QLabel(self)

        self.label_text.setText(f"Welcome to the game, {name}!\n")
        self.label_text.move(275, 80)
        self.label_text.setStyleSheet('QLabel {font:bold;font-family: Arial;font-size:20px;color:"#40128B"}')
        self.label_text.resize(350, 50)

        self.label_text1 = QLabel(self)
        self.label_text1.setText("You have 10 seconds to win as many times as possible against the computer.\n"
                                "Choose one of three options, and the computer will make it's \nown random selection. "
                                "Compare the choices to determine the winner or \nif it's a tie. "
                                "After each round, the result is shown, and you can play \nagain immediately. "
                                "If you don't choose within 1 second, the computer wins. \nAfter 10 seconds, the final winner "
                                "and points are displayed. Test your skills \nand aim for maximum victories within the time limit.\n\nGood Luck!!!")

        self.label_text1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_text1.move(30, 110)
        self.label_text1.setStyleSheet('QLabel {font-family: Arial;font-size:20px;color:"#000000"}')
        self.label_text1.resize(700, 300)

        self.btn_play = QPushButton("PLAY", self)
        self.btn_play.move(29, 400)
        self.btn_play.clicked.connect(self.close)
        self.btn_play.setStyleSheet("border-radius: 30px; "
                             "background-color: #40128B; "
                             "color: #ffffff;"
                             "font-weight: bold;"
                             "font-family: Arial;"
                             "font-size: 20px")
        self.btn_play.resize(200, 60)



    def closeEvent(self, event):
        event.ignore()

app = QApplication(sys.argv)
mainWin =MainWindow()
mainWin.show()
sys.exit(app.exec_())