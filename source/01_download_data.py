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
        file_name = os.path.join(
            destination,
            keyword + str(i) + '.jpg'
        )

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

def batch_download(keywords: list, path: str) -> None:
    """Set up image search and download for all provided keywords.
    
    Inputs:
        - keywords - list of all keywords to be sought and downloaded as image
        - path - folder path where all downloaded data should be stored

    Outputs:
        - the method does not return any object but it saves physical copies
        of found images of the keywords in data folder
    """

    for keyword in keywords:
        # Find images and save the urls
        urls = search_images(keyword)

        # Download the images to the disk
        download_images(urls, path, keyword)

#%%

# Define list of animals to download images of
keywords = [
    'horse', 'pig', 'domestic duck', 'hen', 'rooster', 'cat',
    'dog', 'goose', 'goat', 'sheep', 'turkey', 'cow', 'bull',
    'dove', 'pigeon', 'duckling', 'donkey', 'rabbit'
]

# Bulk download the data
batch_download(keywords, path)
