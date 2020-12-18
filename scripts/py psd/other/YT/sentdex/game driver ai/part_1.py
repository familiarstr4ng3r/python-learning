import numpy as np
import cv2
from PIL import ImageGrab
import time

import direct_keys as keys

#https://www.youtube.com/playlist?list=PLQVvvaa0QuDeETZEOy4VdocT7TOjfSA8a

last_time = time.time()

box = (0, 40, 800, 640)

def start_delay(seconds):
    collection = list(range(seconds))
    for i in collection[::-1]:
        print(i + 1)
        time.sleep(1)

start_delay(3)
print('Start')

#keys.PressKey(keys.W)
#time.sleep(3)
#keys.ReleaseKey(keys.W)
quit()

vertices = np.array([[10, 500],
                    [10, 300],
                    [300, 200],
                    [500, 200],
                    [800, 300],
                    [800, 500]])

def roi(image, vertices):
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(image, mask)
    return masked

def printSeconds():
    global last_time
    t = time.time() - last_time
    print('Loop {} seconds'.format(t))
    last_time = time.time()

def process_image(original_image):
    processed_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    processed_image = cv2.Canny(processed_image, threshold1 = 200, threshold2 = 300)

    global vertices
    processed_image = roi(processed_image, [vertices])
    
    return processed_image

while True:
    #printSeconds()
    screen = np.array(ImageGrab.grab(box))
    new_screen = process_image(screen)
    
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)

    cv2.imshow('window', new_screen)
    #cv2.imshow('window original', screen)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break


print('done')

