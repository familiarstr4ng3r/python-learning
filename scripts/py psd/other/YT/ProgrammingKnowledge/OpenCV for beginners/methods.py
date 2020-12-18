import cv2

# cv2.IMREAD_COLOR = 1
# cv2.IMREAD_GRAYSCALE = 0
# cv2.IMREAD_UNCHANGED = -1

# roi : region of interest

def handle_image(image):
    print(image.shape) # tuple(rows, colums, channels)
    print(image.size) # total number of pixels
    print(image.dtype) # image databype is obtained

    b, g, r = cv2.split(image)
    image = cv2.merge((b, g, r))
    
    cv2.imshow('window', image)
    key = cv2.waitKey(0) & 0xFF

    if key == ord('q') or key == 27:
        print('quitting')

    cv2.destroyAllWindows()

def read_image():
    image = cv2.imread('resources/image.jpg', 1)
    if not image is None:
        handle_image(image)
    else:
        print('image not found')

def main():
    read_image()

if __name__ == '__main__':
    main()
