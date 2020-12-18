import cv2
import numpy as np

# cv2.IMREAD_COLOR = 1
# cv2.IMREAD_GRAYSCALE = 0
# cv2.IMREAD_UNCHANGED = -1

blue_color = (255, 0, 0)
green_color = (0, 255, 0)
red_color = (0, 0, 255)

def process_image(image):
    image = cv2.line(image, (0, 0), (100, 100), red_color, 2)
    image = cv2.arrowedLine(image, (200, 200), (300, 300), green_color, 2)
    image = cv2.rectangle(image, (10, 10), (110, 110), blue_color, 2)
    image = cv2.rectangle(image, (500, 100), (600, 200), green_color, -1)
    image = cv2.circle(image, (300, 300), 100, red_color, 2)

    font = cv2.FONT_HERSHEY_SIMPLEX
    image = cv2.putText(image, 'Hello World', (100, 100), font, 1, blue_color, 2, cv2.LINE_AA)
    
    return image

def handle_image(image):

    image = process_image(image)

    cv2.imshow('window', image)
    
    key = cv2.waitKey(0) & 0xFF
    if key == ord('q') or key == 27:
        print('quitting')

    cv2.destroyAllWindows()

def read_image():
    image = cv2.imread('resources/image.jpg', 1)
    #image = np.zeros([600, 800, 3], np.uint8) # [h, w, channels?] # black image

    if not image is None:
        handle_image(image)
    else:
        print('image not found')

def main():
    read_image()
    print('done')

if __name__ == '__main__':
    main()
