import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import urllib.request
from ikea_function import *
#from jaju_func import *
#from remod_func import *
#from io import StringIO

#site = ['http://living.sivillage.com/jaju/product/productDetail?productNo=01P0000215290&dspCatNo=010000041353', 'http://living.sivillage.com/jaju/product/productDetail?productNo=01P0000182768&dspCatNo=010000041353', 'http://living.sivillage.com/jaju/product/productDetail?productNo=01P0000182770&dspCatNo=010000041353', 'http://living.sivillage.com/jaju/product/productDetail?productNo=01P0000215289&dspCatNo=010000041353', 'http://living.sivillage.com/jaju/product/productDetail?productNo=01P0000019134&dspCatNo=010000041353', 'http://living.sivillage.com/jaju/product/productDetail?productNo=01P0000197556&dspCatNo=010000041353', 'http://living.sivillage.com/jaju/product/productDetail?productNo=01P0000197557&dspCatNo=010000041353', 'http://living.sivillage.com/jaju/product/productDetail?productNo=01P0000215292&dspCatNo=010000041353', 'http://living.sivillage.com/jaju/product/productDetail?productNo=01P0000020724&dspCatNo=010000041353', 'http://living.sivillage.com/jaju/product/productDetail?productNo=01P0000197558&dspCatNo=010000041353', 'http://living.sivillage.com/jaju/product/productDetail?productNo=01P0000215291&dspCatNo=010000041353']
#name = ['SÖDERHAMN 쇠데르함', 'FÄRLÖV 펠뢰브', 'SÖDERHAMN 쇠데르함', 'EKTORP 엑토르프', 'FLOTTEBO 플로테보', 'KLIPPAN 클리판', 'FRIHETEN 프리헤텐', 'LIDHULT 리드훌트', 'VIMLE 빔레']
#price = ['570,000', '899,000', '700,000', '349,000', '689,000', '299,000', '549,000', '269,000', '809,000']
#image_url = ['https://www.ikea.com/kr/ko/images/products/soderhamn-soedeleuham-in-yongsegsyeon-pingkeu__0409691_PE583233_S4.JPG', 'https://www.ikea.com/kr/ko/images/products/farlov-pelloebeu-in-yongsopa-hwaiteu__0479740_PE619080_S4.JPG', 'https://www.ikea.com/kr/ko/images/products/soderhamn-soedeleuham-in-yongsopa-pingkeu__0409688_PE583232_S4.JPG', 'https://www.ikea.com/kr/ko/images/products/ektorp-egtoleupeu-in-yongsopa-beiji__0386580_PE559161_S4.JPG', 'https://www.ikea.com/kr/ko/images/products/flottebo-peullotebo-sopabedeu-bojoteibeul-beiji__0540473_PE652970_S4.JPG', 'https://www.ikea.com/kr/ko/images/products/klippan-keullipan-in-yongsopa-beulaun__0562968_PE663658_S4.JPG', 'https://www.ikea.com/kr/ko/images/products/friheten-peuliheten-in-yongsopabedeu-beiji__0325767_PE523058_S4.JPG', 'https://www.ikea.com/kr/ko/images/products/lidhult-lideuhulteu-in-yongsegsyeon-beulaun__0660819_PE711216_S4.JPG', 'https://www.ikea.com/kr/ko/images/products/vimle-bimle-in-yongsopa-beiji__0514357_PE639443_S4.JPG']
#driver = 0
#phantomjs_path = '/Users/tripl/Desktop/phantomjs-2.1.1-windows'

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
        lbl.setGeometry(30,30+350*n,500,300)
        lbli = QPixmap(image)
        lbli.scaled(500,300,Qt.IgnoreAspectRatio)
        lblii = lbl.setPixmap(lbli)
        print(type(lblii))
        return lblii

    def give_name(self, n):
        naame = QLabel(self.scrollAreaWidgetContents)
        naame.setGeometry(550,110+350*n,300,70)
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        naame.setFont(font)
        naame.setObjectName('penguin')
        naaaame = naame.setText(QCoreApplication.translate("Result",self.name[n]))
        return naaaame

    def give_price(self, n):
        pricee = QLabel(self.scrollAreaWidgetContents)
        pricee.setGeometry(QRect(550,160+350*(n),370,70))
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        pricee.setFont(font)
        pricee.setObjectName('haribo')
        priceee = pricee.setText(QCoreApplication.translate("Result",self.price[n]))
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

        self.name = name
        self.price = price
        self.image_url = image_url
        print('hi6')

        # jaju_PhantomJS(driver, phantomjs_path)
        for i in self.msg :
            print(i)
            if i == '의자' :
                a,b,c,d = ikea_chair(self.room, pic_chart)
                self.name += a
                self.price += b
                self.image_url += d
                """
                a,b,c,d = remod_chair(self.room, pic_chart)
                self.name += a
                self.price += b
                self.image_url +=d

                a,b,c,d = jaju_chair(self.room, pic_chart)
                self.name += a
                self.price += b
                self.image_url +=d
                """
            if i == '책상' :
                a,b,c,d = ikea_table(self.room, pic_chart)
                self.name += a
                self.price += b
                self.image_url += d
                """
                a,b,c,d = remod_table(self.room, pic_chart)
                self.name += a
                self.price += b
                self.image_url +=d

                a,b,c,d = jaju_table(self.room, pic_chart)
                self.name += a
                self.price += b
                self.image_url +=d
                """
            if i == '옷장' :
                a,b,c,d = ikea_closet(self.room, pic_chart)
                self.name += a
                self.price += b
                self.image_url += d
                """
                a,b,c,d = remod_closet(self.room, pic_chart)
                self.name += a
                self.price += b
                self.image_url +=d
                """
            if i == '소파' :
                print('hi10')
                a,b,c,d = ikea_sofa(self.room, pic_chart)
                self.name += a
                self.price += b
                self.image_url += d
                """
                a,b,c,d = remod_sofa(self.room, pic_chart)
                self.name += a
                self.price += b
                self.image_url +=d
                """
                print('hi11')


        print('hi1')
        OtherWindow.resize(800,600)
        OtherWindow.move(1000,300)
        self.centralwidget = QWidget(OtherWindow)
        print('hi1.5')

        layout = QVBoxLayout(self.centralwidget)
        print('hi2')
        
        self.scrollArea = QScrollArea(self.centralwidget)
        layout.addWidget(self.scrollArea)
        print('hi3')
        
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setGeometry(QRect(0,0,700,30+350*len(self.name)))
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
            image = self.give_image(i,position)
            #image.scaled(600,600, QtCore.Qt.IgnoreAspectRatio)
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
        #self.next.setText(translate("OtherWindow",'완료'))
                           
if __name__ == '__main__':
    app = QApplication(sys.argv)
    OtherWindow = QMainWindow()
    ui = Result()
    ui.show_result(OtherWindow,'원룸', ['소파'], '모던', [1], ['http://img.sivillage.com/files/product/01/P0000/21/52/90/01P0000215290_260.jpg'])
    OtherWindow.show()
    sys.exit(app.exec_())
    
