import cv2

green = (0, 255, 0)
red = (0, 0, 255)
white = (255, 255, 255)


point = (300, 200)
font = cv2.FONT_HERSHEY_SIMPLEX
scale = 1
thickness = 2

def centered_text(image, point, text, pivot):
    text_size = cv2.getTextSize(text, font, scale, thickness)[0]
    print("Text size: ", text_size)

    half_size = tuple(e // 2 for e in text_size)
    print("Half size: ", half_size)

    pivot_size = tuple([value*pivot[idx] for idx, value in enumerate(text_size)])
    pivot_size = tuple(int(e) for e in pivot_size)
    print("Pivot size: ", pivot_size)
    
    x = (point[0] - half_size[0])
    y = (point[1] + half_size[1])
    center_point = (x, y)
    #cv2.putText(image, text, center_point, font, scale, white, thickness)

    x = (point[0] - pivot_size[0])
    y = (point[1] + pivot_size[1])
    pivot_point = (x, y)
    cv2.putText(image, text, pivot_point, font, scale, white, thickness)
    
    # draw rectangle around text label
    offset = 10
    top_left = (x - offset, y - text_size[1] - offset)
    bottom_right = (x + text_size[0] + offset, y + offset)
    cv2.rectangle(image, top_left, bottom_right, white)

    # doesn't work
    #rect = (top_left, bottom_right)
    #cv2.rectangle(image, rect, white) 

def handle_image(image):

    draw_into = image.copy()
    
    cv2.circle(draw_into, point, 100, red, 2)
    cv2.circle(draw_into, point, 5, red, 2)
    
    centered_text(draw_into, point, "Hello World!", (0.5, 0.5))

    p2 = (50, 50)
    t = "Lorem ipsum dolor sit amet"
    centered_text(draw_into, point, t, (0, 1))

    
    #cv2.imshow("original", image)
    cv2.imshow("draw", draw_into)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def read_image():
    image = cv2.imread('lena.jpg')
    
    if not image is None:
        handle_image(image)
    else:
        print('image not found')

def main():
    read_image()
    print('done')

if __name__ == '__main__':
    main()
