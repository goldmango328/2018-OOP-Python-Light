# Image Color Cluster  
상태 : **완성**  
이미지에서 색상비중을 고려하여 대표 색상을 추출해내는 프로그램::[출처](https://inyl.github.io/programming/2017/07/31/opencv_image_color_cluster.html?fbclid=IwAR3lilgOrYh-N7Qqso-1E4hb3XWV7dgy3VvONRBTFG-ceLxsjhrXg-Kwo-A)  

1) image_color_cluster.py :: 최종본(함수처리 완료, image_path: url test 필요)  
2) image_color_cluster2.py :: 수정2차본(최종본 바로 이전 단계, 함수처리 이전의 버전)  
3) image_color_cluster3.py :: **진짜 최종본!**(image url로 변환 가능함)  

## image_color_cluster3 이용법  

/# image_url : image가 들어있는 url  
image = URLtoImage(image_url)  
/# image_info : 정렬된 색상테마를 담은 dictionary  
image_info = image_color_cluster(image)  

