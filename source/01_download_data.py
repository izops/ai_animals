# %%
import os
import fastcore.all as fca
import fastai.vision.all as fva

from fastdownload import download_url
from duckduckgo_search import DDGS

#%%
# Define main path
path = '/data'

# %%
# Define functions

def search_images(keywords, max_images = 30):
    """Look for images on web using duckduckgo search.
    
    Inputs:
        - keywords - string keyword to search
        - max_images - integer number of images to look for

    Output:
        - list of
    """
    # Inform user about the process start
    print(f"Searching for {keywords}")

    # Return the list of URLs with the search results
    return fca.L(DDGS().images(keywords)).itemgot('image')

#%%
urls = search_images('bird photos', max_images=1)
