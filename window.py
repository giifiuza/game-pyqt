import sys
import threading
from random import choice
from time import sleep
import re
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import *
from PyQt5 import QtWidgets, uic, QtCore, QtGui


class MainWindow(QWidget):
    def __init__(self, parent=None):
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
        button.clicked.connect(self.openSecond)
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
        self.label1.setStyleSheet('QLabel {font:bold;'
                                  'font-family: Arial;'
                                  'font-size:22px;'
                                  'color:"#40128B"}')
        self.label1.resize(250, 30)

        self.label2 = QLabel(self)
        self.label2.setText("What's your name?")
        self.label2.move(140, 150)
        self.label2.setStyleSheet('QLabel {font:bold;'
                                  'font-family: Arial;'
                                  'font-size:20px;'
                                  'color:"#000000"}')
        self.label2.resize(250, 20)

        self.label3 = QLabel(self)
        self.label3.setText("Enter your name to start playing")
        self.label3.move(75, 90)
        self.label3.setStyleSheet('QLabel {font:bold;'
                                  'font-family: Arial;'
                                  'font-size:20px;'
                                  'color:"#000000"}')
        self.label3.resize(310, 30)

        self.caixa_texto = QLineEdit(self)
        self.caixa_texto.setStyleSheet(
            'QLabel {font:bold;font-family: Arial;'
            'font-size:20px;'
            'color:"#000000", '
            'background: #ffffff}')
        self.caixa_texto.move(150, 200)
        self.caixa_texto.resize(150, 35)

    def read(self):
        self.texto = self.caixa_texto.text()
        self.caixa_texto.setText("")
        if not self.texto.isalpha():
            QMessageBox.warning(self, "Erro", "Only letter. Please try again!")
        else:
            print('tudo certo')

    def openSecond(self):
        self.close()
        self.second = SecondWindow(self.caixa_texto.text())
        if self.second.nome:
            self.second.show()
            self.caixa_texto.clear()


class SecondWindow(QWidget):
    def __init__(self, name, parent=None):
        super(SecondWindow, self).__init__(parent)
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
        self.label_text.move(0, 80)
        self.label_text.setStyleSheet('QLabel {font:bold;font-family: Arial;font-size:20px;color:"#40128B"}')
        self.label_text.resize(750, 50)
        self.label_text.setAlignment(QtCore.Qt.AlignCenter)

        self.label_text1 = QLabel(self)
        self.label_text1.setText(
            "You have 10 seconds to win as many times as possible against the computer.\n"
            "Choose one of three options, and the computer will make its \nrandom selection. "
            "Compare the choices to determine the winner or \nif it's a tie. "
            "After each round, the result is shown, and you can play \nagain immediately. "
            "If you don't choose within 1 second, the computer wins. \nAfter 10 seconds, the final winner "
            "and points are displayed. Test your skills \nand aim for maximum victories within the time limit."
            "\n\nGood Luck!!!")

        self.label_text1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_text1.move(30, 110)
        self.label_text1.setStyleSheet('QLabel {font-family: Arial;font-size:20px;color:"#000000"}')
        self.label_text1.resize(700, 300)

        self.btn_play = QPushButton("START", self)
        self.btn_play.move(285, 400)
        self.btn_play.clicked.connect(self.openThird)
        self.btn_play.setStyleSheet("border-radius: 30px;"
                                    "background-color: #40128B;"
                                    "color: #ffffff;"
                                    "font-weight: bold;"
                                    "font-family: Arial;"
                                    "font-size: 20px")
        self.btn_play.resize(200, 60)

    def openThird(self):
        self.close()
        self.third = ThirdWindow()
        self.third.show()


class ThirdWindow(QWidget):
    def __init__(self, parent=None):
        super(ThirdWindow, self).__init__(parent)
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #cedeff;")
        self.setWindowTitle("Game - Rock, Paper and Scissors")
        self.labels()
        self.buttons()

        self.timer = QTimer()
        self.timer.timeout.connect(self.computerChoice)

        self.timer_10 = QTimer()
        self.timer_10 .timeout.connect(self.updateTimer)
        self.remaining_time = 20
        self.timer_10 .start(1000)
        self.label_timer = QLabel(f"Time: {self.remaining_time}", self)
        self.label_timer.setFont(QFont('Arial', 12))
        self.label_timer.setStyleSheet("font-weight: bold;")
        self.label_timer.move(380, 115)

    def labels(self):
        self.label_user = QLabel(self)
        self.label_user.move(80, 130)
        self.label_user.resize(210, 210)

        self.label_computer = QLabel(self)
        self.label_computer.move(550, 130)
        self.label_computer.resize(210, 210)

        self.label_vs = QLabel(self)
        self.label_vs.move(350, 170)
        self.label_vs.resize(140, 140)
        self.label_vs.setScaledContents(True)
        self.label_vs.setPixmap(QtGui.QPixmap('images/vs.png'))

        self.user_score_label = QLabel("User Score: 0", self)
        self.user_score_label.setFont(QFont('Arial', 12))
        self.user_score_label.setStyleSheet("font-weight: bold;")
        self.user_score_label.move(120, 115)

        self.computer_score_label = QLabel("Computer Score: 0", self)
        self.computer_score_label.setFont(QFont('Arial', 12))
        self.computer_score_label.setStyleSheet("font-weight: bold;")
        self.computer_score_label.move(585, 115)

    def buttons(self):
        self.btn_rock = QPushButton(self)
        self.btn_rock.move(150, 400)
        icon_rock = QtGui.QIcon()
        icon_rock.addPixmap(QtGui.QPixmap("./images/rock-label.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_rock.setIcon(icon_rock)
        self.btn_rock.setIconSize(QtCore.QSize(170, 170))
        self.btn_rock.setStyleSheet("border-radius:5px; background: #cedeff;")
        self.btn_rock.resize(150, 150)
        self.btn_rock.clicked.connect(self.changeRock)

        self.btn_paper = QPushButton(self)
        self.btn_paper.move(350, 400)
        icon_paper = QtGui.QIcon()
        icon_paper.addPixmap(QtGui.QPixmap("./images/paper-label.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_paper.setIcon(icon_paper)
        self.btn_paper.setIconSize(QtCore.QSize(180, 180))
        self.btn_paper.setStyleSheet("border-radius:5px; background: #cedeff;")
        self.btn_paper.resize(150, 150)
        self.btn_paper.clicked.connect(self.changePaper)

        self.btn_scissors = QPushButton(self)
        self.btn_scissors.move(550, 400)
        icon_scissors = QtGui.QIcon()
        icon_scissors.addPixmap(QtGui.QPixmap("./images/scissors-label.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_scissors.setIcon(icon_scissors)
        self.btn_scissors.setIconSize(QtCore.QSize(140, 140))
        self.btn_scissors.setStyleSheet("border-radius:5px; background: #cedeff;")
        self.btn_scissors.resize(150, 150)
        self.btn_scissors.clicked.connect(self.changeScissors)

        self.btn_play2 = QPushButton("PLAY", self)
        self.btn_play2.move(650, 40)
        self.btn_play2.clicked.connect(self.startTimer)
        self.btn_play2.setStyleSheet(
            "background-color: #40128B;"
            "border-radius: 10px; "
            "color: #ffffff;"
            "font-weight: bold;"
            "font-family: Arial;"
            "font-size: 20px")
        self.btn_play2.resize(80, 40)

    def changePaper(self):
        self.userChoice = 1
        self.label_user.setPixmap(QtGui.QPixmap('images/paper-label.png'))
        self.label_user.setScaledContents(True)

    def changeRock(self):
        self.userChoice = 2
        self.label_user.setPixmap(QtGui.QPixmap('images/rock-label.png'))
        self.label_user.setScaledContents(True)

    def changeScissors(self):
        self.userChoice = 3
        self.label_user.setPixmap(QtGui.QPixmap('images/scissors-label.png'))
        self.label_user.setScaledContents(True)

    def computerChoice(self):
        lista = ['papel', 'pedra', 'tesoura']
        self.choicePC= choice(lista)
        if self.choicePC == 'papel':
            self.pc = 1
            self.label_computer.setPixmap(QtGui.QPixmap('images/paper-label.png'))
            self.label_computer.setScaledContents(True)
        elif self.choicePC == 'pedra':
            self.pc = 2
            self.label_computer.setPixmap(QtGui.QPixmap('images/rock-label.png'))
            self.label_computer.setScaledContents(True)
        elif self.choicePC == 'tesoura':
            self.pc = 3
            self.label_computer.setPixmap(QtGui.QPixmap('images/scissors-label.png'))
            self.label_computer.setScaledContents(True)

        # self.checkWin()

    def checkWin(self):

        self.pontoPC = 0
        self.pontoUser = 0

        if self.pc == self.userChoice :
            self.pontoPC += 0
            self.pontoUser += 0
        elif (self.pc == 1 and self.userChoice == 2) or (self.pc == 2 and self.userChoice == 3) or (self.pc == 3 and self.userChoice == 1):
            self.pontoPC += 1
        elif (self.pc == 1 and self.userChoice == 3) or (self.pc == 2 and self.userChoice == 1) or (self.pc == 3 and self.userChoice == 2):
            self.pontoUser += 1

        self.user_score_label.setText(f"User Score: {self.pontoUser}")
        self.computer_score_label.setText(f"Computer Score: {self.pontoPC}")

    def startTimer(self):
        self.timer.start(1000)

    def updateTimer(self):
        self.remaining_time -= 1
        self.label_timer.setText(f"Time: {self.remaining_time}")
        if self.remaining_time <= 0:
            self.btn_paper.setEnabled(False)
            self.btn_rock.setEnabled(False)
            self.btn_scissors.setEnabled(False)
            self.timer.stop()
            sleep(3)
            QMessageBox.about(self, 'Ending Game', "Gonna close!")
            self.close()


app = QApplication(sys.argv)
mainWin = MainWindow()
mainWin.show()
sys.exit(app.exec_())
