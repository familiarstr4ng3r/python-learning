import cv2
from datetime import datetime

def process_image(image):
    text = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    font = cv2.FONT_HERSHEY_SIMPLEX
    scale = 1
    white_color = (255, 255, 255)
    thickness = 2
    image = cv2.putText(image, text, (10, 50), font, scale, white_color, thickness)
    return image

def get_cap_size(cap):
    w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    w = int(w)
    h = int(h)
    return (w, h)

def read_camera():
    cap = cv2.VideoCapture(0)

    size = get_cap_size(cap)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video_writer = cv2.VideoWriter('resources/saved.avi', fourcc, 20.0, size)
    
    while True:
        available, frame = cap.read()

        if available:
            #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            frame = process_image(frame)
            video_writer.write(frame)
            cv2.imshow('window', frame)

            key = cv2.waitKey(50) & 0xFF
            if key == ord('q'):
                break
        else:
            print('not available')
            break

    cap.release()
    video_writer.release()
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


