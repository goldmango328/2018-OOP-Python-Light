from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
        QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
        QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
        QVBoxLayout)
 
import sys
 
class Dialog(QDialog):
 
    def slot_method(self):              # 버튼이 눌리면 실행되는 함수
        print('으아악.. 눌려졌어..')   
 
    def __init__(self):
        super(Dialog, self).__init__()
 
        button=QPushButton("또 누르게..?")          # 버튼에 쓰여질 글
        button.clicked.connect(self.slot_method)        # 버튼이 눌린다면 slot_method 
 
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(button)
 
        self.setLayout(mainLayout)
        self.setWindowTitle("갈")
 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = Dialog()
sys.exit(dialog.exec_())
