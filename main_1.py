import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from main_2 import Checking

class App(QWidget):
 
    def initUI(self, MainWindow):
        MainWindow.setObjectName("what's your name")
        MainWindow.resize(300,200)
        MainWindow.move(200,400)
        self.centralwidget = QWidget(MainWindow)

        self.explain = QLabel(self.centralwidget)
        self.explain.setGeometry(QRect(40,30,250,40))
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.explain.setFont(font)
        self.explain.setObjectName('question')
        
        self.choice_room_button1 = QPushButton(self.centralwidget)
        self.choice_room_button1.setGeometry(QRect(50,100,70,60))
        self.choice_room_button1.setObjectName('hahaha')
        self.choice_room_button1.setToolTip('10평 대 미만!')
        self.choice_room_button1.clicked.connect(lambda:self.openWindow('원룸'))

        self.choice_room_button2 = QPushButton(self.centralwidget)
        self.choice_room_button2.setGeometry(QRect(170,100,70,60))
        self.choice_room_button2.setObjectName('babo')
        self.choice_room_button2.setToolTip('10평 이상!')
        self.choice_room_button2.clicked.connect(lambda:self.openWindow('투룸'))

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def openWindow(self,room):
        self.window = QMainWindow()
        self.ui = Checking()
        self.ui.make_checkbox(self.window,room)
        self.window.show()

    def retranslateUi(self, MainWindow):
        translate = QCoreApplication.translate
        MainWindow.setWindowTitle(translate("MainWindow","불판 1"))
        self.explain.setText(translate('MainWindow','방 사이즈.. 선택해보등가...'))
        self.choice_room_button1.setText(translate('MainWindow','원룸'))
        self.choice_room_button2.setText(translate('MainWindow','투룸'))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = App()
    ui.initUI(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())