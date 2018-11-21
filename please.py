import sys
from PyQt5.QtWidgets import *


class exampleWidget(QWidget):
    def __init__(self,name):
        super().__init__()
        self.name = name
        self.initUI()

    def initUI(self):
        QMessageBox.warning(self, "*조심*", "%s(이)라고요..? 뒷통수를 조심하세요..." %(self.name))

def play(name):
    app = QApplication(sys.argv)
    ex = exampleWidget(name)
    sys.exit(app.exec_())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = exampleWidget("유현아 바보!")
    sys.exit(app.exec_())
