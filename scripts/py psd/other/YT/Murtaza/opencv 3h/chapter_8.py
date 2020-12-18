import cv2
import numpy as np
import image_stacker

## Contours / Shape Detection

blue_color = (255, 0, 0)
green_color = (0, 255, 0)
red_color = (0, 0, 255)
magenta_color = (255, 0, 255)
black_color = (0, 0, 0)

def recognize_shape(point_count, aspect):
    text, color = 'None', magenta_color
    
    if point_count == 4:
        square = aspect > 0.9 and aspect < 1.1
        text = 'Square' if square else 'Rect'
        color = blue_color
    elif point_count == 3:
        text = 'Triangle'
        color = green_color
    elif point_count > 4:
        text = 'Circle'
        color = red_color
    
    return text, color

def get_contours(image, imageToWrite):
    contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        #area = cv2.contourArea(c)
        #cv2.drawContours(imageToWrite, c, -1, red_color, 3)
        
        perimeter = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.03 * perimeter, True)
        x, y, w, h = cv2.boundingRect(approx)

        point_count = len(approx)
        aspect = w/h
        text, color = recognize_shape(point_count, aspect)
        p1 = (x, y)
        p2 = (x + w, y + h)
        center = (x + (w//2), y + (h//2))

        cv2.rectangle(imageToWrite, p1, p2, color, 2)
        cv2.putText(imageToWrite, text, p1, cv2.FONT_HERSHEY_COMPLEX, 1, black_color, 1)

def handle_image(image):
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(gray, 100, 100)
    blank = np.zeros_like(image)
    contour_image = image.copy()

    get_contours(canny, contour_image)
    
    #cv2.imshow('original', image)
    #cv2.imshow('gray', gray)
    #cv2.imshow('canny', canny)
    cv2.imshow('contour', contour_image)

    #stack = image_stacker.stackImages(0.7, [[image, gray, canny], [blank, contour_image, contour_image]])
    #cv2.imshow('stack', stack)

    cv2.waitKey(0)    
    cv2.destroyAllWindows()

def read_image():
    image = cv2.imread('Resources/shapes-color.png')
    if not image is None:
        handle_image(image)
    else:
        print('image not found')

def main():
    read_image()
    print('done')

if __name__ == '__main__':
    main()
