from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000

def hex_to_rgb(value):
    value = value.lstrip('#')
    length = len(value)
    return tuple(int(value[i:i+(length//3)],16) for i in range(0, length, length//3))

def isColorSimilar(im_color, chart):
    compare = 20
    
    im_color = hex_to_rgb(im_color)
    im_rgb = sRGBColor(*im_color)
    im_lab = convert_color(im_rgb, LabColor)

    for elem in chart:
        elem = hex_to_rgb(elem)
        elem_rgb = sRGBColor(*elem)
        elem_lab = convert_color(elem_rgb, LabColor)

        delta_e = delta_e_cie2000(im_lab, elem_lab)
        # print("[DIFF] :",delta_e)
        if delta_e < compare:
            return True
    return False

if __name__ == '__main__':
    print(isColorSimilar('CEB617',['ECD01C']))
