# remod class
# 실행하기 전, selenium 설치와 phantomjs 설치가 되어있어야 함

# size 데이터를 못 가져오면 None 으로 저장 

from color_similarity2 import *
from image_color_cluster3 import *
import bs4
from selenium import webdriver

furn = {'chair':['139','140','141','143'],'sofa':['138'],'cutton':[],'table':['134','135','136','137'],'dresser':['175']}

def get_html(url):
    global driver
    driver.get(url)
   
    html = driver.page_source
    return html 

def get_suburl(data):
    sub_url = []
    url_lst = data.select('div.xans-element-.xans-product.xans-product-listnormal ul.prdList.column3 li a')
    for url in url_lst:
        url = url.get('href')
        product_url = 'http://www.remod.co.kr'+url
        sub_url.append(product_url)

    sub_url = list(set(sub_url))
    return sub_url

class furni:
    global size
    def __init__(self, in_url, chart):
        self.html= get_html(in_url)
        self.soup = bs4.BeautifulSoup(self.html, 'html.parser')
        self.chart =  chart

        self.url = []
        self.color = []
        self.image = []
        self.name = []
        self.price = []
        self.size = []
    
    def get_img(self, soup):
        img = soup.select('div.keyImg div.thumbnail a img')
        img_in = 'http:'+img[0].get('src')
        self.image.append(img_in)
        return img_in

    def get_color(self,image_url):
        image = URLtoImage(image_url)
        image_info = image_color_cluster(image)
        im_color = list(image_info.keys())[0]
        if isColorSimilar(im_color, self.chart):
            # print(im_color)
            self.color.append(im_color)
            return True
        else :
            # 이전에 뽑았던 것들에서 삭제
            self.image.remove(image_url)
            return False

    def get_price(self, sub):
        price = sub.select('div.xans-element-.xans-product.xans-product-detaildesign tbody tr.xans-record- td span')
        for i in price:
            price_in = i.getText().strip()
            flag = False
            for x in ['','판매가','△ Colors']:
                if x == price_in:
                    flag = True
                    break
            if flag == True:
                continue
            else :
                self.price.append(price_in)
            
        print(self.price)
        return self.price

    def get_size(self, soup): # 시간 잡아먹는 주범
        source = soup.select('div.j-grid table.table tbody tr')
        source = [ x.find('td').getText().upper() for x in source if x.find('th').getText() == '크기']
        try :
            text = source[0]
        except IndexError:
            return 
        for x in ['x','X','CM','cm','(',')','높이','h','d','w','W','D','H']:
            text = text.replace(x,' ')
        text = text.split(' ')
        cnt = text.count('')
        for i in range(cnt):
            text.remove('')

        if size == '원룸':
            if text[0] > 250 or text[1]>250 or text[2]>250:
                return False
            else :
                self.size.append(text)
                return True
        
    def get_name(self, sub):
        name = sub.select('div.box a span')
        name_in = name[0].getText().strip()
        self.name.append(name_in)
        # print(name_in)
    
    def get_data(self):
        sub_url = get_suburl(self.soup)
        cnt = 0
        for url in sub_url:
            # error가 발생하는 url을 제외
            print("CNT:",cnt,end=' | ')
            if url == 'http://www.remod.co.kr/web/product/medium/201712/3964_shop1_974172.jpg':
                continue
            if cnt == 1:
                return
            
            html = get_html(url)
            soup = bs4.BeautifulSoup(html, 'html.parser')

            self.url.append(url)
            img = self.get_img(soup)
            print(img,end=' | ')
            parse = self.get_color(img)

            if parse == True:
                if self.get_size(soup) == True:
                    print("YES", end= ' | ')
                    name = self.get_name(soup)
                    self.get_price(soup)
                    print(name)
                    cnt += 1
                else :
                    print("NOPE")
                    self.img.remove(img)
                    self.color.remove(parse)
            else :
                print("NOPE")
                self.url.remove(url)
            

    def changeURL(self,new_url):
        self.html= get_html(new_url)
        self.soup = bs4.BeautifulSoup(self.html, 'html.parser')
        self.get_data()
        
    def print_all(self):
        self.get_data()
        return self.url, self.name, self.price, self.image, self.size, self.color

if __name__ == "__main__":
    # PhantomJS 가 설치되어있는 경로
    PhantomJS_path = '/Users/지명금/Desktop/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs'
    driver = webdriver.PhantomJS(PhantomJS_path)
    driver.implicitly_wait(1)
    
    url = 'http://www.remod.co.kr/product/list.html?cate_no='
    size = '원룸'
    chart = ['#808080','#161c1e']
    
    # 의자 : test success(단일) :: 199개 -> 20개
    
    CHAIR = furni(url+'139&page=1',chart) # 하나당 1개씩만
    CHAIR.changeURL(url+'139$page=2')
    CHAIR.changeURL(url+'139&page=3')
    for i in range(1,4):
        CHAIR.changeURL(url+'140%page='+str(i))
    CHAIR.changeURL(url+'141&page=1')
    CHAIR.changeURL(url+'143&page=1')
    ch_url, ch_name, ch_price, ch_img, ch_size, ch_color = CHAIR.print_all()
    print('[ CHAIR ] '+str(len(ch_url)))

    
    # 옷장 : test success(단일) :: 6개 -> 6개
    DRESSER = furni(url+'175&page=1',chart)
    dr_url, dr_name, dr_price, dr_img, dr_size, dr_color = DRESSER.print_all()
    print("[ DRESSER ] "+str(len(dr_url)))

    # 소파 : test fail(단일) 
    SOFA = furni(url+'138&page=1',chart)
    SOFA.changeURL(url + '138&page=2')
    SOFA.changeURL(url + '138&page=3')
    sf_url, sf_name, sf_price, sf_img, sf_size, sf_color = SOFA.print_all()
    print('[ SOFA ] ' + str(len(sf_url)))
    
    # 테이블 : test success(단일) :: 173개 -> 20개
    TABLE = furni(url+'134&page=1',chart)
    TABLE.changeURL(url + '134&page=2')
    TABLE.changeURL(url + '134&page=3')
    TABLE.changeURL(url + '135&page=1')
    TABLE.changeURL(url + '136&page=1')
    TABLE.changeURL(url + '136&page=2')
    TABLE.changeURL(url + '137&page=1')
    TABLE.changeURL(url + '137&page=2')
    tb_url, tb_name, tb_price, tb_img, tb_size, tb_color = TABLE.print_all()
    print('[ TABLE ] ' + str(len(tb_url)))
