# File created by J Bujarski
# sample.py contains a simple main to test merging pictures en masse

import os
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import urllib

from create import *


def main():
    # Pass in a string to rand_seed
    # master = hue("cool", rand_seed("`213456", intensity=50), intensity=50)
    # master = negative("Me&Cleo.jpg")
    # master = ascii_pic("Me&Pops.jpg")
    # view_pic(master)
    scraper()


def merger():
    master = Image.Image()
    counter = 1

    for filename in os.listdir("/Users/jbujarski/Desktop/Everything/Pictures"):
        if filename.endswith(".jpg") or filename.endswith(".jpeg"):
            name = os.path.join('/Users/jbujarski/Desktop/Everything/Pictures/', filename)
            print(name)
            master = blender(name, master, counter)
            counter += 1
    view_pic(master)


def scraper():
    search = "apples"
    search = search.replace(' ', '+')
    URL = f"https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={search}&oq={search}&gs_l=img"
    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
    headers = {"user-agent": USER_AGENT}
    resp = requests.get(URL, headers=headers)

    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, "html.parser")
    results = []
    for g in soup.find_all('div', class_='r'):
        anchors = g.find_all('a')
        if anchors:
            link = anchors[0]['href']
            title = g.find('h3').text
            item = {
                "title": title,
                "link": link
            }
        results.append(item)
    print(results)

'''
def fetch_image_urls(query: str, max_links_to_fetch: int, sleep_between_interactions: int = 1):
    def scroll_to_end(wd):
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(sleep_between_interactions)

        # build the google query

    search_url = "https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={q}&oq={q}&gs_l=img"

    # load the page
    wd.get(search_url.format(q=query))

    image_urls = set()
    image_count = 0
    results_start = 0
    while image_count < max_links_to_fetch:
        scroll_to_end(wd)

        # get all image thumbnail results
        thumbnail_results = wd.find_elements_by_css_selector("img.Q4LuWd")
        number_results = len(thumbnail_results)


        for img in thumbnail_results[results_start:number_results]:
            # try to click every thumbnail such that we can get the real image behind it
            try:
                img.click()
                time.sleep(sleep_between_interactions)
            except Exception:
                continue

            # extract image urls
            actual_images = wd.find_elements_by_css_selector('img.n3VNCb')
            for actual_image in actual_images:
                if actual_image.get_attribute('src') and 'http' in actual_image.get_attribute('src'):
                    image_urls.add(actual_image.get_attribute('src'))

            image_count = len(image_urls)

            if len(image_urls) >= max_links_to_fetch:
                print(f"Found: {len(image_urls)} image links, done!")
                break
        else:
            print("Found:", len(image_urls), "image links, looking for more ...")
            time.sleep(30)
            return
            load_more_button = wd.find_element_by_css_selector(".mye4qd")
            if load_more_button:
                wd.execute_script("document.querySelector('.mye4qd').click();")

        # move the result startpoint further down
        results_start = len(thumbnail_results)

    return image_urls
'''

if __name__ == "__main__":
    main()
