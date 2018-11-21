# please 파일이 필요해요! 같이 다운받아서 실행시켜주세요!!

import sys
from PyQt5.QtWidgets import QWidget, QListWidget, QListWidgetItem, QLabel, QPushButton, QApplication
import please

class exampleWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        listWidget = QListWidget(self)
        listWidget.itemDoubleClicked.connect(self.buildExamplePopup)

        names = ["박서영 바보", "박서영 멍청이", "박서영 똥개", "박서영 해삼", "박서영 말미잘"]

        for n in names:
            QListWidgetItem(n, listWidget)

        self.setGeometry(1200, 500, 250, 180)
        self.show()

    @staticmethod
    def buildExamplePopup(item):
        name = item.text()
        exPopup = examplePopup(name)
        exPopup.setGeometry(100, 200, 100, 100)
        exPopup.show()


class examplePopup(QWidget):
    def __init__(self, name):
        super().__init__()

        self.name = name

        self.initUI()

    def initUI(self):
        lblName = QLabel(self.name, self)
        please.play(self.name)
        print("I'm here")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = exampleWidget()
    sys.exit(app.exec_())
