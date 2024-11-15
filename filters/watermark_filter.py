#---------------------------------
# Author: Omar S. Gómez
# Date: March 2024
# Description: Software filter that add a watermark text over an image
#---------------------------------
from PIL import Image, ImageDraw, ImageFont

def watermark(img, txt, txt_size):
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", txt_size)
    draw.text((5, 5), txt, fill=(255, 255, 255), font=font)
    return img


