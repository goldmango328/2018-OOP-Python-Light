import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
 
class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = '멧돌_선택박스'	 	# 창 이름
        self.left = 1200            	# 모니터 내 창 위치(x)
        self.top = 500     				# 모니터 내 창 위치(y)					
        self.width = 320				# 창 사이즈 (가로)
        self.height = 200				# 창 사이즈 (세로)
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

		'''
		QMessageBox.Cancel	
		QMessageBox.Ok	
		QMessageBox.Help
		QMessageBox.Open	
		QMessageBox.Save	
		QMessageBox.SaveAll
		QMessageBox.Discard	
		QMessageBox.Close	
		QMessageBox.Apply
		QMessageBox.Reset	
		QMessageBox.Yes	
		QMessageBox.YesToAll
		QMessageBox.No	
		QMessageBox.NoToAll	
		QMessageBox.NoButton
		QMessageBox.RestoreDefaults	
		QMessageBox.Abort	
		QMessageBox.Retry
		QMessageBox.Ignore
		'''
        while True :
            buttonReply = QMessageBox.question(self, self.title, "종료하실건가요..??", QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            if buttonReply == QMessageBox.Yes:
                print('화이팅.. 힘내세요..')
                break
            if buttonReply == QMessageBox.Cancel:
                print('앗 실수;;')
                break
            else:
                print('다음번엔 종료를...;;')
     
        #self.show()
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
