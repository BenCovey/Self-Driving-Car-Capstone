__author__ = 'Ben Covey, Brandon Christen, Alex Cochrane'
from PIL import Image
from numpy import array
img = Image.open("input.png")
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
            if(r == 175 or r == 176 or r == 177 or r == 178 or r == 179 or r == 180 or r == 181 or r == 182 or r == 183 or r == 184 or r == 185):
                if(g == 225 or g == 226 or g == 227 or g == 228 or g == 229 or g == 230 or g == 231 or g == 232 or g == 233 or g == 234 or g == 234):
                    if(b == 24 or b == 25 or b == 26 or b == 27 or b == 28 or b == 29 or b == 30 or b == 31 or b == 32 or b == 33 or b == 34):
                        pixel_array.append('%d,%d' % (x*8, y*8))
                        print('%d,%d' % (x*8, y*8))
                        print(r, g, b)
finally:
    print(len(pixel_array))
    print(pixel_array)
    print("End of range")


