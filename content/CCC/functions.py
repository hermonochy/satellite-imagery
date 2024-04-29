from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# create some useful functions to use during this workshop
def convert(image):
    # open the original image, and show its filetype, colour mode and size
    original = Image.open(image)
    print("original:", original.format, original.mode, original.size)
    # the filetype should be JPEG or PNG; the colour mode should be RGB

    pixelMap = original.load()      #loading the pixel map of the image
    horizontal, vertical = original.size[0], original.size[1]   # name horizontal and vertical, to make next code clearer

    for i in range(horizontal):     # for every horizontal pixel
        for j in range(vertical):   # and every vertical pixel
            pixel = pixelMap[i,j]   # get the rgb value (r,g,b)
            r, g, b = pixel[0], pixel[1], pixel[2]          # name red, green, blue, to make next code clearer

            # check if r, g & b are similar in value (therefore grey)
            if (r in range (g-10, g+10) and b in range (g-10, g+10)):
                # if grey, reset to black (to make sure it show up properly in the next section)
                pixelMap[i,j] = (0, 0, 0)
    
    # convert into a numpy array containing all the pixels except the top 25 rows to cut off the header, and show its data type and shape
    np_img = np.asarray(original)
    np_img = np.delete(np_img, slice(0, 25), axis=0)
    np_img = np.delete(np_img, slice(-25, -1), axis=0)
    print("array: ", np_img.dtype, np_img.shape)
    # the data type should be uint8, the size should be 50 pixels smaller than the original in one dimension
        
    # convert into a luminosity plot by taking just the green values [1] and return as the function's output
    # the colour is determined by the brightness/depth of the pixel, ignoring whether it is red, green or blue
    # Note: this works for our images in NDVI format as they have been pre-processed in this way, you might get strange results using other images!
    lum_img = np_img[:, :, 1]
    return lum_img

def tidy_plot():
    '''
    this function removes the axes of the plots
    because they only show the size of the image, they can be misleading and are not needed for this workshop
    '''
    plt.xticks([])
    plt.yticks([])