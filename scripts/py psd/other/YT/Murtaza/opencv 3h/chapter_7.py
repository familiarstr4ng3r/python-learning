import cv2
import numpy as np
import image_stacker

## Color Detection

def emptyCallback(value):
    pass

def create_window(windowName):
    cv2.namedWindow(windowName)
    cv2.resizeWindow(windowName, 300, 300)
    cv2.createTrackbar('hue min', windowName, 0, 179, emptyCallback)
    cv2.createTrackbar('hue max', windowName, 179, 179, emptyCallback)
    cv2.createTrackbar('sat min', windowName, 0, 255, emptyCallback)
    cv2.createTrackbar('sat max', windowName, 255, 255, emptyCallback)
    cv2.createTrackbar('val min', windowName, 0, 255, emptyCallback)
    cv2.createTrackbar('val max', windowName, 255, 255, emptyCallback)

def handle_image(image):

    name = 'settings'
    create_window(name)

    while True:
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        h_min = cv2.getTrackbarPos('hue min', name)
        h_max = cv2.getTrackbarPos('hue max', name)
        s_min = cv2.getTrackbarPos('sat min', name)
        s_max = cv2.getTrackbarPos('sat max', name)
        v_min = cv2.getTrackbarPos('val min', name)
        v_max = cv2.getTrackbarPos('val max', name)

        lower = np.array([h_min, s_min, v_min])
        upper = np.array([h_max, s_max, v_max])
        mask = cv2.inRange(hsv, lower, upper)
        result = cv2.bitwise_and(image, image, mask=mask)


        horizontal = image_stacker.stackImages(0.5, [[image, hsv], [mask, result]])
        
        #cv2.imshow('original', image)
        #cv2.imshow('hsv', hsv)
        #cv2.imshow('mask', mask)
        #cv2.imshow('result', result)

        cv2.imshow('horizontal', horizontal)

        key = cv2.waitKey(50)
        if key == ord('q'):
            break
    
    cv2.destroyAllWindows()

def read_image():
    image = cv2.imread('Resources/car-orange-20.jpg')
    if not image is None:
        handle_image(image)
    else:
        print('image not found')

def main():
    read_image()
    print('done')

if __name__ == '__main__':
    main()
