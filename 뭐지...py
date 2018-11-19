from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
        QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
        QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
        QVBoxLayout)
 
import sys
 
class Dialog(QDialog):
 
    def slot_method(self):
        print('으아악.. 눌려졌어..')
 
    def __init__(self):
        super(Dialog, self).__init__()
 
        button=QPushButton("또 누르게..?")
        button.clicked.connect(self.slot_method)
 
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(button)
 
        self.setLayout(mainLayout)
        self.setWindowTitle("갈")
 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = Dialog()
sys.exit(dialog.exec_())
