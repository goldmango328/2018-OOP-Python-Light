# jaju class
# 실행하기 전, selenium 설치와 phantomjs 설치가 되어있어야 함

# selenium 설치 = pip install selenium
# phantomjs 설치 = http://phantomjs.org/download.html에서 압축파일 다운로드 -> 압축해
from color_similarity2 import *
from image_color_cluster3 import *
import bs4
from selenium import webdriver
import re

url = 'http://www.sivillage.com/jaju/dispctg/initDispCtg.siv?disp_ctg_no=010000041353&outlet_yn=N&jajuYn=Y'

def get_html(url):
    # PhantomJS 가 설치되어있는 경로
    global driver
    
    driver.get(url)
    html = driver.page_source
    return html 

def get_suburl(data):
    url = data.select('div.item a')
    sub_url: List[Union[str, Any]] = []

    # 변경사항(1): sub_url을 담고있는 형식이 달라져서 과정을 바꿈
    for i in url:
        sub_dict = {}
        sub = i.get('onclick').replace('overpass.tracking.link(','')
        for x in "{} )';":
            sub = sub.replace(x,'')
        sub = re.split('[: ,]',sub)

        flag,key,ele= 0,0,0
        for x in sub:
            if flag == 0:
                key = x
            elif flag == 1:
                ele = x
                
            flag +=1
            
            if flag==2:
                sub_dict[key] = ele
                flag = 0

        product_url = 'http://www.sivillage.com/jaju/goods/initDetailJajuGoods.siv?'
        for x in ['goods_no','sale_shop_divi_cd','sale_shop_no','tr_yn','conts_form_cd','conts_dist_no','rel_no','rel_divi_cd','disp_ctg_no']:
            product_url += '&'+x+'='+sub_dict[x]
        # print(product_url)
        sub_url.append(product_url)

    print(len(sub_url))
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
        name = soup.select('div.gd_name')
        name_in = name[0].getText().strip() # 일부 제품에서 이름을 못 가져옴 : 이지 철재 폴딩 스툴_브라운
        print(name_in)
        if '스툴' in name_in:
            self.name.append(name_in)
            return True,name_in
        else :
            return False,'None'

    def get_img(self, soup):
        img = soup.select('div#zoom_img img')
        img_in = img[0].get('src')
        # print(img_in)
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
        price = soup.select('div.gd_prc dl.g_prc dd')
        price_in = price[0].getText().strip()
        # print(price_in)
        self.price.append(price_in)

    def get_size(self, soup): # 시간 잡아먹는 주범
        source = soup.select('div.gd_info div#divGoodsClssGuideMid table tbody tr')
        source = [ x.find('td').getText().upper() for x in source if x.find('th').getText() == '크기']
        # print(source) # 일부 제품에서 soup를 가져오지 못하는 error발생 : 목재 선반형 스툴 / 이지 철재 폴딩 스툴_베이지
        try :
            text = source[0]
        except IndexError:
            print('ERROR',source)
        
        for x in ['x','X','CM','cm','(',')','높이','h','d','w','W','D','H']:
            text = text.replace(x,' ')
        text = text.split(' ')
        cnt = text.count('')
        for i in range(cnt):
            text.remove('')
        # print(text)
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
                # print("YES", end=' | ')
                self.get_price(soup)
                self.get_size(soup)
            else :
                # print("NOPE")
                self.url.remove(url)
                self.name.remove(name)

        return self.url, self.name, self.price, self.image, self.size, self.color

class table(chair):
    def get_name(self, soup):
        name = soup.select('div.gd_name')
        name_in = name[0].getText().strip()
        if '상' in name_in or '테이블' in name_in:
            self.name.append(name_in)
            return True,name_in
        else :
            return False,'None'

if __name__ == "__main__":
    PhantomJS_path = '/Users/지명금/Desktop/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs'
    driver = webdriver.PhantomJS(PhantomJS_path)
    driver.implicitly_wait(1)

    # 사진 색상 차트를 미리 만들어놔야 함
    # chart :: 색상 차트를 저장해둔 list
    
    chart = ['#828490','#b5bfc6','#bdcdda']

    # 파싱과정에서 직접 url 과 chart를 넘겨줘야 함
    # url :: jaju main page
    CHAIR = chair(url,chart)
    TABLE = table(url,chart)
    
    ch_url, ch_name, ch_price, ch_img, ch_size, ch_color = CHAIR.print_all()
    print(len(ch_name), ch_name)
    print(len(ch_price), ch_price)
    print(len(ch_img), ch_img)
    print(len(ch_size), ch_size)
    print(len(ch_color),ch_color)
    print("ch_total",len(ch_name))
    
    tb_url, tb_name, tb_price, tb_img, tb_size, tb_color = TABLE.print_all()
    print(len(tb_name), tb_name)
    print(len(tb_price), tb_price)
    print(len(tb_img), tb_img)
    print(len(tb_size), tb_size)
    print(len(tb_color),tb_color)
    print("tb_total",len(tb_name))
    
