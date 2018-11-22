# Data Parsing :: REMOD web site

# LOUNGE CHAIR :: cate_no = 139
# DINING CHAIR :: cate_no = 140
# BAR CHAIR :: cate_no = 141
# OFFICE CHAIR :: cate_no = 143

from image_color_cluster3 import *
import bs4
import requests

headers = {'User-Agent': 'Mozilla/5.0'}
furni = {'chair':['139','140','141','143'],'sofa':['138'],'cutton':[],'table':['134','135','136','137'],'dresser':['175']}

# 함수를 통해 원하는 색상, 테마를 입력받고 이를 기준으로 파싱하게끔 코드를 구성해야 함
def getHTML(url):
    response = requests.get(url,headers=headers)

    return response.text

def getImage(url): # 해당하는 url로부터 이미지를 받아오는 함수
    pass

def getColorChart(color): # color라는 dict를 가져오면 거기에서 keys()만 가져오자
    colorchart = list(color.keys())
    return colorchart

def getRepColor(url): # image url에서부터 대표 색상을 뽑아오는 사이트
    image = URLtoImage(url)
    image_info = image_color_cluster(image)
    repcolor = list(image_info.keys())
    return repcolor[0]

for cate_lst in furni.values():
    print(cate_lst)
    for furni in cate_lst:
        # 403 Forbidden Error 가 발생할 상황에 대비하여 headers
        html_text = getHTML('http://www.remod.co.kr/product/list.html?cate_no=139')
        soup = bs4.BeautifulSoup(html_text,'html.parser') 

        content = soup.select('div.xans-element-.xans-product.xans-product-normalpackage div.xans-element-.xans-product.xans-product-listnormal ul li div.box a')
        content_url = [x.get('href') for x in content]
        content_url = list(set(content_url)) # 중복된 데이터 제거 -> 단 파싱된 순서가 별도로 저장되지는 않음
        
        for url in content_url:
            product_url = 'http://www.remod.co.kr'+url
            product_html_text = getHTML(product_url)
            product_soup = bs4.BeautifulSoup(product_html_text, 'html.parser')

            # 색상을 먼저 판단하고 그 다음에 파싱하는 거로..
            
            source = product_soup.select("div.xans-element-.xans-product.xans-product-detail div.detailArea div.keyImg div.thumbnail a img")
            info = []
            flag = True
            for image_url in source:
                product_name = image_url.get('alt') # (1)제품 이름
                product_img = 'http:'+image_url.get('src') # (2)제품 사진
                product_color = getRepColor(product_img) # (3)제품 대표색상
                info.append(x for x in (product_name,product_img,product_color))
                if flag==True:break

            source = product_soup.select("div.xans-element-.xans-product.xans-product-additional div.cont p span")
            # 왜 사이즈를 못 가져오지..
            for detail in source:
                try:
                    if detail.getText().split()[0] == '사이즈':
                        print(detail.getText().split()[2])
                except IndexError:
                    print("ERROR")
                    continue
                
