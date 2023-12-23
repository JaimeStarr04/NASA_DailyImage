from urllib.request import urlopen
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import ssl

ctx = ssl.create_default_context()  # safely handles SSL/TLS certificate/authentication
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def image_url(soup):  # navigates to image url src by using CSS unique id
    css_selector = '.hds-image-of-the-day img'
    img_tag = soup.select_one(css_selector)
    return img_tag['src'] if img_tag else None


def open_nasa_homepage():  # opens nasa's homepage and uses bs4 to parses html for easier coding
    nasa_homepage = 'https://www.nasa.gov/'
    html = urlopen(nasa_homepage, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup


if __name__ == '__main__':
    soup_object = open_nasa_homepage()
    image_link = image_url(soup_object)

    image_data = urlopen(image_link, context=ctx).read()  # opens image url and reads the data
    handle_binary = BytesIO(image_data)  # handles the binary content of the image data and treats them like file
    # like object (what Image.open) expects to read from
    Image.open(handle_binary).show()  # saves img as temp file and displays it
