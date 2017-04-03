import cv2
import time
import numpy
import sys
from . import controller
# Camera 0 is the integrated web cam on my netbook
camera_port = 0

# Number of frames to throw away while the camera adjusts to light levels
ramp_frames = 30
 
# Now we can initialize the camera capture object with the cv2.VideoCapture class.
# All it needs is the index to a camera port.
camera = cv2.VideoCapture(camera_port)

# constants
BLACK_THRESHOLD = 20 # red, blue, and green value less than this
POINT_THRESHOLD = 50 # percentage of any given point that is black


'''def go_straight():
    print("CONTINUE ON")


def turn_left():
    print("TURN LEFT")


def turn_right():
    print("TURN RIGHT")'''


def do_the_gray_thing(im):
    for x in range(300, 310):
        for y in range(325, 335):
            im[x, y] = 200
        for y in range(400, 410):
            im[x, y] = 200
        for y in range(475, 485):
            im[x, y] = 200
        for y in range(250, 260):
            im[x, y] = 200
        for y in range(175, 185):
            im[x, y] = 200

    for x in range(390, 400):
        for y in range(325, 335):
            im[x, y] = 200
        for y in range(400, 410):
            im[x, y] = 200
        for y in range(475, 485):
            im[x, y] = 200
        for y in range(250, 260):
            im[x, y] = 200
        for y in range(175, 185):
            im[x, y] = 200
    return im


def do_the_drive_thing(im):
    # point zero is top left, nine is bottom right. figure it out you dick. it's like a book.
    #
    #   p0  p1  p2  p3  p4
    #
    #   p5  p6  p7  p8  p9
    #
    p0 = 0
    p1 = 0
    p2 = 0
    p3 = 0
    p4 = 0
    p5 = 0
    p6 = 0
    p7 = 0
    p8 = 0
    p9 = 0
    # top row
    for y in range(300, 310):
        # top center
        for x in range(325, 335):
            r, g, b = im[x, y]
            if r < BLACK_THRESHOLD and b < BLACK_THRESHOLD and g < BLACK_THRESHOLD:
                p2 += 1
        # top middle right
        for x in range(400, 410):
            r, g, b = im[x, y]
            if r < BLACK_THRESHOLD and b < BLACK_THRESHOLD and g < BLACK_THRESHOLD:
                p3 += 1
        # top middle left
        for x in range(250, 260):
            r, g, b = im[x, y]
            if r < BLACK_THRESHOLD and b < BLACK_THRESHOLD and g < BLACK_THRESHOLD:
                p1 += 1
        # top right
        for x in range(475, 485):
            r, g, b = im[x, y]
            if r < BLACK_THRESHOLD and b < BLACK_THRESHOLD and g < BLACK_THRESHOLD:
                p4 += 1
        # top left
        for x in range(175, 185):
            r, g, b = im[x, y]
            if r < BLACK_THRESHOLD and b < BLACK_THRESHOLD and g < BLACK_THRESHOLD:
                p0 += 1

    #bottom row
    for y in range(390, 400):
        # bottom middle
        for x in range(325, 335):
            r, g, b = im[x, y]
            if r < BLACK_THRESHOLD and b < BLACK_THRESHOLD and g < BLACK_THRESHOLD:
                p7 += 1
        # bottom middle right
        for x in range(400, 410):
            r, g, b = im[x, y]
            if r < BLACK_THRESHOLD and b < BLACK_THRESHOLD and g < BLACK_THRESHOLD:
                p8 += 1
        # bottom middle left
        for x in range(250, 260):
            r, g, b = im[x, y]
            if r < BLACK_THRESHOLD and b < BLACK_THRESHOLD and g < BLACK_THRESHOLD:
                p6 += 1
        # bottom right
        for x in range(475, 485):
            r, g, b = im[x, y]
            if r < BLACK_THRESHOLD and b < BLACK_THRESHOLD and g < BLACK_THRESHOLD:
                p9 += 1
        # bottom left
        for x in range(175, 185):
            r, g, b = im[x, y]
            if r < BLACK_THRESHOLD and b < BLACK_THRESHOLD and g < BLACK_THRESHOLD:
                p5 += 1

    if p2 > POINT_THRESHOLD or p7 > POINT_THRESHOLD:
        go_straight()
    elif (p0 > POINT_THRESHOLD and p1 > POINT_THRESHOLD) or \
            (p1 > POINT_THRESHOLD and p5 > POINT_THRESHOLD) or \
            (p5 > POINT_THRESHOLD and p6 > POINT_THRESHOLD) or \
            (p6 > POINT_THRESHOLD and p0 > POINT_THRESHOLD):
        turn_left()
    elif (p3 > POINT_THRESHOLD and p4 > POINT_THRESHOLD) or \
            (p4 > POINT_THRESHOLD and p8 > POINT_THRESHOLD) or \
            (p8 > POINT_THRESHOLD and p9 > POINT_THRESHOLD) or \
            (p9 > POINT_THRESHOLD and p4 > POINT_THRESHOLD):
        turn_right()


# Captures a single image from the camera and returns it in PIL format
def get_image():
    # read is the easiest way to get a full image out of a VideoCapture object.
    retval, im = camera.read()
    return im
 
# Ramp the camera - these frames will be discarded and are only used to allow v4l2
# to adjust light levels, if necessary
for i in xrange(ramp_frames):
    temp = get_image()
while True:
    try:
        # Take the actual image we want to keep
        camera_capture = get_image()
        f = "test_image.png"
        
        # A nice feature of the imwrite method is that it will automatically choose the
        # correct format based on the file extension you provide. Convenient!
        # cv2.imwrite(f, camera_capture)
         
        # You'll want to release the camera, otherwise you won't be able to create a new
        # capture object until your script exits
        # del(camera)
        im = camera_capture
        print(im.shape)
        height, width, channel = im.shape
        # cv2.imshow('image color', im)
        # im2 = im
        # cv2.imshow('image', im)
        ifilter = 170
        im[im >= ifilter] = 255
        im[im < ifilter] = 0
        print(im[395,330])

        # do the other thing here
        do_the_drive_thing(im)
        im = do_the_gray_thing(im)

        # im.save("/home/pi/Desktop/filteredimg.jpeg")
        from PIL import Image
        img = Image.fromarray(im)
        # path is relative because a macbook isn't a pi
        # img.save("filteredimg.jpeg")
        cv2.imshow('image color removal', im)
        
        # time.sleep(5)
        key = cv2.waitKey(5)
        if key != -1:
            cv2.destroyAllWindows()
            exit(0)
        else:
            cv2.destroyAllWindows()

    except:
        import webbrowser
        e = sys.exc_info()[0]
        url = "http://stackoverflow.com/search?q=[python]+" + e
        webbrowser.open(url, 2)
        exit(0)
