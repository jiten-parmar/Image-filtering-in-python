import cv2
from tkinter import *
import numpy as np
import scipy.interpolate
import matplotlib.pyplot as plt
from tkinter.filedialog import askopenfilename


def fileOpen():
    Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
    return filename

root = Tk()
root.geometry('600x600')
filename = fileOpen()
image1 = cv2.imread(filename)



def dilation_erosion():
    global image1
    image = image1
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    r, image = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY)

    kernel = np.ones((5, 5), np.uint8)
    fig, ax = plt.subplots(1, figsize=(16, 12))

    m = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)
    ax = plt.subplot(236)
    plt.imshow(m, cmap='Greys')
    plt.title('dilation - erosion')
    plt.savefig('dila_ero.png', dpi=300, bbox_inches='tight')
    imagef = cv2.imread("dila_ero.png")
    cv2.imshow("output", image)
    cv2.waitKey(0)

def blackAndWhite():
    global image1
    image = image1
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("output", image)
    cv2.waitKey(0)


def gaussianBlur():
    global image1
    image = image1
    x = cv2.GaussianBlur(image, (35, 35), 0)
    cv2.imshow("output", x)
    cv2.waitKey(0)

def sharpen():
    global image1
    image = image1
    kernel = np.array([[-1, -1, -1],
                       [-1, 9, -1],
                       [-1, -1, -1]])
    x = cv2.filter2D(image, -1, kernel)
    cv2.imshow("output", x)
    cv2.waitKey(0)


def sepia():
    global image1
    image = image1
    kernel = np.array([[0.272, 0.534, 0.131],
                       [0.349, 0.686, 0.168],
                       [0.393, 0.769, 0.189]])

    x = cv2.filter2D(image, -1, kernel)
    cv2.imshow("output",x)
    cv2.waitKey(0)


def emboss():
    global image1
    image = image1
    kernel = np.array([[0,-1,-1],
                        [1,0,-1],
                        [1,1,0]])
    x = cv2.filter2D(image, -1, kernel)
    cv2.imshow("output", x)
    cv2.waitKey(0)


def brightnessControl():
    global image1
    image = image1
    x = cv2.convertScaleAbs(image, beta=150)
    cv2.imshow("output", x)
    cv2.waitKey(0)



def spreadLookupTable(x, y):
  spline = scipy.interpolate.UnivariateSpline(x, y)
  return spline(range(256))


def coldImage():
    global image1
    image = image1
    increaseLookupTable = spreadLookupTable([0, 64, 128, 256], [0, 80, 160, 256])
    decreaseLookupTable = spreadLookupTable([0, 64, 128, 256], [0, 50, 100, 256])
    red_channel, green_channel, blue_channel = cv2.split(image)
    red_channel = cv2.LUT(red_channel, increaseLookupTable).astype(np.uint8)
    blue_channel = cv2.LUT(blue_channel, decreaseLookupTable).astype(np.uint8)
    x = cv2.merge((red_channel, green_channel, blue_channel))
    cv2.imshow("output", x)
    cv2.waitKey(0)

def warmImage():
    global image1
    image = image1
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
dilation_erosion_button = Button(root, text="dil_eros", command=dilation_erosion).grid(row=2,column=0)
blackAndWhiteButton = Button(root, text="B & W", command=blackAndWhite).grid(row=2,column=2)




#cv2.imshow("output",coldimage)
#cv2.waitKey(0)



root.mainloop()