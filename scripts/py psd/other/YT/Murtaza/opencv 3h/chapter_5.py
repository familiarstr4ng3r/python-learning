import cv2
import numpy as np

## Warp Perspective

def handle_image(image):
    width, height = 300, 500

    ## both arrays must be in the same order
    ## in this case: TOP-LEFT, TOP-RIGHT, BOTTOM-LEFT, BOTTOM-RIGHT
    pts1 = np.float32([[57, 65], [145, 60], [60, 175], [163, 166]])
    pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
    
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    transformed = cv2.warpPerspective(image, matrix, (width, height))

    cv2.imshow('original', image)
    cv2.imshow('transformed', transformed)

    cv2.waitKey(0)

def read_image():
    image = cv2.imread('Resources/warp-perspective.jpg')
    if not image is None:
        handle_image(image)
    else:
        print('image not found')

def main():
    read_image()
    print('done')

if __name__ == '__main__':
    main()
