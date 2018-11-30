import bs4
import requests
import image_percent_plot


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
    global cnt
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
        #print(name_now)
        name_in = name_now[0].getText().strip()
        print(name_in)
        self.name.append(name_in)
        return self.name

    def get_price(self, sub):
        price_now = sub.select('div.addList div.rightInfoDiv div.priceContainer span.packagePrice')
        price_in = price_now[0].getText().strip()
        price_in = price_in.replace('₩\xa0','')
        print(price_in)
        self.price.append(price_in)
        return self.price

    def get_size(self, sub):
        size_now = sub.select('div#metric')
        size_in = size_now[0].getText().strip()
        size_in = size_in.split(' cm')
        if len(size_in) < 3:
            self.size.append('none size')
        else:
            self.size.append([size_in[0].split(': ')[1], size_in[1].split(': ')[1], size_in[2].split(': ')[1]])
        return self.size

    def get_color(self, image_url):
        image = image_percent_plot.URLtoImage(image_url)
        image_info = image_percent_plot.image_color_cluster(image)
        print(list(image_info.keys())[0])
        return list(image_info.keys())[0]

    def print_all(self):
        for i in self.url:
            sub_html = get_html(i)
            if sub_html == '제품 정보가 없습니다.':
                pass
            else:
                sub = bs4.BeautifulSoup(sub_html, 'html.parser')
                image = self.get_img(sub)
                color = self.get_color('https://www.ikea.com'+ image)
                if color is theme_pic_color[0]:  #이 부분만 모듈로 수정하면 될 거같아요!
                    print("Yes!")
                    self.image.append(image)
                    self.color.append(color)
                    self.get_name(sub)
                    self.get_price(sub)
                    self.get_size(sub)
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
        return self.size

class table(parsing_data):
    def get_size(self, sub):
        size_now = sub.select('div#metric')
        size_in = size_now[0].getText().strip()
        size_in = size_in.split(' cm')
        print(size_in)
        if len(size_in)<2:
            self.size.append('none size')
        elif len(size_in) == 3:
            self.size.append([size_in[0].split(': ')[1], size_in[1].split(': ')[1]])
        elif len(size_in) > 3:
            self.size.append([size_in[0].split(': ')[1], size_in[1].split(': ')[1], size_in[2].split(': ')[1]])
        return self.size


if __name__ == "__main__":
    theme_pic_url = 'https://images.homify.com/c_fill,f_auto,q_auto:eco,w_980/v1490248980/p/photo/image/1918911/IMG_6320.jpg'
    theme_pic = image_percent_plot.URLtoImage(theme_pic_url)
    theme_pic_color = image_percent_plot.image_color_cluster(theme_pic)
    print(theme_pic_color.getkeys())
    #class 처리
    #소파
    def sofa_data():
        SOFA = parsing_data('https://www.ikea.com/kr/ko/catalog/categories/departments/living_room/39130/')
        SOFA.print_all()


    #의자
    def chair_data():
        CHAIR = chair('https://www.ikea.com/kr/ko/catalog/categories/departments/dining/25219/')
        CHAIR.print_all()


    #책상
    def table_data():
        TABLE = table('https://www.ikea.com/kr/ko/catalog/categories/departments/dining/21825/')
        TABLE.print_all()


    #옷장
    def closet_data():
        CLOS = parsing_data('https://www.ikea.com/kr/ko/catalog/categories/departments/bedroom/10451/')
        CLOS.print_all()

    sofa_data()