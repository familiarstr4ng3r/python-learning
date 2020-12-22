import os
import math
import time

from PIL import Image
import numpy as np
import cv2

# Example usage:
# Horizontal is not finished
#image = get_horizontal_stack(images)
#image = get_horizontal_padded(images, divisibility)

# Grid is finished
#image = pack_grid(images, 2, 2, divisibility, pivot)

def get_images(folder):
    images = []

    for root, dirs, files in os.walk(folder):

        for file in files:
            path = os.path.join(root, file)
            image = Image.open(path)
            images.append(image)

    return images


def get_horizontal_stack(images):
    grid_x, grid_y = (len(images), 1)

    image = images[0]
    w, h = image.size

    total_width = w * grid_x
    total_height = h * grid_y
    size = (total_width, total_height)
    
    background = Image.new("RGBA", size, 0)

    for i, image in enumerate(images):
        x = i * w
        background.paste(image, (x, 0))

    return background


def get_horizontal_padded(images, divisibility = None):
    grid_x, grid_y = (len(images), 1)

    image = images[0]
    w, h = image.size

    if not divisibility is None:
        frame_w = divisibility * math.ceil(w / divisibility)
        frame_h = divisibility * math.ceil(h / divisibility)
    else:
        frame_w = w
        frame_h = h

    total_width = frame_w * grid_x
    total_height = frame_h * grid_y
    size = (total_width, total_height)

    background = Image.new("RGBA", size, 0)

    x_diff = (frame_w - w) // 2
    y_diff = (frame_h - h) // 2

    for i, image in enumerate(images):
        x = i * frame_w + x_diff
        y = 0 + y_diff
        background.paste(image, (x, y))

    return background


def pack_grid(images, grid, pivot = (0.5, 0.5), divisibility = None, frame_size = None):

    if frame_size is None:
        w, h = images[0].size
    else:
        w, h = frame_size
        
    if divisibility is None:
        frame_w, frame_h = w, h
    else:
        frame_w, frame_h = get_size_by_div(divisibility, (w, h))

    grid_x, grid_y = grid
    
    total_width = frame_w * grid_x
    total_height = frame_h * grid_y
    size = (total_width, total_height)
    
    background = Image.new("RGBA", size)

    # calculating here because of all images has same size
    #x_diff = (frame_w - w) * pivot[0]
    #y_diff = (frame_h - h) * (1 - pivot[1])
    
    #x_diff = int(x_diff)
    #y_diff = int(y_diff)

    for y in range(grid_y):
        for x in range(grid_x):

            index = y * grid_x + x
            if index >= len(images): continue
            image = images[index]

            # calculating here because each image has different size
            # need be here to calculate correct pivot
            x_diff, y_diff = get_difference(image, (frame_w, frame_h), pivot)
            x_pos = x * frame_w + x_diff
            y_pos = y * frame_h + y_diff
            
            pos = (x_pos, y_pos)
            background.paste(image, pos)

    return background


def get_difference(image, frame_size, pivot):
    w, h = image.size
    frame_w, frame_h = frame_size
    pivot_x, pivot_y = pivot
    
    x_diff = (frame_w - w) * pivot_x
    y_diff = (frame_h - h) * (1 - pivot_y)
    
    x_diff = int(x_diff)
    y_diff = int(y_diff)
    return x_diff, y_diff


def get_size_by_div(divisibility, size):
    w, h = size
    frame_w = divisibility * math.ceil(w / divisibility)
    frame_h = divisibility * math.ceil(h / divisibility)
    return frame_w, frame_h


def show(image, scaleFactor = 0.5):
    image = np.array(image)
    h, w, _ = image.shape
    h = int(h * scaleFactor)
    w = int(w * scaleFactor)
    
    image = cv2.resize(image, (w, h))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    cv2.imshow("result", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def draw_rects(image, grid_size):
    img = np.array(image)
    
    red = (255, 0, 0)
    grid_x, grid_y = grid_size

    total_w, total_h = image.size
    w, h = int(total_w / grid_x), int(total_h / grid_y)
    
    for y in range(grid_y):
        for x in range(grid_x):
            p1 = (x * w, y * h)
            p2 = (p1[0] + w, p1[1] + h)
            cv2.rectangle(img, p1, p2, red, 5)

    return img


def get_max_size(images):

    max_w, max_h = 0, 0
    images = [np.array(image) for image in images]

    for image in images:
        h, w, _ = image.shape
        if w > max_w: max_w = w
        if h > max_h: max_h = h

    return max_w, max_h


def main_packer():
    t1 = time.time()
    
    image_folder = r"C:\Users\User\Desktop\2D RUNNER\parts\Prehistoric\Parts\palm_4 down"
    
    images = get_images(image_folder)

    grid = (3, 2)
    pivot = (0.5, 0)
    divisibility = 100
    frame_size = get_max_size(images)
    
    image = pack_grid(images, grid, pivot, divisibility, frame_size)
    
    print("Packed:", time.time() - t1)

    #image.save("Resources/test.png")
    
    show_result = True

    if show_result:
        image = draw_rects(image, grid)
        show(image)


def main():
    main_packer()


if __name__ == "__main__":
    main()
    print("Done")



