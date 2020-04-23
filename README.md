# ArtGUI
Python Group Project - Permits various photo searching/editing capabilities.

Team Members:
* Betty Tannnuzzo
* Rainie Dormanen
* J Bujarski

NOTE: To properly implement the webscraper, chromedriver MUST be included in the PATH used in download_images.py.
Further, ensure pixels.jpg is in the current working directory.

Libraries required:
* tkinter
* random
* sys
* io.BytesIO
* requests
* urllib3
* PIL.Image
* Pil.ImageTK
* bs4.BeautifulSoup
* selenium.webdriver
* urllib3.exceptions.InsecureRequestWarning
* matplotlib.pyplot (file for testing purposes)
* numpy
* os

Other resources required:
* chromedriver (version 81 used)

Extra features implemented:
* Originally, a feature was intended to create a text string from an input image, however this was impractical to implement.
Rather, two functions were created to develop Ascii Art from the image, the more rudimentary using 8 values, the more
condensed using 36 values.
    *Note that the Ascii options are mainly for MAC users only  
    
Division of Labor:

* J:
  * All functions in create.py and implementations in PixelArtGUI.py
    * All functions are original code, Ascii values found using ord() and https://en.wikipedia.org/wiki/Block_Elements
  * Minor edits on GUI visualizations: word_search visualizations, search_image visualizations
    * Visual update on search_word: frame/label edits, beautification
    * Frame/picture formatting in search_image, image updating / button functionality
  
  
* Betty:
  * All functions for the web scraper in download_images.py
    * I followed and try to extract google_images_download.py to see how they got their images from Google since this library didn't work unless it ran for a couple of hours. 
      --> https://github.com/hardikvasa/google-images-download/blob/master/google_images_download/google_images_download.py
    * I also referenced some StackOverflow discussions:
       --> https://stackoverflow.com/questions/20716842/python-download-images-from-google-image-search
  * GUI implementation and visualization
    * Built the skeleton of all 3 windows in the GUI 
    * I created the main window in the GUI using tkinter's widgets and functionalities
    * I also created and provided functionality for the tkinter window when searching for a word

Rainie:


-----------------------------------------------------------------------------------------------------------------

Milestone 2:
Project function: a GUI that procedurally generates images from text, thus every string of text would generate a unique picture. 
To get these images to map to text, we will be creating what is most similar to a hashtable in Python. Betty will be doing so and attempting to build/imitate a database that will hold these mapped texts and images. 
J is responsible for the algorithms/functions associated with the user input, as well as the overall functionality of what exactly is supposed to appear when a word(s) or image(s) is searched. 
Rainie is in charge of the overall design and look of our GUI. Basically, she will create the layout and blueprint of the GUI, making it aesthetically pleasing for our users. 
We have been brainstorming and working on paper and white board, trying to visualize what exactly we want this to look like, rather than writing actual code for it yet. But it is soon to come!

Milestone 3:
J Bujarski: 
  * The best way to determine the generated picture from the input text would be a web scraper.
    * Pictures can be searched for from Google, and pixel-by-pixel broken down to determine what an "average" picture would be.
    * Libraries to include: requests, BeautifulSoup
  * Picture data can be stored in a 2d array, with ratios created for the downloaded pictures
    * Thus, smaller pictures are spread out to cover as many pixels as larger pictures
    * Average RGB values per pixel stored in an element
    * Overall picture updated on completion of a picture being added.
    * User can input the number of images to use for the "Average" creation
      * Multiprocessing can be used to process several images at once.
    * Libraries to include: pandas, matplotlib, multiprocessing, flask (!!!)
    
    
Betty Tannuzzo:
  * Along with keeping the images in a 2D array, we can map certain images to words. 
    * Perhaps we can do this by creating a dictionary with the words being searched as keys and the urls for images as values
    * One downside to this is that we would have to limit the amount of words searched due to it being pretty impossible to have every 
      word from the dictionary 
    * We should probably search Google for it (as J mentioned above) and somehow save that image url to that specific word in the 
      database
  * Libraries to include: all the ones mentioned above
    * plus 
      * os, xgoogle, re, urllib, GeoIP, sys
      
 Rainie Dormanen:
  * We might also need to actually process the images to be used to develop the new images
  * There are also pre-existing libraries that allow webscraping of Google, and Bing, etc... that might be of use to us for 
  finding and saving images and their URLs into our Python Code
    Libraries to include (potentially) :scikit-image, google_images_search, image_search, OpenCV
