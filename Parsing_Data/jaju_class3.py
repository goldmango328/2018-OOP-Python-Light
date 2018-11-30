# jaju class
# 실행하기 전, selenium 설치와 phantomjs 설치가 되어있어야 함

# selenium 설치 = pip install selenium
# phantomjs 설치 = http://phantomjs.org/download.html에서 압축파일 다운로드 -> 압축해
from color_similarity2 import *
from image_color_cluster3 import *
import bs4
from selenium import webdriver
    
def get_html(url):
    # PhantomJS 가 설치되어있는 경로
    global driver
    
    driver.get(url)
    html = driver.page_source
    return html 

def get_suburl(data):
    url = data.select('div.item a')
    sub_url: List[Union[str, Any]] = []
    for i in url:
        product_url = 'http://living.sivillage.com' + i.get('href')
        sub_url.append(product_url)

    return sub_url

class chair:
    def __init__(self, in_url,chart):
        self.html= get_html(in_url)
        self.soup = bs4.BeautifulSoup(self.html, 'html.parser')
        self.chart = chart
        
        self.color = []
        self.image = []
        self.name = []
        self.price = []
        self.size = []
        self.url = []

    def get_name(self, soup):
        name = soup.select('div.pull-left.detail-info div.header div.title.mg-t10')
        name_in = (name[0]).getText().strip()
        if '스툴' in name_in:
            self.name.append(name_in)
            return True,name_in
        else :
            return False,'None'
        
    def get_img(self, soup):
        img = soup.select('div.j-prd-view div.img-box div.owl-stage-outer img')
        img_in = img[0].get('src')
        self.image.append(img_in)
        return img_in

    def get_color(self, image_url):
        image = URLtoImage(image_url)
        image_info = image_color_cluster(image)
        im_color = list(image_info.keys())[0]
        if isColorSimilar(im_color, self.chart):
            self.color.append(im_color)
            return True
        else :
            # 이전에 뽑았던 것들에서 삭제
            self.image.remove(image_url)
            return False
            
    def get_price(self, soup):
        price = soup.select('div.pull-left.detail-info div.body.mg-t20 div.j-detail_price span')
        price_in = price[0].getText().strip()
        self.price.append(price_in)

    def get_size(self, soup): # 시간 잡아먹는 주범
        source = soup.select('div.j-grid table.table tbody tr')
        source = [ x.find('td').getText().upper() for x in source if x.find('th').getText() == '크기']
        text = source[0]
        for x in ['x','X','CM','cm','(',')','높이','h','d','w','W','D','H']:
            text = text.replace(x,' ')
        text = text.split(' ')
        cnt = text.count('')
        for i in range(cnt):
            text.remove('')

        self.size.append(text)

    def print_all(self):
        self.url = get_suburl(self.soup)
        for url in self.url :
            html = get_html(url)
            soup = bs4.BeautifulSoup(html,'html.parser')

            flag,name = self.get_name(soup) # 이름을 먼저 받아와서 chair인지 table인지를 판단 idx에 삽입 & self.url에서 제외)
            if flag == False: # 의자가 아닌 경우
                self.url.remove(url)
                continue
            
            img = self.get_img(soup) # idx에 해당되는 img를 받아오고
            parse = self.get_color(img) # img의 색이 colorchart안에 있는지를 확인
            if parse == True:
                print("YES", end=' | ')
                self.get_price(soup)
                self.get_size(soup)
                print(name)
            else :
                print("NOPE")
                self.url.remove(url)
                self.name.remove(name)

        return self.url, self.name, self.price, self.image, self.size, self.color

class table(chair):
    def get_name(self, soup):
        name = soup.select('div.pull-left.detail-info div.header div.title.mg-t10')
        name_in = (name[0]).getText().strip()
        if '상' in name_in or '테이블' in name_in:
            self.name.append(name_in)
            return True,name_in
        else :
            return False,'None'

if __name__ == "__main__":
    PhantomJS_path = '/Users/지명금/Desktop/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs'
    driver = webdriver.PhantomJS(PhantomJS_path)
    driver.implicitly_wait(1)

    chart=['#828490','#b5bfc6','#bdcdda']
    url = 'http://living.sivillage.com/jaju/display/displayCategory?dspCatNo=010000041353&upDspCatNo=010000000007&chnSct=P'
    CHAIR = chair(url,chart)
    TABLE = table(url,chart)
    ch_url, ch_name, ch_price, ch_img, ch_size, ch_color = CHAIR.print_all()
    # print(len(ch_name), len(ch_price), len(ch_img), len(ch_size), len(ch_color))
    tb_url, tb_name, tb_price, tb_img, tb_size, tb_color = TABLE.print_all()
