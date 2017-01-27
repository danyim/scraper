from lxml import html
import requests
import jsonpickle
from selenium import webdriver

url = 'https://www.carid.com/advanceone-wheels/'

# Sends simple 200 request--for static pages
# page = requests.get(url)
# tree = html.fromstring(page.content)

# Using the webdriver will allow for fetching dynamic content
driver = webdriver.Firefox()
driver.get('https://www.carid.com/advanceone-wheels/')

tree = html.fromstring(driver.page_source)
all_items = tree.xpath('//li[@class="js-product-list-item"]')
processed_items = []

class CarItem(object):
    pass

for i in all_items:
    obj = CarItem()
    obj.brand = i.attrib["data-brand"].strip()
    obj.itemname = i.attrib["data-name"].strip()
    obj.price = i.attrib["data-wl-price"].strip()
    processed_items.append(obj)

print jsonpickle.encode(processed_items)
