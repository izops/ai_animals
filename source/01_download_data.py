# %%
import os
import time
import fastcore.all as fca
import fastai.vision.all as fva

from fastdownload import download_url
from duckduckgo_search import DDGS

#%%
# Define main path
path = 'data/'

# %%
# Define functions

def search_images(keywords: str) -> fca.L:
    """Look for images on web using duckduckgo search.
    
    Inputs:
        - keywords - string keyword to search
        - max_images - integer number of images to look for

    Output:
        - list of urls with the search results
    """
    # Inform user about the process start
    print(f"Searching for {keywords}")

    # Return the list of URLs with the search results
    return fca.L(DDGS().images(keywords)).itemgot('image')

def download_images(urls: fca.L, path: str, keyword: str) -> None:
    """Download images from url to a set path.
    
    Inputs:
        - urls - list of web addresses of objects to be downloaded
        - path - path to save the file

    Outputs:
        - none
    """

    # Create data folder if needed
    if os.path.exists(os.path.join(path, keyword)):
        destination = path
    else:
        destination = os.path.join(path, keyword)

        # Create new directory
        os.mkdir(destination)

    for i, url in enumerate(urls):
        # Create file name
        file_name = os.path.join(destination, keyword + str(i) + '.jpg')

        print(file_name)

        # Attempt to download the image, wait and skip if error occurs
        try:
            download_url(
                url,
                file_name,
                show_progress=False
            )
        except:
            time.sleep(1)
            pass

#%%
keyword = 'horse'
urls = search_images(keyword)
download_images(urls, path, keyword)
