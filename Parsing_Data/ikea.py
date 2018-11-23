import bs4
import requests
import re

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

def get_img(sub):
        sub_main = sub.select('div.rightContent div.pipContainer div#leftMainContainer div.rightContentContainer img#productImg')
        sub_main = str(sub_main[0]).split(' ')
        for line in sub_main:
            if 'src' in line:
                line = line.replace('"', '')
                line = line.replace('src=', '')
                image.append(line)

def get_name(sub):
        name_now = sub.select('div.addList div.rightInfoDiv h1 span.productName')
        for i in name_now:
            name_in = i.getText().strip()
            name.append(name_in)

def get_price(sub):
        price_now = sub.select('div.addList div.rightInfoDiv div.priceContainer span.packagePrice')
        for i in price_now:
            price_in = i.getText().strip()
            price_in = str(price_in).replace('\xa0','')
            price.append(price_in)
            #print(price_in)
def get_size(sub):
    size_now = sub.select('div#metric')
    for i in size_now:
        size_in = i.getText().strip()
        size_in = str(size_in).split(' cm')
        if len(size_in) < 3:
            size.append('none size')
        else:
            size.append(size_in[0].split(': ')[1] + ' cm X ' + size_in[1].split(': ')[1] + ' cm X ' + size_in[2].split(': ')[1] + ' cm')

#소파
html = get_html('https://www.ikea.com/kr/ko/catalog/categories/departments/living_room/39130/')
sofa = bs4.BeautifulSoup(html, 'html.parser')
image = []
name = []
price = []
size = []

url = get_url(sofa)
#링크를 타고 들어가서 사진, 이름, 가격, 사이즈 처리
# 마지막에 사진을 넘겨줘서 사진의 대푯값 찾기
cnt = 1
for i in url:
    sub_html = get_html(i)
    sub = bs4.BeautifulSoup(sub_html, 'html.parser')
    #get_img(sub)
    #get_name(sub)
    get_price(sub)
    #get_size(sub)

print(price)