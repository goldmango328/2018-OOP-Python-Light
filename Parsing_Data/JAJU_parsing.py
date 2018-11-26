# Data Parsing :: JAJU web site

from image_color_cluster3 import *
import bs4
from selenium import webdriver
        
# main page : http://living.sivillage.com/jaju/display/displayShop
# 가구 수납 : http://living.sivillage.com/jaju/display/displayCategory?dspCatNo=010000041353&upDspCatNo=010000000007&chnSct=P
# 제품 정보 : http://living.sivillage.com/jaju/product/productDetail?productNo=01P0000215289&dspCatNo=010000041353

# 문제점 (1) : 의자, 책상, 테이블이 한꺼번에 몰려있음 -> 처리 방법이 필요함
# 의자 == ' 스톨'이 들어가는 경우를 처리해주면 될 것으로 생각

driver = webdriver.PhantomJS('/Users/지명금/Desktop/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs')
driver.implicitly_wait(1)

driver.get('http://living.sivillage.com/jaju/display/displayCategory?dspCatNo=010000041353&upDspCatNo=010000000007&chnSct=P')

html = driver.page_source
soup = bs4.BeautifulSoup(html, 'html.parser')

# 이름
name = soup.select('div.subject.ellipsis_ext p')
chair_name = []

for i in name:
    # print(i.getText())
    chair_name.append(i.getText())

# 이미지
image = soup.select('div.img img')
chair_img = []

for i in image:
    # print(i.get('src'))
    chair_img.append(i.get('src'))

# 대표색상
img_color = []
for image_url in chair_img:
    image = URLtoImage(image_url)
    image_info = image_color_cluster(image)
    print(list(image_info.keys())[0])
    img_color.append(list(image_info.keys())[0])
    

# 가격
price = soup.select('div.j-item_price span.normal')
chair_price = []

for i in price:
    # print(i.getText().strip())
    chair_price.append(i.getText().strip())

# 크기
size_url = soup.select('div.item a')
sub_url = []
size = []
for i in size_url:
    # print(i.get('href'))
    product_url = 'http://living.sivillage.com' + i.get('href')
    sub_url.append(product_url)

for url in sub_url:
    driver.get(url)
    product_html = driver.page_source
    product_soup = bs4.BeautifulSoup(product_html, 'html.parser')

    source = product_soup.select('div.j-grid table.table tbody tr')
    for i in source:
        # print(i.find('th').getText())
        if i.find('th').getText() == '크기':
            print(i.find('td').getText())
            # 사이즈 쪼개기이이

            text = i.find('td').getText().upper()
            for x in ['x','X','CM','cm','(',')','높이','h','d','w','W','D','H']:
                text = text.replace(x,' ')
            text = text.split(' ')
            cnt = text.count('')
            for i in range(cnt):
                text.remove('')
            print(text)
            size.append(text)

