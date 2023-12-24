from urllib.request import urlopen
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import ssl

ctx = ssl.create_default_context()  
ctx.check_hostname = True
ctx.verify_mode = ssl.CERT_REQUIRED


def image_url(soup): 
    css_selector = '.hds-image-of-the-day img'
    img_tag = soup.select_one(css_selector)
    return img_tag['src'] if img_tag else None


def open_nasa_homepage():  
    nasa_homepage = 'https://www.nasa.gov/'
    html = urlopen(nasa_homepage, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup


if __name__ == '__main__':
    soup_object = open_nasa_homepage()
    image_link = image_url(soup_object)

    image_data = urlopen(image_link, context=ctx).read()  
    handle_binary = BytesIO(image_data) 
    Image.open(handle_binary).show()  
