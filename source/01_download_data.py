# %%
import os
import time
import fastcore.all as fca
import fastai.vision.all as fva
from PIL import Image

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
    return fca.L(DDGS().images(keywords + ' animal')).itemgot('image')

def download_images(urls: fca.L, path: str, keyword: str) -> None:
    """Download images from url to a set path.
    
    Inputs:
        - urls - list of web addresses of objects to be downloaded
        - path - path to save the file

    Outputs:
        - none
    """

    # Define target folder
    destination = os.path.join(path, keyword)

    # Create data folder if needed
    if not os.path.exists(destination):
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

        # Add waiting time
        time.sleep(3)

def resize_images(
    input_folder: str,
    output_folder: str,
    size=(400, 400)
) -> None:
    """Resize jpeg images in the input directory to the required size.
    The images are resized keeping their original aspect ratio. The extra space
    needed to fill the required size is padded with black pixels.

    Inputs:
        - input_folder - string containing path to the folder with images to
        resize
        - output_folder - string with target path where the resized images will
        be saved
        - size - tuple containing the required target size of images

    Outputs:
        - no returns, the resized images are saved in the output folder
    """
    # Create output folder if needed
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Resize all jpeg images in the source directory, remove corrupt files
    for filename in os.listdir(input_folder):
        if filename.endswith('.jpg') or filename.endswith('.jpeg'):
            # Obtain the full file name with path
            img_path = os.path.join(input_folder, filename)
            
            try:
                # Open the image, this will only work with valid files
                img = Image.open(img_path)

                # Resize and pad to make it square
                old_size = img.size
                ratio = float(size[0]) / max(old_size)
                new_size = tuple([int(x * ratio) for x in old_size])
                img = img.resize(new_size, Image.LANCZOS)  # Updated here

                # Create a new image and paste the resized image onto it
                new_img = Image.new("RGB", size)
                new_img.paste(img, ((size[0] - new_size[0]) // 2,
                                    (size[1] - new_size[1]) // 2))

                # Save the resized image
                new_img.save(os.path.join(output_folder, filename))

            except:
                # There was an error opening image, remove it
                os.remove(img_path)
#%%

# Define list of animals to download images of
keywords = [
    # 'horse', 'pig', 'domestic duck', 'hen', 'rooster', 'cat',
    # 'dog', 'goose', 'goat', 'sheep',
    'turkey', 'cow', 'bull',
    'dove', 'pigeon', 'duckling', 'donkey', 'rabbit'
]

# Bulk download the data
batch_download(keywords, path)

# %%

# Get all subdirectories for clean up
subfolders = os.listdir(path)

for subfolder in subfolders:
    # Create subfolder path
    sub_path = os.path.join(path, subfolder)

    # Resize images or remove corrupt ones in every subfolder
    resize_images(subfolder, subfolder)