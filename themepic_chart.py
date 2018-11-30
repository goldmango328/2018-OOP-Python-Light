import image_percent_plot

def getCHART(theme_pic_url):
    theme_pic = image_percent_plot.URLtoImage(theme_pic_url)
    pic_chart = image_percent_plot.image_color_cluster(theme_pic)
    return list(pic_chart.keys())