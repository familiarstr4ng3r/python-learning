import cv2
import numpy as np
from PIL import ImageGrab

## Contours / Shape Detection
# py chapter_9.py

red_color = (0, 0, 255)
blue_color = (255, 0, 0)

def resize_image(image, scale_factor):
    h, w, c = image.shape # tuple(rows, colums, channels)
    resized = cv2.resize(image, (int(w * scale_factor), int(h * scale_factor)))
    return resized

def recognize_face(image, face_cascade, eye_cascade):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    #print(len(faces))

    for (x,y,w,h) in faces:
        p1 = (x, y)
        p2 = (x + w, y + h)
        cv2.rectangle(image, p1, p2, red_color, 2)

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = image[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            e_p1 = (ex,ey)
            e_p2 = (ex+ew,ey+eh)
            cv2.rectangle(roi_color, e_p1, e_p2, blue_color, 2)


def handle_image(image):
    
    face_cascade = cv2.CascadeClassifier('Resources/haarcascades/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('Resources/haarcascades/haarcascade_eye.xml')
    
    window_name = 'window'
    cv2.namedWindow(window_name)
    #https://docs.opencv.org/3.4/d7/dfc/group__highgui.html
    cv2.setWindowProperty(window_name, cv2.WND_PROP_TOPMOST, cv2.WINDOW_FULLSCREEN)
    #topmost = cv2.getWindowProperty(window_name, cv2.WND_PROP_TOPMOST)
    #print(topmost)
    #quit()

    box = (500, 0, 1350, 750)
    while True:
        ## captured in BGR by default
        screen = np.array(ImageGrab.grab(box))

        ## inside converted from BGR to GRAY, from GRAY recognized faces and eyes
        ## drawing to original BGR
        recognize_face(screen, face_cascade, eye_cascade)
        
        ## converting to human-normal image
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
        screen = resize_image(screen, 0.5)
        
        cv2.imshow(window_name, screen)
        
        key = cv2.waitKey(20)
        if key == ord('q'):
            break
    
    #cv2.imshow('original', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

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
