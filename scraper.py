from lxml import html
import requests
import jsonpickle

page = requests.get('https://www.carid.com/advanceone-wheels/')
tree = html.fromstring(page.content)
# item = tree.xpath('//div[@title="buyer-name"]/text()')
# brand = tree.xpath('//span[@class="lst_a_name"]/b/text()')
# itemname = tree.xpath('//span[@class="lst_a_name"]/span/text()')

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
# print "buyers: ", buyers
# print "brand: ", brand
# print "item: ", item
