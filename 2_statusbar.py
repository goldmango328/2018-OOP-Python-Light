import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QIcon
 
class App(QMainWindow):
 
    def __init__(self,left,top,width,height):
        super().__init__()
        self.title = '멧돌은 갈갈갈'  # 창의 이름
        self.left = left #10    # 모니터 내 창의 위치(x)
        self.top = top #10      # 모니터 내 창의 위치(y)
        self.width = width #640     # 창 사이즈(가로)
        self.height = height #480   # 창 사이즈(세로)
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.statusBar().showMessage('갈갈갈갈...')
        self.show()
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App(1200,500,640,480)
    sys.exit(app.exec_())
