#---------------------------------
# Author: Omar S. Gómez
# Date: March 2024
# Description: Software filter that flips an image from top to bottom 
#---------------------------------

from PIL import Image

def flip(img):
    hori_flippedImage = img.transpose(Image.FLIP_TOP_BOTTOM)
    return hori_flippedImage
