from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import main_1, main_2

class Second(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()
    def setupUi(self):
        self.setWindowTitle("please")

class First(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()
    def setupUi(self):
        self.setWindowTitle("help")
        btn1 = QPushButton("Click me", self)
        btn1.move(20, 20)
        btn1.clicked.connect(self.btn1_clicked)
    def btn1_clicked(self):
        #QMessageBox.about(self, "message", "clicked")
        main2()
        
        
def main1():
    app = QApplication(sys.argv)
    main1 = First()
    main1.show()
    sys.exit(app.exec_())

def main2():
    app = QApplication(sts.argv)
    main2 = Second()
    main2.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main1()  

    
# 하나의 window에서 버튼을 누르면 또 다른 window가 열리도록 하는 코드!!! ...를 만들고 싶어요;;
