import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
 
class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = '멧돌은 갈갈갈' # 창 이름
        self.left = 10 # 모니터 내 창의 위치 (x)
        self.top = 10 # 모니터 내 창의 위치 (y)
        self.width = 640 # 창 사이즈 (가로)
        self.height = 480 # 창 사이즈 (세로)
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
