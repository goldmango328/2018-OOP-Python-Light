import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import urllib.request
from main_result import Result
from give_me_the_image import *
#from io import StringIO

#image_url2 = ['http://www.remod.co.kr/web/product/medium/201810/455d656ef6974715f5bd27e3e061612b.jpg', 'http://www.remod.co.kr/web/product/medium/201810/fec8fad5fcac1d6d88f2cdc81eec0eea.jpg', 'http://www.remod.co.kr/web/product/medium/201810/5f4a2ce986119e4706af592b79b474cd.jpg', 'http://www.remod.co.kr/web/product/medium/201810/9f4a992dfe9747c8db95bfee10331b3d.jpg', 'http://www.remod.co.kr/web/product/medium/201702/3882_shop1_509894.jpg', 'http://www.remod.co.kr/web/product/medium/201702/3881_shop1_764247.jpg', 'http://www.remod.co.kr/web/product/medium/201702/3878_shop1_700913.jpg', 'http://www.remod.co.kr/web/product/medium/201702/3877_shop1_682037.jpg', 'http://www.remod.co.kr/web/product/medium/201702/3148_shop1_263204.jpg', 'http://www.remod.co.kr/web/product/medium/201808/1c2ff18abf847302e03362613bba2d30.jpg', 'http://www.remod.co.kr/web/product/medium/201808/7eb3b60d13c0481051de26df8889a84f.jpg', 'http://www.remod.co.kr/web/product/medium/201806/4314_shop1_15301962550173.jpg', 'http://www.remod.co.kr/web/product/medium/201806/4311_shop1_15286871717718.jpg', 'http://www.remod.co.kr/web/product/medium/201712/3123_shop1_395408.jpg', 'http://www.remod.co.kr/web/product/medium/201702/3806_shop1_646868.jpg', 'http://www.remod.co.kr/web/product/medium/201708/3917_shop1_881738.jpg', 'http://www.remod.co.kr/web/product/medium/201712/3991_shop1_403719.jpg', 'http://www.remod.co.kr/web/product/medium/201712/3966_shop1_135440.jpg', 'http://www.remod.co.kr/web/product/medium/201704/3728_shop1_183221.jpg', 'http://www.remod.co.kr/web/product/medium/201712/4012_shop1_668390.jpg', 'http://www.remod.co.kr/web/product/medium/201712/4011_shop1_552284.jpg', 'http://www.remod.co.kr/web/product/medium/201712/4010_shop1_959866.jpg', 'http://www.remod.co.kr/web/product/medium/201712/3149_shop1_575120.jpg', 'http://www.remod.co.kr/web/product/medium/201703/3825_shop1_518816.jpg', 'http://www.remod.co.kr/web/product/medium/201710/3962_shop1_653377.jpg', 'http://www.remod.co.kr/web/product/medium/201703/3018_shop1_424612.jpg', 'http://www.remod.co.kr/web/product/medium/201703/3019_shop1_427435.jpg', 'http://www.remod.co.kr/web/product/medium/201712/4016_shop1_434561.jpg', 'http://www.remod.co.kr/web/product/medium/201703/3800_shop1_710083.jpg', 'http://www.remod.co.kr/web/product/medium/201712/4005_shop1_684263.jpg']
#image_url = ['http://img.sivillage.com/files/product/01/P0000/21/52/90/01P0000215290_260.jpg', 'http://img.sivillage.com/files/product/01/P0000/18/27/68/01P0000182768_260.jpg', 'http://img.sivillage.com/files/product/01/P0000/18/27/70/01P0000182770_260.jpg', 'http://img.sivillage.com/files/product/01/P0000/21/52/89/01P0000215289_260.jpg', 'http://img.sivillage.com/files/product/01/P0000/01/91/34/01P0000019134_260.jpg', 'http://img.sivillage.com/files/product/01/P0000/19/75/56/01P0000197556_260.jpg', 'http://img.sivillage.com/files/product/01/P0000/19/75/57/01P0000197557_260.jpg', 'http://img.sivillage.com/files/product/01/P0000/21/52/92/01P0000215292_260.jpg', 'http://img.sivillage.com/files/product/01/P0000/02/07/24/01P0000020724_260.jpg', 'http://img.sivillage.com/files/product/01/P0000/19/75/58/01P0000197558_260.jpg', 'http://img.sivillage.com/files/product/01/P0000/21/52/91/01P0000215291_260.jpg']

class Images(object):

    def give_image(self, url, n):
        images = url
        data = urllib.request.urlopen(images).read()
        image = QImage()
        image.loadFromData(data)
        lbl = QPushButton(self.scrollAreaWidgetContents)
        lbl.setGeometry(30,30+350*n,260,200)
        lbl.clicked.connect(lambda:self.click(n))
        lbli = QIcon()
        lbliii = QPixmap(image)
        lbliii.scaled(300,300,Qt.KeepAspectRatio)
        lbli.addPixmap(lbliii)
        lblii = lbl.setIcon(lbli)
        lblii = lbl.setIconSize(QSize(300,300))
        return lblii

    def click(self,n):
        self.object.append(n)
        self.selected_url.append(self.image_url[n])


    def show_images(self, OtherWindow, room, msg, theme):
        self.room = room
        self.msg = msg
        self.theme = theme
        self.object = []
        self.selected_url = []
        self.image_url = get_theme_image(self.theme)
        
        OtherWindow.resize(360,600)
        OtherWindow.move(1000,200)
        self.centralwidget = QWidget(OtherWindow)

        layout = QVBoxLayout(self.centralwidget)

        self.scrollArea = QScrollArea(self.centralwidget)
        layout.addWidget(self.scrollArea)

        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setGeometry(QRect(0,0,300,90+350*len(self.image_url)))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        layout = QHBoxLayout(self.scrollAreaWidgetContents)

        for i in range(len(self.image_url)):
            image = self.give_image(self.image_url[i],i)
            layout.addWidget(image)

        self.next = QPushButton(self.scrollAreaWidgetContents)
        self.next.setGeometry(QRect(110,10+350*len(self.image_url),100,50))
        font = QFont()
        font.setBold(True)
        self.next.setFont(font)
        self.next.setObjectName('qwerty')
        self.next.clicked.connect(self.NextWindow)
        
        OtherWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(OtherWindow)
        self.retranslateUi(OtherWindow)
        QMetaObject.connectSlotsByName(OtherWindow)

    def NextWindow(self):
        print('hi1')
        self.window = QMainWindow()
        print('hi2')
        self.ui = Result()
        print('hi3')
        print(self.object)
        print(self.selected_url)
        self.ui.show_result(self.window, self.room, self.msg, self.theme, self.object, self.selected_url)
        print('hi4')
        self.window.show()
        print('hi5')

    def retranslateUi(self, OtherWindow):
        translate = QCoreApplication.translate
        OtherWindow.setWindowTitle(translate("OtherWindow", "불판 4"))
        self.next.setText(translate("OtherWindow",'조회'))
        #self.next.setText(translate("OtherWindow",'완료'))
                           
if __name__ == '__main__':
    app = QApplication(sys.argv)
    OtherWindow = QMainWindow()
    ui = Images()
    ui.show_images(OtherWindow,'test 방','test 가구','test 테마')
    OtherWindow.show()
    sys.exit(app.exec_())
    
