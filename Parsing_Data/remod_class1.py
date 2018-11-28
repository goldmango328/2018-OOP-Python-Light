# remod class
# 실행하기 전, selenium 설치와 phantomjs 설치가 되어있어야 함

# 내일 아침에 확인해보기

from image_color_cluster3 import *
import bs4
from selenium import webdriver

furni = {'chair':['139','140','141','143'],'sofa':['138'],'cutton':[],'table':['134','135','136','137'],'dresser':['175']}

def get_html(url):
    # PhantomJS 가 설치되어있는 경로
    PhantomJS_path = '/Users/지명금/Desktop/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs'
    driver = webdriver.PhantomJS(PhantomJS_path)
    driver.implicitly_wait(1)
    
    driver.get(url)
    html = driver.page_source
    return html 

def get_suburl(url, key):
    sub_url = []
    
    for cate_no in furni[key]:
        cate_url = url+cate_no
        sub_url.append(cate_url)
        
    return sub_url

def get_product_url(data):
    sub_url = []
    url_lst = data.select('div.xans-element-.xans-product.xans-product-listnormal ul.prdList.column3 li a')
    for url in url_lst:
        url = url.get('href')
        product_url = 'https://www.remod.co.kr'+url
        sub_url.append(product_url)

    sub_url = list(set(sub_url))
    return sub_url

class lounge_chair:
    def __init__(self, in_url):
        self.html= get_html(in_url)
        self.soup = bs4.BeautifulSoup(self.html, 'html.parser')

        self.color = []
        self.image = []
        self.name = []
        self.price = []
        self.size = []

    def get_img(self, sub):
        img = sub.select('div.box a img')
        for i in img:
            img_in = i.get('src')
            self.image.append(img_in)

        print(self.image)
        return self.image

    def get_name(self, sub):
        name = sub.select('div.box a span p')
        for i in name:
            name_in = i.getText().strip()
            self.name.append(name_in)
            
        print(self.name)
        return self.name

    def get_price(self, sub):
        price = sub.select('div.box ul.xans-element-.xans-product.xans-product-listitem li.xans-record- span p')
        for i in price:
            price_in = i.getText().strip()
            self.price.append(price_in)

        print(self.price)
        return self.price

    def get_size(self, data): # 시간 잡아먹는 주범
        sub_url = get_product_url(data)
        for url in sub_url:
            sub_html = get_html(url)
            sub_soup = bs4.BeautifulSoup(sub_html,'html.parser')

            source = sub_soup.select('div.xans-element-.xans-product.xans-product-additional div.cont p span p')
            # 이후에 '사이즈' 로 시작하면 크기를 표현하고 있는 것
            source = [ x[7:] for x in source if x.getText().strip()[:3] == '사이즈']
            for text in source:
                for x in ['x','X','CM','cm','(',')','높이','h','d','w','W','D','H']:
                    text = text.replace(x,' ')
                text = text.split(' ')
                cnt = text.count('')
                for i in range(cnt):
                    text.remove('')
                
            self.size.append(text)

        print(self.size)
        return self.size

    def get_color(self):
        for image_url in self.image:
            image = URLtoImage(image_url)
            image_info = image_color_cluster(image)
            self.color.append(list(image_info.keys())[0])
            
        print(self.color)
        return self.color
            
    def print_all(self):
        self.get_name(self.soup)
        self.get_price(self.soup)
        self.get_img(self.soup)
        self.get_size(self.soup)
        self.get_color()
        return self.name, self.price, self.image, self.size, self.color

if __name__ == "__main__":
    url = 'http://www.remod.co.kr/product/list.html?cate_no='
    CHAIR1 = lounge_chair(url+'139&page=1')
    ch_name, ch_price, ch_img, ch_size, ch_color = CHAIR1.print_all()
    

