from image_color_cluster3 import *

def get_imagechart(image_lst):
    pic_chart = []
    
    for img_url in image_lst:
        image = URLtoImage(img_url)
        image_info = image_color_cluster(image)
        pic_chart.extend(list(image_info.keys()))

    return pic_chart

if __name__ == "__main__":
    image_lst = ['http://www.remod.co.kr/web/product/big/201810/1d7852270e75210f4ec535b09bf4d378.jpg','http://www.remod.co.kr/web/product/big/201810/394f949e38f86a95ca601f9ce7720433.jpg']
    pic = get_imagechart(image_lst)
    print(pic)
