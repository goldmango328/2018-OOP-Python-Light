import numpy as np
from skimage import io
from skimage.color import rgb2lab, deltaE_cie76

def hex_to_rgb(value):
    value = value.lstrip('#')
    length = len(value)
    return list(int(value[i:i+(length//3)],16) for i in range(0, length, length//3))

def get_ColorChart(chart):
    chart = list(hex_to_rgb(value) for value in chart)
    return chart

# im_color :: 이미지 대표 색상 ex) #FFFFFF
# chart :: 테마 색상 차트  ex) ['#FFFFFF','#0FAAFG' ... ]
def isColorSimilar(im_color, chart):
    im_color = hex_to_rgb(im_color) # HEX 코드로 된 이미지 대표 색상을 RGB로 변환
    chart = get_ColorChart(chart) # 테마 색상차트의 element를 전부 hex에서 rgb로 변환
    rgb = np.array([[im_color]]) 
    lab = rgb2lab(rgb)
    threshold = 20 # 얼마나 비슷한 색상을 가져올건지 범위 설정

    for color in chart:
        color_3d = np.uint8(np.asarray([[color]]))
        dE_color = deltaE_cie76(rgb2lab(color_3d), lab)

        if dE_color.any() < threshold :
            return True
    return False
