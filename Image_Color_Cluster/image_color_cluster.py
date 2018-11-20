import numpy as np
import cv2
import matplotlib.image as mpimg
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from PIL import Image

def centroid_histogram(clt):
    # grab the number of different clusters and create a histogram
    # based on the number of pixels assigned to each cluster
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)

    # normalize the histogram, such that it sums to one
    hist = hist.astype("float")
    hist /= hist.sum()

    # return the histogram
    return hist

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

def image_color_cluster(image_path, k = 5):
    image = cv2.imread(image_path,cv2.IMREAD_UNCHANGED) # alpha channel 을 가져오는 것
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = image.reshape((image.shape[0] * image.shape[1], 3))
    
    clt = KMeans(n_clusters = k)
    clt.fit(image)

    hist = centroid_histogram(clt)
    bar = plot_colors(hist, clt.cluster_centers_)
    
    plt.figure()
    plt.axis("off")
    plt.imshow(bar)
    plt.show()

# Image Convert : JPEG -> PNG
img = Image.open('chair.jpg') # 해당하는 이미지 
img = img.convert("RGBA")
datas = img.getdata()

newData = [] # 이미지를 pixel 단위로 쪼개서 alpha를 확인하여 제거하는 과정
for item in datas:
    if item[0] > 200 and item[1] > 200 and item[2] > 200: # image의 흰색 배경을 제거하는 코드
        newData.append((item[0], item[1], item[2],0)) # image alpha channel-> 0으로 줄여서 아예 보이지 않게 하는 것
    else :
        newData.append(item)

img.putdata(newData)
img.save('chair_2.png',"PNG")
    
image_path ="chair_2.png"
# image path를 이렇게 설정해도 실제로 코드에서 돌아갈 때는
# 배경이 있는 이미지로 진행됨 -> 왜??????ㅜㅠㅜㅠㅜ

#preview image
image = mpimg.imread(image_path,cv2.IMREAD_UNCHANGED)
plt.imshow(image)

image_color_cluster(image_path)
    
