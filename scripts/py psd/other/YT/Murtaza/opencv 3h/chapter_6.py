import cv2
import numpy as np

## Joining Images

## https://www.murtazahassan.com/courses/learn-opencv-in-3-hours/

def handle_image(image):

    ## images must have same channels

    h, w, c = image.shape # tuple(rows, colums, channels)
    resized = cv2.resize(image, (w // 2, h // 2))

    images = []
    for i in range(3):
        images.append(resized)

    horizontal = np.hstack(images)
    #vertical = np.vstack((image, image))

    #cv2.imshow('original', image)
    cv2.imshow('horizontal', horizontal)
    #cv2.imshow('vertical', vertical)

    #cv2.imwrite(f'horizontal {len(images)}.jpg', horizontal)

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
