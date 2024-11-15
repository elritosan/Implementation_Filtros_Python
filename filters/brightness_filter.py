#---------------------------------
# Author: Omar S. Gómez
# Date: March 2024
# Description: Software filter that applies a brightness factor given an image 
#---------------------------------

from PIL import ImageEnhance

def brightness(img, factor):
    enhancer = ImageEnhance.Brightness(img)
    new_image = enhancer.enhance(factor) 
    return new_image
