import cv2
import numpy as np

#events = [i for i in dir(cv2) if 'EVENT' in i]
#print(events)

font = cv2.FONT_HERSHEY_SIMPLEX
white_color = (255, 255, 255)
scale = 0.5
thickness = 2

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        text = f'{x}:{y}'
        cv2.putText(image, text, (x, y), font, scale, white_color, thickness)
        cv2.imshow('window', image)
    elif event == cv2.EVENT_RBUTTONDOWN:
        b = image[y, x, 0]
        g = image[y, x, 1]
        r = image[y, x, 2]
        text = f'{b}:{g}:{r}'
        print(text)

def click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        b = image[y, x, 0]
        g = image[y, x, 1]
        r = image[y, x, 2]
        colored_image = np.zeros((200, 200, 3), np.uint8)
        colored_image[:] = [b, g, r]
        cv2.imshow('color', colored_image)

#image = np.zeros([300, 300, 3], np.uint8)
image = cv2.imread('resources/image.jpg', 1)
cv2.imshow('window', image)

cv2.setMouseCallback('window', click)

key = cv2.waitKey(0) & 0xFF
#if key == ord('q'):
cv2.destroyAllWindows()

print('done')
