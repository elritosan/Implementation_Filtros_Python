#---------------------------------
# Author: Omar S. Gómez
# Date: March 2024
# Description: Software filter that applies a contrast factor given an image 
#---------------------------------

from PIL import ImageEnhance

def contrast(img, factor):
    enhancer = ImageEnhance.Contrast(img)
    image_with_contrast = enhancer.enhance(factor)
    return image_with_contrast
