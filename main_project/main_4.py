import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import urllib.request
#from io import StringIO

class Images(object):

    def show_images(self, OtherWindow):
        OtherWindow.resize(300,200)
        OtherWindow.move(10,10)
        self.centralwidget = QWidget(OtherWindow)

        
        image_url = 'https://images.homify.com/c_fill,f_auto,h_700,q_auto/v1490248980/p/photo/image/1918911/IMG_6320.jpg'
        data = urllib.request.urlopen(image_url).read()
        image = QImage()
        image.loadFromData(data)
        lbl = QLabel(self.centralwidget)
        lbli = QPixmap(image)
        lblii = lbli.scaled(500,500,Qt.KeepAspectRatio)
        lbl.setPixmap(lblii)
        OtherWindow.resize(lblii.width(), lblii.height())

        OtherWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(OtherWindow)
        self.retranslateUi(OtherWindow)
        QMetaObject.connectSlotsByName(OtherWindow)

    def retranslateUi(self, OtherWindow):
        translate = QCoreApplication.translate
        OtherWindow.setWindowTitle(translate("OtherWindow", "멧돌 4"))
        #self.next.setText(translate("OtherWindow",'완료'))
                           
if __name__ == '__main__':
    app = QApplication(sys.argv)
    OtherWindow = QMainWindow()
    ui = Images()
    ui.show_images(OtherWindow)
    OtherWindow.show()
    sys.exit(app.exec_())
    
