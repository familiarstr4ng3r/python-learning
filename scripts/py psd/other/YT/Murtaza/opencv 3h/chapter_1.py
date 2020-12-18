import cv2

cap = cv2.VideoCapture('Resources/video.mp4')

while True:
    success, image = cap.read()
    if success:
        cv2.imshow('window', image)
        
        key = cv2.waitKey(10)
        if key == ord('q'):
            break
    else:
        print('not success')
        break

print('done')