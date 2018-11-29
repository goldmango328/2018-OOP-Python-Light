import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from main_3 import Teama

class Checking(object):

    def make_checkbox(self, OtherWindow):    # 의자, 책상, 소파, 옷장
        OtherWindow.setObjectName("please help")
        OtherWindow.resize(150,250)
        OtherWindow.move(600,400)
        self.centralwidget = QWidget(OtherWindow)
        self.centralwidget.setObjectName("hi, I'm Baymax!")
                
        self.checkbox1 = QCheckBox(self.centralwidget)
        self.checkbox1.setGeometry(QRect(50,20,150,30))
        self.checkbox1.stateChanged.connect(self.state)
        
        self.checkbox2 = QCheckBox(self.centralwidget)
        self.checkbox2.setGeometry(QRect(50,50,150,30))
        self.checkbox2.stateChanged.connect(self.state)
        
        self.checkbox3 = QCheckBox(self.centralwidget)
        self.checkbox3.setGeometry(QRect(50,80,150,30))
        self.checkbox3.stateChanged.connect(self.state)
        
        self.checkbox4 = QCheckBox(self.centralwidget)
        self.checkbox4.setGeometry(QRect(50,110,150,30))
        self.checkbox4.stateChanged.connect(self.state)

        self.next = QPushButton(self.centralwidget)
        self.next.setGeometry(QRect(50,180,50,30))
        font = QFont()
        font.setBold(True)
        self.next.setFont(font)
        self.next.setObjectName('congratulation')
        self.next.clicked.connect(self.NextWindow)

        OtherWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(OtherWindow)
        self.retranslateUi(OtherWindow)
        QMetaObject.connectSlotsByName(OtherWindow)

    def NextWindow(self):
        self.window = QMainWindow()
        self.ui = Teama()
        self.ui.make_checkbox(self.window)
        self.window.show()

    def retranslateUi(self, OtherWindow):
        translate = QCoreApplication.translate
        OtherWindow.setWindowTitle(translate("OtherWindow", "멧돌 2"))
        self.checkbox1.setText(translate("OtherWindow",'의자'))
        self.checkbox2.setText(translate("OtherWindow",'책상'))
        self.checkbox3.setText(translate("OtherWindow",'소파'))
        self.checkbox4.setText(translate("OtherWindow",'옷장'))
        self.next.setText(translate("OtherWindow",'완료'))
                           
    def state(self):
        msg = ""
        if self.checkbox1.isChecked() == True:
            msg += "의자 "
        if self.checkbox2.isChecked() == True:
            msg += "책상 "
        if self.checkbox3.isChecked() == True:
            msg += "소파 "
        if self.checkbox4.isChecked() == True:
            msg += "옷장 "
        print(msg)
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    OtherWindow = QMainWindow()
    ui = Checking()
    ui.make_checkbox(OtherWindow)
    OtherWindow.show()
    sys.exit(app.exec_())
    
