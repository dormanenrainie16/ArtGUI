'''
from google_images_download import google_images_download
response = google_images_download.googleimagesdownload()

search_query = input("Enter a word to search: ")


def download_images(query):

    - keywords is the search query
    - format is the the image file format
    - limit is the number of images to be downloaded
    - print_urls is to print the image file url
    - size is the image size which can be specified
        manually ('large, medium, icon')
    - aspect_ratio denotes the height width ratio
        of images to download.
        ('tall, square, wide, panoramic')


    argument = {"keywords": query,
                "format": "jpg",
                "limit": 5,
                "print_urls": True,
                "size": "medium",
                "aspect_radio": "panoramic"}
    try:
        response.download(argument)

    except FileNotFoundError:
        argument = {"keywords": query,
                    "format": "jpg",
                    "limit": 5,
                    "print_urls": True,
                    "size": "medium"}

        try:
            response.download(query)
        except:
            pass


# for query in search_query:
download_images(search_query)
print()
'''

'''
from giextractor import GoogleImageExtractor
import time
from selenium import webdriver

driver = webdriver.Chrome('C://Program Files//chromedriver.exe')
driver.get('http://www.google.com/')
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()

imageExtractor = GoogleImageExtractor()
imageExtractor.extract_images(imageQuery='apple fruit', imageCount=500)
'''

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

import datetime
import time

urllib3.disable_warnings(InsecureRequestWarning)


def search(searchword1):
    # searchword1 = input("Enter a word to search: ")
    searchurl = 'https://www.google.com/search?q=' + searchword1 + '&source=lnms&tbm=isch'

    dirs = 'pictures'
    maxcount = 100

    chromedriver = 'C://Program Files//chromedriver.exe'

    if not os.path.exists(dirs):
        os.mkdir(dirs)

    return dirs, maxcount, chromedriver, searchurl

def download_google_staticimages(user_input):
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    # options.add_argument('--headless')

    dirs, maxcount, chromedriver,searchurl = search(user_input)

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

    # Scroll down
    # for i in range(30):
    for i in range(50):
        element.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.3)

    try:
        browser.find_element_by_id('smb').click()
        for i in range(50):
            element.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.3)
    except:
        for i in range(10):
            element.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.3)

    print(f'Reached end of page.')
    time.sleep(0.5)
    print(f'Retry')
    time.sleep(0.5)

    # Below is in japanese "show more result" sentences. Change this word to your lanaguage if you require.
    browser.find_element_by_xpath('//input[@value="Show more results"]').click()

    # Scroll down 2
    for i in range(50):
        element.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.3)

    try:
        browser.find_element_by_id('smb').click()
        for i in range(50):
            element.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.3)
    except:
        for i in range(10):
            element.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.3)

    # elements = browser.find_elements_by_xpath('//div[@id="islrg"]')
    # page_source = elements[0].get_attribute('innerHTML')
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

    count = 0
    if urls:
        for url in urls:
            try:
                res = requests.get(url, verify=False, stream=True)
                rawdata = res.raw.read()
                with open(os.path.join(dirs, 'img_' + str(count) + '.jpg'), 'wb') as f:
                    f.write(rawdata)
                    count += 1
            except Exception as e:
                print('Failed to write rawdata.')
                print(e)

    browser.close()
    return count


# Main block
def main():
    t0 = time.time()
    count = download_google_staticimages("rainbow")
    t1 = time.time()

    total_time = t1 - t0
    print(f'\n')
    print(f'Download completed. [Successful count = {count}].')
    print(f'Total time is {str(total_time)} seconds.')


if __name__ == '__main__':
    main()
