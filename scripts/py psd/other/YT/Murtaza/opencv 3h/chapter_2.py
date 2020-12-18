import cv2
import numpy as np

def handle_image(image):
    #cv2.imshow('original', image)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(image, (19,19), 0)
    canny = cv2.Canny(image, 100, 100)

    kernel = np.ones((5, 5), np.uint8)
    dilate = cv2.dilate(canny, kernel, iterations=1)
    erode = cv2.erode(dilate, kernel, iterations=1)

    #cv2.imshow('gray', gray)
    #cv2.imshow('blurred', blurred)
    cv2.imshow('canny', canny)
    cv2.imshow('dilate', dilate)
    cv2.imshow('erode', erode)

    cv2.waitKey(0)

def read_image():
    image = cv2.imread('Resources/data/lena.jpg')
    if not image is None:
        handle_image(image)
    else:
        print('image not found')

def main():
    read_image()
    print('done')

if __name__ == '__main__':
    main()