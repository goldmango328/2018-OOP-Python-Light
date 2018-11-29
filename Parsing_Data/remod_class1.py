# remod class
# 실행하기 전, selenium 설치와 phantomjs 설치가 되어있어야 함

from image_color_cluster3 import *
import bs4
from selenium import webdriver

furni = {'chair':['139','140','141','143'],'sofa':['138'],'cutton':[],'table':['134','135','136','137'],'dresser':['175']}

def get_html(url):
    global driver
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
        product_url = 'http://www.remod.co.kr'+url
        sub_url.append(product_url)

    sub_url = list(set(sub_url))
    return sub_url

class furni:
    def __init__(self, in_url):
        self.html= get_html(in_url)
        self.soup = bs4.BeautifulSoup(self.html, 'html.parser')

        self.color = []
        self.image = []
        self.name = []
        self.price = []
        self.size = []
        self.url = get_product_url(self.soup)
        
        self.get_data()

    def get_img(self, sub):
        img = sub.select('div.box a img')
        for i in img:
            img_in = i.get('src')
            self.image.append('http:'+img_in)

        # print(self.image)
        return self.image

    def get_name(self, sub):
        name = sub.select('div.box a span')
        for i in name:
            name_in = i.getText().strip()
            self.name.append(name_in)
        # print(self.name)
        return self.name

    def get_price(self, sub):
        price = sub.select('div.box ul.xans-element-.xans-product.xans-product-listitem li.xans-record- span')
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
            
        # print(self.price)
        return self.price

    def get_size(self, data): # 여기에 source가 들어가지를 않음.. empty list
        sub_url = get_product_url(data)
        for url in sub_url:
            sub_html = get_html(url)
            sub_soup = bs4.BeautifulSoup(sub_html,'html.parser')
            # try 1:
            source = sub_soup.select('div.xans-element-.xans-product.xans-product-additional > div#prdDetail > div.cont p')
            source = [x.getText().strip()[6:] for x in source if '사이즈' in x.getText()]
            if len(source)>1:
                source = source[0]

            if len(source) == 0:
                # try 2:
                source = sub_soup.select('div.xans-element-.xans-product.xans-product-detaildesign > table > tbody tr.xans-record- td span')
                source = [x.getText() for x in source if x.getText()[0] == 'w']
                if len(source)>1:
                    source = source[0]
                    
                if len(source) == 0: # 더이상 처리하기 힘든 경우 None으로 표기
                    source = 'None'

            if source == 'None':
                self.size.append(source)
                continue
            
            try:
                source = str(*source)
            except TypeError:
                source = source
                
            source = source.split('(')[0]
            for x in [' ','w','d','h','mm'] :
                source = source.replace(x,'')
            source = source.split('x')

            for i in range(len(source)):
                if '~' in source[i]:
                    source[i] = source[i].split('~')[1]
            try:
                source = [ int(x)/10 for x in source ] # mm단위를 cm단위로 통일화
            except ValueError:
                source = 'None'
                
            self.size.append(source)

        # print(self.size)
        return self.size

    def get_color(self):
        for image_url in self.image:
            image = URLtoImage(image_url)
            image_info = image_color_cluster(image)
            self.color.append(list(image_info.keys())[0])
        # print(self.color)
        return self.color
        
    def get_data(self):
        self.get_name(self.soup)
        self.get_price(self.soup)
        self.get_img(self.soup)
        self.get_size(self.soup)
        self.url.extend(get_product_url(self.soup))

    def changeURL(self,new_url):
        self.html= get_html(new_url)
        self.soup = bs4.BeautifulSoup(self.html, 'html.parser')
        self.get_data()
        
    def print_all(self):
        self.get_color()
        return self.url, self.name, self.price, self.image, self.size, self.color

if __name__ == "__main__":
    # PhantomJS 가 설치되어있는 경로
    PhantomJS_path = '/Users/지명금/Desktop/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs'
    driver = webdriver.PhantomJS(PhantomJS_path)
    driver.implicitly_wait(1)
    
    url = 'http://www.remod.co.kr/product/list.html?cate_no='

    # 의자 : test success :: 199개
    
    CHAIR = furni(url+'139&page=1')
    CHAIR.changeURL(url+'139$page=2')
    CHAIR.changeURL(url+'139&page=3')
    for i in range(1,4):
        CHAIR.changeURL(url+'140%page='+str(i))
    CHAIR.changeURL(url+'141&page=1')
    CHAIR.changeURL(url+'143&page=1')
    ch_url, ch_name, ch_price, ch_img, ch_size, ch_color = CHAIR.print_all()
    # print('CHAIR'+str(len(ch_url)))

    # 옷장
    DRESSER = furni(url+'175&page=1')
    dr_url, dr_name, dr_price, dr_img, dr_size, dr_color = DRESSER.print_all()
    # print(len(dr_url),dr_url)
    # print(len(dr_name),dr_name)
    # print(len(dr_price),dr_price)
    # print(len(dr_img),dr_img)
    # print(len(dr_color),dr_color)
    print("DRESSER "+str(len(dr_url)))
          
    # 소파
    SOFA = furni(url+'138&page=1')
    SOFA.changeURL(url + '138&page=2')
    SOFA.changeURL(url + '138&page=3')
    sf_url, sf_name, sf_price, sf_img, sf_size, sf_color = SOFA.print_all()
    print('SOFA')

    # 테이블 '134','135','136','137'
    TABLE = furni(url+'134&page=1')
    TABLE.changeURL(url + '134&page=2')
    TABLE.changeURL(url + '134&page=3')
    TABLE.changeURL(url + '135&page=1')
    TABLE.changeURL(url + '136&page=1')
    TABLE.changeURL(url + '136&page=2')
    TABLE.changeURL(url + '137&page=1')
    TABLE.changeURL(url + '137&page=2')
    tb_url, tb_name, tb_price, tb_img, tb_size, tb_color = TABLE.print_all()
    print('TABLE')
    
    # 
    # print(len(ch_url), ch_url)
    # print(len(ch_name), ch_name)
    # print(len(ch_price), ch_price)
    # print(len(ch_img), ch_img)
    # print(len(ch_size), ch_size)
    # print(len(ch_color), ch_color)
    
    
