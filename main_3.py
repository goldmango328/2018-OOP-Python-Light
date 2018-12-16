import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from main_4 import Images

class Teama(object):

    def make_checkbox(self, OtherWindow, room, msg):
        OtherWindow.setObjectName("ester egg")
        OtherWindow.resize(150,250)
        OtherWindow.move(800,400)
        self.centralwidget = QWidget(OtherWindow)
        self.centralwidget.setObjectName("I'm grooot")
        self.room = room
        self.msg = msg

        self.theme = '미정'
                
        self.checkbox1 = QCheckBox(self.centralwidget)
        self.checkbox1.setGeometry(QRect(50,20,150,30))
        self.checkbox1.stateChanged.connect(self.state1)
        
        self.checkbox2 = QCheckBox(self.centralwidget)
        self.checkbox2.setGeometry(QRect(50,50,150,30))
        self.checkbox2.stateChanged.connect(self.state2)
        
        self.checkbox3 = QCheckBox(self.centralwidget)
        self.checkbox3.setGeometry(QRect(50,80,150,30))
        self.checkbox3.stateChanged.connect(self.state3)
        
        self.checkbox4 = QCheckBox(self.centralwidget)
        self.checkbox4.setGeometry(QRect(50,110,150,30))
        self.checkbox4.stateChanged.connect(self.state4)

        self.next = QPushButton(self.centralwidget)
        self.next.setGeometry(QRect(50,180,50,30))
        font = QFont()
        font.setBold(True)
        self.next.setFont(font)
        self.next.setObjectName('happy happy happy day...?')
        self.next.clicked.connect(self.NextWindow)

        OtherWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(OtherWindow)
        self.retranslateUi(OtherWindow)
        QMetaObject.connectSlotsByName(OtherWindow)

    def NextWindow(self):
        self.window = QMainWindow()
        self.ui = Images()
        self.ui.show_images(self.window, self.room, self.msg, self.theme)
        self.window.show()

    def retranslateUi(self, OtherWindow):
        translate = QCoreApplication.translate
        OtherWindow.setWindowTitle(translate("OtherWindow", "불판 3"))
        self.checkbox1.setText(translate("OtherWindow",'모던'))
        self.checkbox2.setText(translate("OtherWindow",'미니멀'))
        self.checkbox3.setText(translate("OtherWindow",'북유럽'))
        self.checkbox4.setText(translate("OtherWindow",'컨트리'))
        self.next.setText(translate("OtherWindow",'완료'))
                           
    def state1(self):
        if self.checkbox1.isChecked() == True:
            #print("모던")
            self.checkbox2.setChecked(False)
            self.checkbox3.setChecked(False)
            self.checkbox4.setChecked(False)
            self.theme = '모던' 

    def state2(self):
        if self.checkbox2.isChecked() == True:
            #print("미니멀")
            self.checkbox1.setChecked(False)
            self.checkbox3.setChecked(False)
            self.checkbox4.setChecked(False)
            self.theme = '미니멀'

    def state3(self):
        if self.checkbox3.isChecked() == True:
            #print("북유럽")
            self.checkbox1.setChecked(False)
            self.checkbox2.setChecked(False)
            self.checkbox4.setChecked(False)
            self.theme = '북유럽'

    def state4(self):
        if self.checkbox4.isChecked() == True:
            #print("컨트리")
            self.checkbox1.setChecked(False)
            self.checkbox2.setChecked(False)
            self.checkbox3.setChecked(False)
            self.theme = '컨트리'
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    OtherWindow = QMainWindow()
    ui = Teama()
    ui.make_checkbox(OtherWindow,'test 방', 'test 가구')
    OtherWindow.show()
    sys.exit(app.exec_())
    
