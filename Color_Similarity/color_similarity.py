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

def isColorSimilar(im_color, chart):
    rgb = np.array([[im_color]])
    lab = rgb2lab(rgb)
    threshold = 20 # 얼마나 비슷한 색상을 가져올건지 범위 설정

    for color in chart:
        color_3d = np.uint8(np.asarray([[color]]))
        dE_color = deltaE_cie76(rgb2lab(color_3d), lab)

        if dE_color.any() < threshold :
            print('True')
            return True
    return False
