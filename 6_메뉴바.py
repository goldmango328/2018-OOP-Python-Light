import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
 
class App(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.title = '컵라면'
        self.left = 1200
        self.top = 500
        self.width = 640
        self.height = 400
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        mainMenu = self.menuBar() 
        fileMenu = mainMenu.addMenu('의자') # 메뉴 추가
        editMenu = mainMenu.addMenu('침대')
        viewMenu = mainMenu.addMenu('책상')
        searchMenu = mainMenu.addMenu('가구')
        toolsMenu = mainMenu.addMenu('또가구')
        helpMenu = mainMenu.addMenu('가구그만')
 
        exitButton = QAction(QIcon('exit24.png'), '나가려고?', self) # 메뉴 속 버튼의 아이콘
        exitButton.setShortcut('Q')    # 버튼의 단축키
        # exitButton.setStatusTip('얘는 뭐지..?') # 밑에서 상태를 알려주는 함수라고는 한다.
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)
 
        self.show()
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
