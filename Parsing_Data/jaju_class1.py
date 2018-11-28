# jaju class
# 실행하기 전, selenium 설치와 phantomjs 설치가 되어있어야 함

# selenium 설치 = pip install selenium
# phantomjs 설치 = http://phantomjs.org/download.html에서 압축파일 다운로드 -> 압축해제

from image_color_cluster3 import *
import bs4
from selenium import webdriver

def get_html(url):
    # PhantomJS 가 설치되어있는 경로
    PhantomJS_path = '/Users/지명금/Desktop/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs'
    driver = webdriver.PhantomJS(PhantomJS_path)
    driver.implicitly_wait(1)
    
    driver.get(url)
    html = driver.page_source
    return html 

def get_suburl(data):
    url = data.select('div.item a')
    sub_url = []
    for i in url:
        product_url = 'http://living.sivillage.com' + i.get('href')
        sub_url.append(product_url)

    return sub_url

class chair:
    def __init__(self, in_url):
        self.html= get_html(in_url)
        self.soup = bs4.BeautifulSoup(self.html, 'html.parser')

        self.idx = [] # 해당하는 상품의 파싱되는 순서를 담은 list
        self.color = []
        self.image = []
        self.name = []
        self.price = []
        self.size = []

    def get_img(self, sub):
        img = sub.select('div.img img')
        for i in img:
            img_in = i.get('src')
            self.image.append(img_in)
        
        self.image = [ self.image[i] for i in self.idx]
        return self.image

    def get_name(self, sub):
        idx = 0
        name = sub.select('div.subject.ellipsis_ext p')
        for i in name:
            name_in = i.getText().strip()
            if '스툴' in name_in:
                self.name.append(name_in)
                self.idx.append(idx)

            idx += 1
        return self.name

    def get_price(self, sub):
        price = sub.select('div.j-item_price span.normal')
        for i in price:
            price_in = i.getText().strip()
            self.price.append(price_in)

        self.price = [ self.price[i] for i in self.idx ]
        return self.price

    def get_size(self, data): # 시간 잡아먹는 주범
        sub_url = get_suburl(data)
        for url in sub_url:
            sub_html = get_html(url)
            sub_soup = bs4.BeautifulSoup(sub_html,'html.parser')

            source = sub_soup.select('div.j-grid table.table tbody tr')
            source = [ x.find('td').getText().upper() for x in source if x.find('th').getText() == '크기']
            for text in source:
                for x in ['x','X','CM','cm','(',')','높이','h','d','w','W','D','H']:
                    text = text.replace(x,' ')
                text = text.split(' ')
                cnt = text.count('')
                for i in range(cnt):
                    text.remove('')
                
            self.size.append(text)

        self.size = [ self.size[i] for i in self.idx ]
        return self.size

    def get_color(self):
        for image_url in self.image:
            image = URLtoImage(image_url)
            image_info = image_color_cluster(image)
            self.color.append(list(image_info.keys())[0])

        return self.color
            
    def print_all(self):
        self.get_name(self.soup)
        self.get_price(self.soup)
        self.get_img(self.soup)
        # print("SUCCESS#1")
        self.get_size(self.soup)
        # print("SUCCESS#2")
        self.get_color()
        # print("DONE")
        return self.name, self.price, self.image, self.size, self.color

class table(chair):
    def get_name(self, sub):
        idx = 0
        name = sub.select('div.subject.ellipsis_ext p')
        for i in name:
            name_in = i.getText().strip()
            if '상' in name_in or '테이블' in name_in:
                self.name.append(name_in)
                self.idx.append(idx)

            idx += 1

        return self.name

if __name__ == "__main__":
    url = 'http://living.sivillage.com/jaju/display/displayCategory?dspCatNo=010000041353&upDspCatNo=010000000007&chnSct=P'
    CHAIR = chair(url)
    TABLE = table(url)
    ch_name, ch_price, ch_img, ch_size, ch_color = CHAIR.print_all()
    # print(len(ch_name), len(ch_price), len(ch_img), len(ch_size), len(ch_color))
    tb_name, tb_price, tb_img, tb_size, tb_color = TABLE.print_all()   
