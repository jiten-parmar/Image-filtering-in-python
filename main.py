import cv2
from tkinter import *
import numpy as np
import scipy.interpolate
from tkinter.filedialog import askopenfilename
from PIL import ImageTk,Image

root = Tk()
root.geometry('1200x700')
root.title('Image Editor')


def fileOpen():
    Tk().withdraw()
    filename = askopenfilename()
    return filename


filename = fileOpen()
image1 = cv2.imread(filename)

myImage = ImageTk.PhotoImage(Image.open(filename))
myLabel = Label(image=myImage)
#myLabel.grid(row=4, column=0, columnspan=13)

def Scale():
    global image1
    image = image1

    width = 1280
    height = 720

    # dsize
    dsize = (width, height)

    # resize image
    output0 = cv2.resize(image, dsize)

    scale_percent = int(e.get())

    # calculate the 50 percent of original dimensions
    width = int(output0.shape[1] * scale_percent / 100)
    height = int(output0.shape[0] * scale_percent / 100)

    # dsize
    dsize = (width, height)

    # resize image
    output = cv2.resize(output0, dsize)

    cv2.imshow("output", output)
    cv2.waitKey(0)




def Abs_BandW():
    global image1
    image = image1
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    r, image = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY)

    width = 1280
    height = 720

    # dsize
    dsize = (width, height)

    # resize image
    output = cv2.resize(image, dsize)

    cv2.imshow("output", output)
    cv2.waitKey(0)

def blackAndWhite():
    global image1
    image = image1
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    width = 1280
    height = 720

    # dsize
    dsize = (width, height)

    # resize image
    output = cv2.resize(image, dsize)

    cv2.imshow("output", output)
    cv2.waitKey(0)


def gaussianBlur():
    global image1
    image = image1
    x = cv2.GaussianBlur(image, (35, 35), 0)
    width = 1280
    height = 720

    # dsize
    dsize = (width, height)

    # resize image
    output = cv2.resize(x, dsize)
    cv2.imshow("output", output)
    cv2.waitKey(0)

def sharpen():
    global image1
    image = image1
    kernel = np.array([[-1, -1, -1],
                       [-1, 9, -1],
                       [-1, -1, -1]])
    x = cv2.filter2D(image, -1, kernel)
    width = 1280
    height = 720

    # dsize
    dsize = (width, height)

    # resize image
    output = cv2.resize(x, dsize)
    cv2.imshow("output", output)
    cv2.waitKey(0)


def sepia():
    global image1
    image = image1
    kernel = np.array([[0.272, 0.534, 0.131],
                       [0.349, 0.686, 0.168],
                       [0.393, 0.769, 0.189]])

    x = cv2.filter2D(image, -1, kernel)
    width = 1280
    height = 720

    # dsize
    dsize = (width, height)

    # resize image
    output = cv2.resize(x, dsize)
    cv2.imshow("output",output)
    cv2.waitKey(0)


def emboss():
    global image1
    image = image1
    kernel = np.array([[0,-1,-1],
                        [1,0,-1],
                        [1,1,0]])
    x = cv2.filter2D(image, -1, kernel)
    width = 1280
    height = 720

    # dsize
    dsize = (width, height)

    # resize image
    output = cv2.resize(x, dsize)
    cv2.imshow("output", output)
    cv2.waitKey(0)


def brightnessControl():
    global image1
    image = image1
    brightness = int(e.get())
    x = cv2.convertScaleAbs(image, beta=brightness)
    width = 1280
    height = 720

    # dsize
    dsize = (width, height)

    # resize image
    output = cv2.resize(x, dsize)
    cv2.imshow("output", output)
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
    width = 1280
    height = 720

    # dsize
    dsize = (width, height)

    # resize image
    output = cv2.resize(x, dsize)
    cv2.imshow("output", output)
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
    width = 1280
    height = 720

    # dsize
    dsize = (width, height)

    # resize image
    output = cv2.resize(x, dsize)
    cv2.imshow("output", output)
    cv2.waitKey(0)


e = Entry(root, width=10, borderwidth=5)
e.grid(row=3, column=2, padx=10, pady=10)
sepiaButton = Button(root, text="sepia",width=30, height=3,font=28, padx=40, pady=20,  command=lambda: sepia()).grid(row=0,column=0)
blurButton = Button(root, text="blur",width=30, height=3,font=28,padx=40, pady=20, command=gaussianBlur).grid(row=0,column=2)
embossButton = Button(root, text="emboss",width=30, height=3,font=28,padx=40, pady=20, command=emboss).grid(row=0,column=3)
sharpButton = Button(root, text="sharp",width=30, height=3,font=28,padx=40, pady=20, command=sharpen).grid(row=1,column=0)
brightButton = Button(root, text="bright",width=30, height=3,font=28,padx=40, pady=20, command=brightnessControl).grid(row=2,column=2)
coldButton = Button(root, text="cold",width=30, height=3,font=28,padx=40, pady=20, command=coldImage).grid(row=1,column=2)
Warmbutton = Button(root, text="warm",width=30, height=3,font=28,padx=40, pady=20, command=warmImage).grid(row=1,column=3)
PureBandW_button = Button(root, text="pure B & W",width=30, height=3,font=28,padx=40, pady=20, command=Abs_BandW).grid(row=2,column=0)
blackAndWhiteButton = Button(root, text="B & W",width=30, height=3,font=28,padx=40, pady=20, command=blackAndWhite).grid(row=2,column=3)
scaleButton = Button(root, text="Scale",width=30, height=3,font=28, padx=40, pady=20,  command=Scale).grid(row=3,column=0)

button_Exit = Button(root, text="Exit", command=root.quit).grid(row=5,column=3)


#cv2.imshow("output",coldimage)
#cv2.waitKey(0)



root.mainloop()