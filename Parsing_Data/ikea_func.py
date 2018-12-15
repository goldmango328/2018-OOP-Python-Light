import bs4
import requests
from color_similarity2 import *
from image_color_cluster3 import *


def get_html(url):
    """
    웹 사이트 주소를 입력 받아, html tag 를 읽어드려 반환한다.
    :param url: parsing target web url
    :return: html tag
    """
    response = requests.get(url)
    try:
        response.raise_for_status()
    except requests.HTTPError:
        return '제품 정보가 없습니다.'
    else:
        return response.text


def get_url(data):
    url_main = data.select('div.productLists div.gridRow div.threeColumn div.image a')
    url = []
    for i in url_main:
        url.append("https://www.ikea.com/" + i.get('href'))
    return url


class parsing_data:
    def __init__(self, in_url):
        self.html= get_html(in_url)
        self.data = bs4.BeautifulSoup(self.html, 'html.parser')
        self.image = []
        self.name = []
        self.price = []
        self.size = []
        self.color = []
        self.url = get_url(self.data)

    def get_img(self, sub):
        sub_main = sub.select('div.rightContent div.pipContainer div#leftMainContainer div.rightContentContainer img#productImg')
        sub_main = str(sub_main[0]).split(' ')
        for line in sub_main:
            if 'src' in line:
                line = line.replace('"', '')
                line = line.replace('src=', '')
                now_img = line
        return now_img

    def get_name(self, sub):
        name_now = sub.select('div.addList div.rightInfoDiv h1 span.productName')
        name_in = name_now[0].getText().strip()
        self.name.append(name_in)
        return self.name

    def get_price(self, sub):
        price_now = sub.select('div.addList div.rightInfoDiv div.priceContainer span.packagePrice')
        price_in = price_now[0].getText().strip()
        price_in = price_in.replace('₩\xa0','')
        self.price.append(price_in)
        return self.price

    def get_size(self, sub):
        size_now = sub.select('div#metric')
        size_in = size_now[0].getText().strip()
        size_in = size_in.split(' cm')
        if len(size_in) < 3:
            self.size.append('none size')
        else:
            a = int(size_in[0].split(': ')[1])
            b = int(size_in[1].split(': ')[1])
            c= int(size_in[2].split(': ')[1])
            print(a, b, c)
            if input_size == '원룸':
                if a>250 or b>250 or c>250:
                    self.size.append([a, b, c])
                    return False
                else:
                    self.size.append([a, b, c])
                    return True
            else:
                self.size.append([a, b, c])
                return True

    def get_color(self, image_url):
        image = URLtoImage(image_url)
        image_info = image_color_cluster(image)
        return list(image_info.keys())[0]

    def print_all(self):
        if len(self.url)>50:
            n = 50
        else:
            n = len(self.url)
        for i in range(n):
            sub_html = get_html(self.url[i])
            if sub_html == '제품 정보가 없습니다.':
                pass
            else:
                sub = bs4.BeautifulSoup(sub_html, 'html.parser')
                image = self.get_img(sub)
                color = self.get_color('https://www.ikea.com'+ image)
                if isColorSimilar(color, pic_chart):
                    print('Yes')
                    if self.get_size(sub) == True:
                        self.image.append(image)
                        self.color.append(color)
                        self.get_name(sub)
                        self.get_price(sub)
                    else:
                        pass
                else:
                    pass
        return self.name, self.price, self.size, self.image


class chair(parsing_data):
    def get_size(self,sub):
        size_now = sub.select('div#metric')
        size_in = size_now[0].getText().strip()
        size_in = size_in.split(' cm')
        if len(size_in) < 2:
            self.size.append('none size')
        else:
            if '시험 중량: ' in size_in[0]:
                self.size.append([size_in[0].split(': ')[2], size_in[1].split(': ')[1], size_in[2].split(': ')[1]])
            else:
                self.size.append([size_in[0].split(': ')[1], size_in[1].split(': ')[1], size_in[2].split(': ')[1]])
        return True


class table(parsing_data):
    def get_size(self, sub):
        size_now = sub.select('div#metric')
        size_in = size_now[0].getText().strip()
        size_in = size_in.split(' cm')
        if len(size_in)<2:
            self.size.append('none size')
        elif len(size_in) == 3:
            a = int(size_in[0].split(': ')[1])
            b = int(size_in[1].split(': ')[1])
            print(a,b)
            if input_size == '원룸':
                if a>250 or b>250:
                    return False
                else:
                    self.size.append([a, b])
                    return True
            else:
                self.size.append([a, b, c])
                return True
        elif len(size_in) > 3:
            a = int(size_in[0].split(': ')[1])
            b = int(size_in[1].split(': ')[1])
            c = int(size_in[2].split(': ')[1])
            if input_size == '원룸':
                if a>250 or b>250 or c>250:
                    return False
                else:
                    self.size.append([a, b])
                    return True
            else:
                self.size.append([a, b, c])
                return True


def ikea_sofa(room_size, pic_chart, theme_pic_url):
    # class 처리
    # 소파
    def sofa_data():
        SOFA = parsing_data('https://www.ikea.com/kr/ko/catalog/categories/departments/living_room/39130/')
        name, price, size, image = SOFA.print_all()
        #print(name, price, size, image)


def ikea_chair(room_size, pic_chart, theme_pic_url):
    CHAIR = chair('https://www.ikea.com/kr/ko/catalog/categories/departments/dining/25219/')
    name, price, size, image = CHAIR.print_all()
    return name, price, size, image


def ikea_table(room_size, pic_chart, theme_pic_url):
    # 책상
    TABLE = table('https://www.ikea.com/kr/ko/catalog/categories/departments/dining/21825/')
    name, price, size, image = TABLE.print_all()
    return name, price, size, image


def ikea_closet(room_size, pic_chart, theme_pic_url):
    # 옷장
    CLOS = parsing_data('https://www.ikea.com/kr/ko/catalog/categories/departments/bedroom/10451/')
    name, price, size, image = CLOS.print_all()
    return name, price, size, image


if __name__ == "__main__":
    theme_pic_url = 'https://images.homify.com/c_fill,f_auto,h_700,q_auto/v1505116232/p/photo/image/2221347/30%ED%8F%89%EB%8C%80_%EC%95%84%ED%8C%8C%ED%8A%B8_%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B413.jpg'
    theme_pic = URLtoImage(theme_pic_url)
    pic_chart = image_color_cluster(theme_pic)
    print(list(pic_chart.keys()))
    #class 처리
    #소파
    def sofa_data():
        SOFA = parsing_data('https://www.ikea.com/kr/ko/catalog/categories/departments/living_room/39130/')
        name, price, size, image = SOFA.print_all()
        print(name, price, size, image)


    #의자
    def chair_data():
        CHAIR = chair('https://www.ikea.com/kr/ko/catalog/categories/departments/dining/25219/')
        name, price, size, image = CHAIR.print_all()
        print(name, price, size, image)


    #책상
    def table_data():
        TABLE = table('https://www.ikea.com/kr/ko/catalog/categories/departments/dining/21825/')
        name, price, size, image = TABLE.print_all()
        print(name, price, size, image)


    #옷장
    def closet_data():
        CLOS = parsing_data('https://www.ikea.com/kr/ko/catalog/categories/departments/bedroom/10451/')
        name, price, size, image = CLOS.print_all()
        print(name, price, size, image)

    input_size = '원룸'
    table_data()