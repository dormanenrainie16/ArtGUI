from google_images_download import google_images_download
response = google_images_download.googleimagesdownload()

search_query = input("Enter a word to search: ")


def download_images(query):
    '''
    - keywords is the search query
    - format is the the image file format
    - limit is the number of images to be downloaded
    - print_urls is to print the image file url
    - size is the image size which can be specified
        manually ('large, medium, icon')
    - aspect_ratio denotes the height width ratio
        of images to download.
        ('tall, square, wide, panoramic')
    '''

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
