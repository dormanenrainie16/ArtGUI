'''
Created by: Betty Tannuzzo
Version 1
Searches Google Chrome for images based on keyword and downloads image to directory
'''
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

import json
import os
import argparse

import requests
import urllib
import urllib3
from urllib3.exceptions import InsecureRequestWarning
from io import BytesIO

import time


def search(searchword1):
    urllib3.disable_warnings(InsecureRequestWarning)

    searchurl = 'https://www.google.com/search?q=' + searchword1 + '&source=lnms&tbm=isch'

    maxcount = 100

    chromedriver = '/Users/jbujarski/PycharmProjects/proj/chromedriver'

    return maxcount, chromedriver, searchurl


def download_google_staticimages(user_input):
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    # options.add_argument('--headless')

    maxcount, chromedriver, searchurl = search(user_input)

    try:
        browser = webdriver.Chrome(chromedriver, options=options)
    except Exception as e:
        print(f'No found chromedriver in this environment.')
        print(f'Install on your machine. exception: {e}')
        sys.exit()

    browser.set_window_size(1280, 1024)
    browser.get(searchurl)
    time.sleep(1)

    print(f'Getting you a lot of images. This may take a few moments...')

    element = browser.find_element_by_tag_name('body')

    page_source = browser.page_source

    soup = BeautifulSoup(page_source, 'lxml')
    images = soup.find_all('img')

    urls = []
    for image in images:
        try:
            url = image['data-src']
            if not url.find('https://'):
                urls.append(url)
        except:
            try:
                url = image['src']
                if not url.find('https://'):
                    urls.append(image['src'])
            except Exception as e:
                print(f'No found image sources.')
                print(e)
    ret_list = []
    count = 0
    if urls:
        for url in urls:
            try:
                response = requests.get(url)
                ret_list.append(Image.open(BytesIO(response.content)))
                count += 1
                if count > maxcount: break
            except Exception as e:
                print('Failed to write rawdata.')
                print(e)

    if browser:
        browser.quit()
    return ret_list
