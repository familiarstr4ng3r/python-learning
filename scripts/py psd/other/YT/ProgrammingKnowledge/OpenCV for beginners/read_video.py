import cv2
from datetime import datetime
import time

#https://www.codingforentrepreneurs.com/blog/open-cv-python-change-video-resolution-or-scale
#VideoCapture("rtsp://username:password@ip-address")

def process_image(image, size):
    text = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    font = cv2.FONT_HERSHEY_SIMPLEX
    scale = 1
    white_color = (255, 255, 255)
    thickness = 2
    
    cv2.putText(image, text, (10, 50), font, scale, white_color, thickness)
    cv2.putText(image, str(size), (10, 100), font, scale, white_color, thickness)
    
    #return image

def set_cap_size(cap, resolution = 720):
    w = 16 * resolution / 9
    w = int(w)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, w)            # 3
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, resolution)  # 4

def get_cap_size(cap):
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    size = (width, height, fps)
    size = [int(e) for e in size]

    return size

def read_camera():

    t1 = time.time()
    print(t1)

    # 192.168.1.1
    
    index = "rtsp://192.168.1.64/0"
    #index = 0
    cap = cv2.VideoCapture(index)
    print("cap start")

    m = cap.get(cv2.CAP_PROP_MODE) # 0.0
    
    #set_cap_size(cap, 480)
    size = get_cap_size(cap)
    
    #fourcc = cv2.VideoWriter_fourcc(*'XVID')
    #video_writer = cv2.VideoWriter('resources/saved.avi', fourcc, 20.0, size)
    
    while True:
        available, frame = cap.read()

        if available:
            #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            process_image(frame, size)
            #video_writer.write(frame)
            cv2.imshow('window', frame)

            key = cv2.waitKey(50) & 0xFF
            if key == ord('q'):
                break
        else:
            print(time.time() - t1)
            print('not available')
            break

    cap.release()
    #video_writer.release()
    cv2.destroyAllWindows()

def read_video():
    cap = cv2.VideoCapture('resources/video.mp4')

    while (cap.isOpened()):
        
        available, frame = cap.read()

        #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        cv2.imshow('window', frame)

        key = cv2.waitKey(50) & 0xFF

        if key == ord('q'):
            break
    

    cap.release()
    cv2.destroyAllWindows()


def main():
    read_camera()
    #read_video()

if __name__ == '__main__':
    main()


