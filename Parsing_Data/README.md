# Parsing Data  
> 전체 조사한 사이트들 중 아래의 사이트에서 자료를 긁어오는 것으로 최종 결정을 내림    
1) [이케아](https://www.ikea.com/) :: 유현아 **작업중**  
2) [리모드](http://www.remod.co.kr/)  
4) [자주JAJU](http://living.sivillage.com/jaju/display/displayShop?temp=www.jaju.co.kr) :: 지명금 **작업중**  

## 파싱해올 데이터  
> 각 사이트에서 파싱해올 자료  

:size: 가구의 사이즈   
:color: 가구의 대표색상  
- 사진에서의 컬러차트를 뽑고 가구의 대표색상과 비교 (인테리어 : 컬러차트, 가구 : 대표색상)  
:source: 가구 판매처  
:image url: 가구 이미지 url 출처  

## import module   
> 이케아, 리모드, 자주를 파싱하는 데 이용한 모듈들에 대한 정리  

import [image_color_cluster](https://github.com/goldmango328/2018-OOP-Python-Light/tree/DataParsing/Image_Color_Cluster)  
import beautifulsoup4  

