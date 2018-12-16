import numpy as np
import cv2
import matplotlib.image as mpimg
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from PIL import Image
import urllib
import operator

def sameWithBack(r,g,b):
    if 0<=r<=2 and 246<=g<=248 and 239<=b<=241 :
        return True
    else :
        return False
    
def RGBtoHEX(r,g,b):
    hex = "#{:02x}{:02x}{:02x}".format(r,g,b)
    return hex

def getColorPercent(hist, centroids):
    colorPercent = {}
    for (percent,color) in zip(hist, centroids):
        colorlst = color.astype("uint8").tolist()
        Hex = RGBtoHEX(*colorlst)

        if sameWithBack(*colorlst):
            continue
        else :
            # print(percent,Hex)
            colorPercent[str(Hex)] = percent
            
    return colorPercent

def centroid_histogram(clt):
    # grab the number of different clusters and create a histogram
    # based on the number of pixels assigned to each cluster
    # 색상 정보와 관련된 histogram을 만들어서 hist라는 형식에 저장하는 함수
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)

    # normalize the histogram, such that it sums to one
    hist = hist.astype("float")
    hist /= hist.sum()
    
    # return the histogram
    return hist

def image_color_cluster(image, k = 5):
    convert_image = changeBackground(image).convert('RGB')
    convert_image = np.array(convert_image)
    convert_image = convert_image[:,:,::-1].copy()

    image = cv2.cvtColor(convert_image, cv2.COLOR_BGR2RGB)
    image = image.reshape((image.shape[0] * image.shape[1], 3))
    
    clt = KMeans(n_clusters = k)
    clt.fit(image)

    hist = centroid_histogram(clt)
    # 색상 정보를 맞게 가져왔는지 눈으로 확인해보고 싶을때
    # bar = plot_colors(hist, clt.cluster_centers_)
    # plt.figure()
    # plt.axis("off")
    # plt.imshow(bar)
    # plt.show() 
    dct = getColorPercent(hist, clt.cluster_centers_)

    sorted_lst = sorted(dct.items(), key=operator.itemgetter(1),reverse=True)

    sorted_dct = {}
    for (key,value) in sorted_lst:
        sorted_dct[key] = value
    return dct

def changeBackground(img):
    img = img.convert("RGBA")
    datas = img.getdata()

    newData = [] # 이미지를 pixel 단위로 쪼개서 alpha를 확인하여 제거하는 과정
    for item in datas:
        if item[0] > 200 and item[1] > 200 and item[2] > 200: # image의 흰색 배경을 제거하는 코드
            newData.append((0,247,240,0)) # image alpha channel-> 0으로 줄여서 아예 보이지 않게 하는 것
        else :
            newData.append(item)

    img.putdata(newData)
    return img

def plot_colors(hist, centroids):
    # initialize the bar chart representing the relative frequency
    # of each of the colors
    bar = np.zeros((50, 300, 3), dtype="uint8")
    startX = 0

    # loop over the percentage of each cluster and the color of
    # each cluster
    for (percent, color) in zip(hist, centroids):
        # plot the relative percentage of each cluster
        endX = startX + (percent * 300)
        cv2.rectangle(bar, (int(startX), 0), (int(endX), 50),
                      color.astype("uint8").tolist(), -1)
        startX = endX

    # return the bar chart
    return bar

def URLtoImage(url):
    resp = urllib.request.urlopen(url)   
    image_array = np.asarray(bytearray(resp.read()), dtype="uint8")
    image_array = cv2.imdecode(image_array,-1)
    image = Image.fromarray(image_array, 'RGB')
    return image

if __name__ == "__main__":
    # parsing 코드에서 실행할 부분은 여기!
    # 넘겨줄 image url
    image_url = 'http://img.sivillage.com/files/product/01/P0000/21/52/89/01P0000215289_500.jpg'
    image = URLtoImage(image_url)
    # image_info : 정렬된 색상테마를 담은 dictionary
    image_info = image_color_cluster(image)
