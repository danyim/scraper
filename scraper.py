"""
Scrapes wehpage data
"""

import sys
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

def main(argv):
    """ Runs the scraper and extracts the items from the website """

    if len(argv) <= 1:
        print 'Usage:\tscraper.py [URL] [output file]'
        exit()

    url = argv[1]
    tree = get_web_html_using_driver(url)
    all_items = tree.xpath('//li[@class="js-product-list-item"]')
    processed_items = []

    for i in all_items:
        obj = {}
        obj['brand'] = i.attrib['data-brand'].strip()
        obj['itemname'] = i.attrib['data-name'].strip()
        obj['price'] = i.attrib['data-wl-price'].strip()
        processed_items.append(obj)

    print 'Found', len(processed_items), 'items...\n'
    print obj_to_json(processed_items)

    if argv[1] != '':
        out_filename = argv[2]
        print 'Outputting to', out_filename
        with open(out_filename, 'a') as out_file:
            out_file.write(obj_to_json(processed_items))

if __name__ == '__main__':
    main(sys.argv)
