import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
 
class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = '멧돌은 갈갈갈' #1200,500,640,480
        self.left = 1200 # 모니터 내 창 위치(x)
        self.top = 500 # 모니터 내 창 위치(y)
        self.width = 280 # 모니터 사이즈(가로)
        self.height = 200 # 모니터 사이즈(세로)
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        button = QPushButton('눌러봐', self)
        button.setToolTip('당신이 멧돌이라면...')
        button.move(100,70) # 창 내 버튼의 위치
        button.clicked.connect(self.on_click)
 
        self.show()
 
    @pyqtSlot()
    def on_click(self): # 클릭하면...
        print('현아 일어나!!!')
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
