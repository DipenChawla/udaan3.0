# import the necessary packages

import numpy as np
import argparse
import cv2
import matplotlib.pyplot as plt

"""
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help='path to input image file')
args = vars(ap.parse_args())
"""
def skewcorrection(img_path, show=False):
    # load the image from disk
    image = cv2.imread(img_path)

    #Resizing.
    W = 1000
    height, width, depth = image.shape
    imgScale = W/width
    newX, newY = image.shape[1]*imgScale, image.shape[0]*imgScale
    #image = cv2.resize(image,(1280,920)) # Because the image was too big.
    
    # convert the image to grayscale and flip the foreground
    # and background to ensure foreground is now "white" and 
    # the background is "black"
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.bitwise_not(gray)

    # threshold the image, setting all foreground pixels to 255
    # and all background pixels to 0
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # grab the (x, y) coordinates of all pixel values that 
    # are greater than zero, than use these coordinates to 
    # compute a rotated bounding box that contains all
    # coordinates

    coords = np.column_stack(np.where(thresh > 0))
    angle = cv2.minAreaRect(coords)[-1]

    # the `cv2.minAreaRect` function returns values in the 
    # range [-90, 0); as the rectangle rotates clockwise the returned 
    # angle trends to 0 -- in this special case we 
    # need to add 90 degrees to the angle
    if angle < -45:
        angle = -(90 + angle) 
    else:
        angle = -angle
        
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h),
        flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

    """
    cv2.putText(rotated, "Angle: {:.2f} degrees".format(angle),
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    """
                
    # show the output image


    print("[INFO] angle: {:.3f}".format(angle))
    cv2.imwrite(f'{img_path}', rotated)

    #image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    #Show the original and rotated images.
    if show:
        plt.imshow(cv2.resize(image, (int(newX), int(newY))))
        plt.show()
        plt.imshow(cv2.resize(rotated, (int(newX), int(newY))))
        plt.show()
    print(rotated.shape)
    """
    rotated = cv2.cvtColor(rotated, cv2.COLOR_RGB2GRAY)
    (thresh, im_bw) = cv2.threshold(rotated, 0, 1, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    cv2.imshow('original', image)
    print(skeletonize(im_bw).shape)
    cv2.imshow('rotated', skeletonize(im_bw))
    cv2.waitKey(0)  
    cv2.imwrite('image_no_skew.jpg', im_bw)
    """
    """
    import textract
    text = textract.process('image_no_skew.jpg', encoding='ascii', method='tesseract')
    print('<<---------------TEXERACT------------------>>')
    print(type(text))
    print(text)
    """
    
if __name__ == '__main__':
	# construct the argument parse and parse the arguments
	ap = argparse.ArgumentParser()
	ap.add_argument("-i", "--image", required=True,
					help='path to input image file')
	args = vars(ap.parse_args())
	skewcorrection(args['image'])
