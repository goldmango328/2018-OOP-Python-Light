import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
 
class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = '원룸 / 투룸 입력'
        self.left = 1200
        self.top = 500
        self.width = 280
        self.height = 200 
        self.initUI()

    def clicked1(self):
        print('원룸이 클릭되셨습니다..')
        self.one_room()

    def clicked2(self):
        print('투룸이 클릭되셨습니다..')
        self.two_room()

    def one_room(self):
        test_button = QPushButton("test")
        test_button.move(50,150)

    def two_room(self):
        print("It's just going")
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        choice_room_button1 = QPushButton('원룸', self)
        choice_room_button1.setToolTip('10평 대 미만!')
        choice_room_button1.move(50,70)
        choice_room_button1.clicked.connect(self.clicked1)

        choice_room_button2 = QPushButton('투룸', self)
        choice_room_button2.setToolTip('10평 이상!')
        choice_room_button2.move(150,70)
        choice_room_button2.clicked.connect(self.clicked2)
        
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    apple = App()
    sys.exit(app.exec_())
    
'''
class Dialog(QDialog):
    NumGridRows = 10
    NumButtons = 2
 
    def __init__(self):
        super(Dialog, self).__init__()
 
        b1=QPushButton("원룸")
        b1.setToolTip('10평 대 미만!')
        b2=QPushButton("투룸 이상")
        b2.setToolTip('10평 이상!')
 
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(b1)
        mainLayout.addWidget(b2)
 
        self.setLayout(mainLayout)
        self.setWindowTitle("원룸 / 투룸 입력")
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = Dialog()
    sys.exit(dialog.exec_())
'''
