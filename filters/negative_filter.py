#---------------------------------
# Author: Omar S. Gómez
# Date: March 2024
# Description: Software filter that inverts the colors (color-reversed) of an image 
#---------------------------------

from PIL import ImageOps 

def negative(img):
    inverted_image = ImageOps.invert(img)
    return inverted_image
