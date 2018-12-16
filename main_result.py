import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import urllib.request
from ikea_function import *

# from io import StringIO

# site = ['http://living.sivillage.com/jaju/product/productDetail?productNo=01P0000215290&dspCatNo=010000041353', 'http://living.sivillage.com/jaju/product/productDetail?productNo=01P0000182768&dspCatNo=010000041353', 'http://living.sivillage.com/jaju/product/productDetail?productNo=01P0000182770&dspCatNo=010000041353', 'http://living.sivillage.com/jaju/product/productDetail?productNo=01P0000215289&dspCatNo=010000041353', 'http://living.sivillage.com/jaju/product/productDetail?productNo=01P0000019134&dspCatNo=010000041353', 'http://living.sivillage.com/jaju/product/productDetail?productNo=01P0000197556&dspCatNo=010000041353', 'http://living.sivillage.com/jaju/product/productDetail?productNo=01P0000197557&dspCatNo=010000041353', 'http://living.sivillage.com/jaju/product/productDetail?productNo=01P0000215292&dspCatNo=010000041353', 'http://living.sivillage.com/jaju/product/productDetail?productNo=01P0000020724&dspCatNo=010000041353', 'http://living.sivillage.com/jaju/product/productDetail?productNo=01P0000197558&dspCatNo=010000041353', 'http://living.sivillage.com/jaju/product/productDetail?productNo=01P0000215291&dspCatNo=010000041353']
# name = ['원형 수납 패브릭 스툴_그레이', '목재 선반형 스툴', '목재 선반형 바 스툴', '원형 수납 패브릭 스툴_민트', '크러쉬 스툴 26x21x39cm_베이지', '이지 철재 폴딩 스툴_베이지', '이지 철재 폴딩 스툴_그레이', '사각 접이식 수납 스툴_그레이', '크러쉬 스툴 28x21x22cm_다크브라운', '이지 철재 폴딩 스툴_브라운', '사각 접이식 수납 스툴_민트']
# price = ['59,900원', '59,900원', '79,900원', '59,900원', '13,900원', '9,900원', '9,900원', '19,900원', '7,900원', '9,900원', '19,900원']
# image_url = ['http://img.sivillage.com/files/product/01/P0000/21/52/90/01P0000215290_260.jpg', 'http://img.sivillage.com/files/product/01/P0000/18/27/68/01P0000182768_260.jpg', 'http://img.sivillage.com/files/product/01/P0000/18/27/70/01P0000182770_260.jpg', 'http://img.sivillage.com/files/product/01/P0000/21/52/89/01P0000215289_260.jpg', 'http://img.sivillage.com/files/product/01/P0000/01/91/34/01P0000019134_260.jpg', 'http://img.sivillage.com/files/product/01/P0000/19/75/56/01P0000197556_260.jpg', 'http://img.sivillage.com/files/product/01/P0000/19/75/57/01P0000197557_260.jpg', 'http://img.sivillage.com/files/product/01/P0000/21/52/92/01P0000215292_260.jpg', 'http://img.sivillage.com/files/product/01/P0000/02/07/24/01P0000020724_260.jpg', 'http://img.sivillage.com/files/product/01/P0000/19/75/58/01P0000197558_260.jpg', 'http://img.sivillage.com/files/product/01/P0000/21/52/91/01P0000215291_260.jpg']
phantomjs_path = '/Users/tripl/Desktop/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs'


def get_imagechart(image_lst):
    pic_chart = []

    for img_url in image_lst:
        image = URLtoImage(img_url)
        image_info = image_color_cluster(image)
        pic_chart.extend(list(image_info.keys()))

    return pic_chart


class Result(object):

    def give_image(self, url, n):
        images = url
        print(images)
        data = urllib.request.urlopen(images).read()
        image = QImage()
        image.loadFromData(data)
        lbl = QLabel(self.scrollAreaWidgetContents)
        lbl.setGeometry(30, 30 + 350 * n, 260, 300)
        lbli = QPixmap(image)
        lbli.scaled(260, 300, Qt.KeepAspectRatio)
        lblii = lbl.setPixmap(lbli)
        return lblii

    def give_name(self, n):
        naame = QLabel(self.scrollAreaWidgetContents)
        naame.setGeometry(QRect(320, 60 + 350 * n, 300, 70))
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        naame.setFont(font)
        naame.setObjectName('penguin')
        naaaame = naame.setText(QCoreApplication.translate("Result", self.name[n]))
        return naaaame

    def give_price(self, n):
        pricee = QLabel(self.scrollAreaWidgetContents)
        pricee.setGeometry(QRect(320, 110 + 350 * n, 300, 70))
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        pricee.setFont(font)
        pricee.setObjectName('haribo')
        priceee = pricee.setText(QCoreApplication.translate("Result", self.price[n]))
        return priceee

    '''
    def give_site(self, n):
        sitee = QLabel(self.scrollAreaWidgetContents)
        sitee.setGeometry(QRect(320,150+350*n,300,70))
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        sitee.setFont(font)
        sitee.setObjectName('popstar')
        sitee.openExternalLinks()
        urlLink = '<a href=\"'+site[n]+'">누...눌러봐..</a>'
        print(urlLink)
        siteee = sitee.setText(urlLink)
        return siteee
    '''

    def show_result(self, OtherWindow, room, msg, theme, ob, selected_url):
        self.room = room
        self.msg = msg
        self.theme = theme
        self.object = ob
        self.selected_url = selected_url
        print(self.msg)
        pic_chart = get_imagechart(self.selected_url)
        print('hi5')
        input_size = self.room

        self.name = []
        self.price = []
        self.image_url = []
        print('hi6')

        for i in self.msg:
            print(i)
            if i == '의자':
                a, b, c, d = ikea_chair(self.room, pic_chart)
                self.name += a
                self.price += b
                self.image_url += d
            if i == '책상':
                a, b, c, d = ikea_table(self.room, pic_chart)
                self.name += a
                self.price += b
                self.image_url += d
            if i == '옷장':
                a, b, c, d = ikea_closet(self.room, pic_chart)
                self.name += a
                self.price += b
                self.image_url += d
            if i == '소파':
                print('hi10')
                a, b, c, d = ikea_sofa(self.room, pic_chart)
                self.name += a
                self.price += b
                self.image_url += d
                print('hi11')

        print('hi1')
        OtherWindow.resize(600, 600)
        OtherWindow.move(1300, 200)
        self.centralwidget = QWidget(OtherWindow)
        print('hi1.5')

        layout = QVBoxLayout(self.centralwidget)
        print('hi2')

        self.scrollArea = QScrollArea(self.centralwidget)
        layout.addWidget(self.scrollArea)
        print('hi3')

        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 500, 30 + 350 * len(self.name)))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        layout = QHBoxLayout(self.scrollAreaWidgetContents)
        print('hi4')

        position = 0
        print('hi7')
        print(self.name)
        print(self.price)
        print(self.image_url)
        # self.selected_url = ['https://images.homify.com/c_fill,f_auto,h_700,q_auto/v1544070461/p/photo/image/2825640/%EC%9D%B8%EC%B2%9C_%EB%85%BC%ED%98%84_%ED%95%9C%ED%99%94_%EC%97%90%EC%BD%94_22.jpg']

        for i in self.image_url:
            image = self.give_image(i, position)
            # 이거 테스트로.. ㅠㅜ image.scaled(600,600, QtCore.Qt.IgnoreAspectRatio)
            layout.addWidget(image)
            naaame = self.give_name(position)
            layout.addWidget(naaame)
            priceeee = self.give_price(position)
            layout.addWidget(priceeee)
            position += 1

        print('hi8')

        OtherWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(OtherWindow)
        self.retranslateUi(OtherWindow)
        QMetaObject.connectSlotsByName(OtherWindow)

    def retranslateUi(self, OtherWindow):
        translate = QCoreApplication.translate
        OtherWindow.setWindowTitle(translate("OtherWindow", "result 불판"))
        # self.next.setText(translate("OtherWindow",'완료'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    OtherWindow = QMainWindow()
    ui = Result()
    ui.show_result(OtherWindow, '원룸', ['소파'], '모던', [1, 3, 5, 7, 9],
                   ['http://img.sivillage.com/files/product/01/P0000/21/52/90/01P0000215290_260.jpg',
                    'http://img.sivillage.com/files/product/01/P0000/18/27/68/01P0000182768_260.jpg',
                    'http://img.sivillage.com/files/product/01/P0000/18/27/70/01P0000182770_260.jpg',
                    'http://img.sivillage.com/files/product/01/P0000/21/52/89/01P0000215289_260.jpg',
                    'http://img.sivillage.com/files/product/01/P0000/01/91/34/01P0000019134_260.jpg',
                    'http://img.sivillage.com/files/product/01/P0000/19/75/56/01P0000197556_260.jpg',
                    'http://img.sivillage.com/files/product/01/P0000/19/75/57/01P0000197557_260.jpg',
                    'http://img.sivillage.com/files/product/01/P0000/21/52/92/01P0000215292_260.jpg',
                    'http://img.sivillage.com/files/product/01/P0000/02/07/24/01P0000020724_260.jpg',
                    'http://img.sivillage.com/files/product/01/P0000/19/75/58/01P0000197558_260.jpg',
                    'http://img.sivillage.com/files/product/01/P0000/21/52/91/01P0000215291_260.jpg'])
    OtherWindow.show()
    sys.exit(app.exec_())