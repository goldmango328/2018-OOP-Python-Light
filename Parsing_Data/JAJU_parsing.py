# Data Parsing :: JAJU web site

import image_color_cluster
import bs4
import requests

def get_html(url):
    repsonse = requests.get(url)
    response.raise_for_status()

    return response.text
