from lxml import html
import requests
import jsonpickle
from selenium import webdriver

URL = 'https://www.carid.com/advanceone-wheels/'

def get_web_html_using_driver(url):
    """ Using the webdriver will allow for fetching dynamic content """
    driver = webdriver.Firefox()
    driver.get(url)
    return html.fromstring(driver.page_source)

def get_web_html_using_request(url):
    """ Sends simple 200 request to grab static pages """
    page = requests.get(url)
    return html.fromstring(page.content)

def obj_to_json(obj):
    """ Function wrapper for JSON encoding """
    return jsonpickle.encode(obj)

def main():
    """ Runs the scraper and extracts the items from the website """
    tree = get_web_html_using_driver(URL)
    all_items = tree.xpath('//li[@class="js-product-list-item"]')
    processed_items = []

    for i in all_items:
        obj = {}
        obj['brand'] = i.attrib["data-brand"].strip()
        obj['itemname'] = i.attrib["data-name"].strip()
        obj['price'] = i.attrib["data-wl-price"].strip()
        processed_items.append(obj)

    print 'Found', len(processed_items), 'items...\n'
    print obj_to_json(processed_items)

if __name__ == "__main__":
    main()
