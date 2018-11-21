# Image Color Cluster  
상태 : **완성**  
이미지에서 색상비중을 고려하여 대표 색상을 추출해내는 프로그램::[출처](https://inyl.github.io/programming/2017/07/31/opencv_image_color_cluster.html?fbclid=IwAR3lilgOrYh-N7Qqso-1E4hb3XWV7dgy3VvONRBTFG-ceLxsjhrXg-Kwo-A)  

1) image_color_cluster.py :: 최종본(함수처리 완료, image_path: url test 필요)  
2) image_color_cluster2.py :: 수정2차본(최종본 바로 이전 단계, 함수처리 이전의 버전)  
3) image_color_cluster3.py :: **진짜 최종본!**(image url로 변환 가능함)  

## image_color_cluster3 이용법  
<pre><code># image_url : image가 들어있는 url  
image = URLtoImage(image_url)  
# image_info : 정렬된 색상테마를 담은 dictionary  
image_info = image_color_cluster(image)  
</code></pre>

## import module  
<pre><code>import numpy as np  
import cv2  
import matplotlib.image as mpimg  
from matplotlib import pyplot as plt  
from sklearn.cluster import KMeans  
from PIL import Image  
import urllib  
import operator  
</code></pre>

import **numpy,cv2,matplotlib,sklearn.cluster,PIL,urllib, operator**  

+) install sklearn.cluster
<pre><code>pip install -U scikit-learn</code></pre>  
+) install cv2  
<pre><code>pip install OpenCV-Python</code></pre>  
