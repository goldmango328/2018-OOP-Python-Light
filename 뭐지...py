from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
        QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
        QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
        QVBoxLayout)
 
import sys
 
class Dialog(QDialog):
 
    def slot_method1(self):
        print('으아악.. 눌려졌어..')

    def slot_method2(self):
        print('내놔!!!!')
 
    def __init__(self):
        super(Dialog, self).__init__()
 
        button1=QPushButton("또 누르게..?")
        button1.clicked.connect(self.slot_method1)

        button2=QPushButton("하리보...?")
        button2.clicked.connect(self.slot_method2)
 
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(button1)
        mainLayout.addWidget(button2)
 
        self.setLayout(mainLayout)
        self.setWindowTitle("갈")
 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = Dialog()
sys.exit(dialog.exec_())
