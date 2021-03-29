import cv2
from tkinter import *
import numpy as np
import scipy.interpolate

root = Tk()
root.geometry('600x600')

def gaussianBlur():
    image = cv2.imread("Resources/image2.jpg")
    x = cv2.GaussianBlur(image, (35, 35), 0)
    cv2.imshow("output", x)
    cv2.waitKey(0)

def sharpen():
    image = cv2.imread("Resources/image2.jpg")
    kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    x = cv2.filter2D(image, -1, kernel)
    crop_img = x[0:200, 0:200]
    cv2.imshow("output", crop_img)
    cv2.waitKey(0)


def sepia():
    initialImage = cv2.imread("Resources/image2.jpg")
    kernel = np.array([[0.272, 0.534, 0.131],
                       [0.349, 0.686, 0.168],
                       [0.393, 0.769, 0.189]])

    x = cv2.filter2D(initialImage, -1, kernel)
    cv2.imshow("output",x)
    cv2.waitKey(0)


def emboss():
    image = cv2.imread("Resources/image2.jpg")
    kernel = np.array([[0,-1,-1],
                            [1,0,-1],
                            [1,1,0]])
    x = cv2.filter2D(image, -1, kernel)
    cv2.imshow("output", x)
    cv2.waitKey(0)


def brightnessControl():
    image = cv2.imread("Resources/image2.jpg")
    x = cv2.convertScaleAbs(image, beta=150)
    cv2.imshow("output", x)
    cv2.waitKey(0)



def spreadLookupTable(x, y):
  spline = scipy.interpolate.UnivariateSpline(x, y)
  return spline(range(256))


def coldImage():
    image = cv2.imread("Resources/image2.jpg")
    increaseLookupTable = spreadLookupTable([0, 64, 128, 256], [0, 80, 160, 256])
    decreaseLookupTable = spreadLookupTable([0, 64, 128, 256], [0, 50, 100, 256])
    red_channel, green_channel, blue_channel = cv2.split(image)
    red_channel = cv2.LUT(red_channel, increaseLookupTable).astype(np.uint8)
    blue_channel = cv2.LUT(blue_channel, decreaseLookupTable).astype(np.uint8)
    x = cv2.merge((red_channel, green_channel, blue_channel))
    cv2.imshow("output", x)
    cv2.waitKey(0)

def warmImage():
    image = cv2.imread("Resources/image2.jpg")
    increaseLookupTable = spreadLookupTable([0, 64, 128, 256], [0, 80, 160, 256])
    decreaseLookupTable = spreadLookupTable([0, 64, 128, 256], [0, 50, 100, 256])
    red_channel, green_channel, blue_channel = cv2.split(image)
    red_channel = cv2.LUT(red_channel, decreaseLookupTable).astype(np.uint8)
    blue_channel = cv2.LUT(blue_channel, increaseLookupTable).astype(np.uint8)
    x = cv2.merge((red_channel, green_channel, blue_channel))
    cv2.imshow("output", x)
    cv2.waitKey(0)




sepiaButton = Button(root, text="sepia", command=sepia).grid(row=0,column=0)
blurButton = Button(root, text="blur", command=gaussianBlur).grid(row=0,column=1)
embossButton = Button(root, text="emboss", command=emboss).grid(row=0,column=2)
sharpButton = Button(root, text="sharp", command=sharpen).grid(row=1,column=0)
brightButton = Button(root, text="bright", command=brightnessControl).grid(row=2,column=1)
coldButton = Button(root, text="cold", command=coldImage).grid(row=1,column=1)
Warmbutton = Button(root, text="warm", command=warmImage).grid(row=1,column=2)





#cv2.imshow("output",coldimage)
#cv2.waitKey(0)



root.mainloop()