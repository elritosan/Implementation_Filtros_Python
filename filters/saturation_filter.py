#---------------------------------
# Author: Omar S. Gómez
# Date: March 2024
# Description: Software filter that applies saturation over an image given a factor
#---------------------------------

from PIL import Image, ImageEnhance

def saturation(img, factor):
    enhancer = ImageEnhance.Color(img)
    saturated_image = enhancer.enhance(factor)
    return saturated_image

