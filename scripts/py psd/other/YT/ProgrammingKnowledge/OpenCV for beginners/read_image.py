import cv2

# cv2.IMREAD_COLOR = 1
# cv2.IMREAD_GRAYSCALE = 0
# cv2.IMREAD_UNCHANGED = -1

image = cv2.imread('resources/image.jpg', 0)

if not image is None:
    cv2.imshow('window', image)
    key = cv2.waitKey(0) & 0xFF

    if key == ord('q') or key == 27:
        #27 - escape
        #cv2.imwrite('image-copy.jpg', image)
        print('saved')

    cv2.destroyAllWindows()
