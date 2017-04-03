__author__ = 'Ben Covey, Brandon Christen, Alex Cochrane'
from PIL import Image
import matplotlib.pyplot as plt
from numpy import array
from skimage import data
from SimpleCV import Image, Camera

cam = Camera()
img = cam.getImage()

rgb_im = img.convert('RGB')
pixel_array = []
# if(r == 181 or g == 230 or b == 29):
# Try is in place in case we get a issue with indexing, say photo sizing.
try:
    # Range is currently 1/8 of the image, so we are multiplying all the xy by 8 to allow for scaling
    # We are scaling to allow this program to preform
    for x in range(50):
        for y in range(50):
            r, g, b = rgb_im.getpixel((x*8, y*8))
            # I am using that maybe RGB values to allow lightning tolerances. I was thinking of making those into a
            # single array, then comparing that array to the rbg values. Or Switch statement
            if(r in range(175, 186)):
                if(g in range(225, 235)):
                    if(b in range(24, 35)):
                        pixel_array.append('%d,%d' % (x*8, y*8))
                        print('%d,%d' % (x*8, y*8))
                        print(r, g, b)
finally:
    print(len(pixel_array))
    print(pixel_array)
    print("End of range")
