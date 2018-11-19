from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
        QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
        QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
        QVBoxLayout)
 
import sys
 
class Dialog(QDialog):
 
    def slot_method1(self):             # 버튼이 눌려지면 실행될 함수
        print('으아악.. 눌려졌어..')

    def slot_method2(self):             # 위와 동일한 기능
        print('내놔!!!!')
 
    def __init__(self):
        super(Dialog, self).__init__()  # 상속받은 QDialog의 init 실행
 
        button1=QPushButton("또 누르게..?")         # 1번 버튼 이름 설정
        button1.clicked.connect(self.slot_method1)      # 1번 버튼 클릭 시 1번 함수 실행

        button2=QPushButton("하리보...?")          # 2번 버튼 이름 설정
        button2.clicked.connect(self.slot_method2)      # 2번 버튼 클릭 시 2번 함수 실행
 
        mainLayout = QVBoxLayout()              # 작은 창 세팅..?
        mainLayout.addWidget(button1)           # 작은 창 안에 1번 버튼 추가
        mainLayout.addWidget(button2)           # 작은 창 안에 2번 버튼 추가
 
        self.setLayout(mainLayout)              # 작은 창 띄우기
        self.setWindowTitle("갈")                # 작은 창 이름
 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = Dialog()
sys.exit(dialog.exec_())
