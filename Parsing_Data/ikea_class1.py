import bs4
import requests


def get_html(url):
    """
    웹 사이트 주소를 입력 받아, html tag 를 읽어드려 반환한다.
    :param url: parsing target web url
    :return: html tag
    """
    response = requests.get(url)
    response.raise_for_status()

    return response.text

def get_url(data):
    url_main = data.select('div.productLists div.gridRow div.threeColumn div.image a')
    url = []
    for i in url_main:
        url.append("https://www.ikea.com/" + i.get('href'))
    return url

class sofa:
    def __init__(self,in_url):
        self.html= get_html(in_url)
        self.data = bs4.BeautifulSoup(self.html, 'html.parser')
        self.image = []
        self.name = []
        self.price = []
        self.size = []
        self.url = get_url(self.data)

    def get_img(self):
        for i in self.url:
            sub_html = get_html(i)
            sub = bs4.BeautifulSoup(sub_html, 'html.parser')
            sub_main = sub.select('div.rightContent div.pipContainer div#leftMainContainer div.rightContentContainer img#productImg')
            sub_main = str(sub_main[0]).split(' ')
            for line in sub_main:
                if 'src' in line:
                    line = line.replace('"', '')
                    line = line.replace('src=', '')
                    self.image.append(line)
        return self.image

    def get_name(self):
        for i in self.url:
            sub_html = get_html(i)
            sub = bs4.BeautifulSoup(sub_html, 'html.parser')
            name_now = sub.select('div.addList div.rightInfoDiv h1 span.productName')
            for i in name_now:
                name_in = i.getText().strip()
                self.name.append(name_in)
                print(name_in)
        return self.name

    def get_price(self):
        for i in self.url:
            sub_html = get_html(i)
            sub = bs4.BeautifulSoup(sub_html, 'html.parser')
            price_now = sub.select('div.addList div.rightInfoDiv div.priceContainer span.packagePrice')
            for i in price_now:
                price_in = i.getText().strip()
                price_in = str(price_in).replace('\xa0', '')
                self.price.append(price_in)
        return self.price

    def get_size(self):
        for i in self.url:
            sub_html = get_html(i)
            sub = bs4.BeautifulSoup(sub_html, 'html.parser')
            size_now = sub.select('div#metric')
            for i in size_now:
                size_in = i.getText().strip()
                size_in = str(size_in).split(' cm')
                if len(size_in) < 3:
                    self.size.append('none size')
                else:
                    self.size.append(size_in[0].split(': ')[1] + ' cm X ' + size_in[1].split(': ')[1] + ' cm X ' + size_in[2].split(': ')[1] + ' cm')
        return self.size

    '''def print_all(self):
        for i in self.url:
            sub_html = get_html(i)
            sub = bs4.BeautifulSoup(sub_html, 'html.parser')
            self.get_img(sub)
            self.get_name(sub)
            self.get_price(sub)
            self.get_size(sub)
        return self.url, self.name, self.price, self.image, self.size'''


#class 처리
SOFA = sofa('https://www.ikea.com/kr/ko/catalog/categories/departments/living_room/39130/')
print(SOFA.get_name())
print(SOFA.get_img())
print(SOFA.get_size())
print(SOFA.get_price())
