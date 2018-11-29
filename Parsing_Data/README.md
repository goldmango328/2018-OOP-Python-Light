# Parsing Data  
> 전체 조사한 사이트들 중 아래의 사이트에서 자료를 긁어오는 것으로 최종 결정을 내림    
1) [이케아](https://www.ikea.com/) :: 유현아 **끝!**  
2) [리모드](http://www.remod.co.kr/)  :: 지명금 ****  
4) [자주JAJU](http://living.sivillage.com/jaju/display/displayShop?temp=www.jaju.co.kr) :: 지명금 **끝!**  

## 파싱해올 데이터  
> 각 사이트에서 파싱해올 자료  
1) 이름
2) 사진
3) 가격
4) 길이,폭,높이
5) 대표색상(GUI)
6) 링크

## import module   
> 이케아, 리모드, 자주를 파싱하는 데 이용한 모듈들에 대한 정리  

import [image_color_cluster3](https://github.com/goldmango328/2018-OOP-Python-Light/tree/DataParsing/Image_Color_Cluster)  
import beautifulsoup4  
from selenium import webdriver  

## 2018-11-29 ERROR  
Traceback (most recent call last):
  File "C:\Users\지명금\Desktop\OOP-Python-Light\remod_class1.py", line 182, in <module>
    sf_url, sf_name, sf_price, sf_img, sf_size, sf_color = SOFA.print_all()
  File "C:\Users\지명금\Desktop\OOP-Python-Light\remod_class1.py", line 154, in print_all
    self.get_color()
  File "C:\Users\지명금\Desktop\OOP-Python-Light\remod_class1.py", line 135, in get_color
    image = URLtoImage(image_url)
  File "C:\Users\지명금\Desktop\OOP-Python-Light\image_color_cluster3.py", line 111, in URLtoImage
    image = Image.fromarray(image_array, 'RGB')
  File "C:\Users\지명금\AppData\Local\Programs\Python\Python37-32\lib\site-packages\PIL\Image.py", line 2511, in fromarray
    return frombuffer(mode, size, obj, "raw", rawmode, 0, 1)
  File "C:\Users\지명금\AppData\Local\Programs\Python\Python37-32\lib\site-packages\PIL\Image.py", line 2454, in frombuffer
    return frombytes(mode, size, data, decoder_name, args)
  File "C:\Users\지명금\AppData\Local\Programs\Python\Python37-32\lib\site-packages\PIL\Image.py", line 2387, in frombytes
    im.frombytes(data, decoder_name, args)
  File "C:\Users\지명금\AppData\Local\Programs\Python\Python37-32\lib\site-packages\PIL\Image.py", line 801, in frombytes
    raise ValueError("not enough image data")
ValueError: not enough image data
