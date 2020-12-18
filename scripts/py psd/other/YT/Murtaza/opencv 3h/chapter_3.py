import cv2
import numpy as np

def handle_image(image):
    h, w, c = image.shape # tuple(rows, colums, channels)
    resized = cv2.resize(image, (w // 2, h // 2))
    cropped = image[0:200, 0:300] # y, x : [bottom left, top right]

    cv2.imshow('original', image)
    cv2.imshow('resized', resized)
    cv2.imshow('cropped', cropped)

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

# https://www.youtube.com/watch?v=WQeoO7MI0Bs