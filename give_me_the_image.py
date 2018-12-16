import bs4
import requests


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


def theme_in(select_theme):
    if select_theme == '모던':
        return 'https://www.homify.co.kr/rooms/style-modern'
    elif select_theme == '미니멀':
        return 'https://www.homify.co.kr/rooms/style-minimalist'
    elif select_theme == '북유럽':
        return 'https://www.homify.co.kr/rooms/style-scandinavian'
    elif select_theme == '컨트리':
        return 'https://www.homify.co.kr/rooms/style-country'


def get_theme_image(input_theme):
    html = get_html(theme_in(input_theme))
    data = bs4.BeautifulSoup(html, 'html.parser')
    url_main = data.select('div.container div.-spaced-horizontal- ol.-spaced-horizontal- li.-block- div.photo a.js-photo-link')

    url_sub = []
    image = []
    for line in url_main:
        url_sub.append('https://www.homify.co.kr' + line.get('href'))

    for line in url_sub:
        sub_html = get_html(line)
        sub = bs4.BeautifulSoup(sub_html, 'html.parser')
        image_now = sub.select('div.big-photo div.big-photo--container div.-up-to-sm- img.big-photo--photo')
        for img_line in image_now:
            image.append(img_line.get('src'))

    return image

if __name__ == "__main__":
    print(get_theme_image('모던'))
