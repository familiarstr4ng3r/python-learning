import json
import atlas_packer

def get_text(path):
    try:
        with open(path) as f:
            text = f.read()
    except IOError:
        return False, None, "[IOError]"
    else:
        return True, text, None


def handle_dict(dictionary):

    separator = "/"
    
    folders = dictionary["folders"]
    save_path = dictionary["save_path"]
    base_path = dictionary["base_path"]

    for folder in folders:
        path = separator.join([base_path, folder["path"]])
        images = atlas_packer.get_images(path)

        grid = folder["grid"]
        pivot = folder["pivot"]
        #div = folder["divisibility"]
        same_size = folder["same_size"]

        frame_size = None if same_size else atlas_packer.get_max_size(images)
        
        result = atlas_packer.pack_grid(images, grid, pivot = pivot, frame_size = frame_size)

        path = separator.join([save_path, folder["filename"]])
        result.save(path)
        
        #result = atlas_packer.draw_rects(result, grid)
        #atlas_packer.show(result)


def main():

    path = "Resources/prehistoric.json"

    if path is None: path = input("Enter path to json: ")

    success, text, error = get_text(path)

    if success:
        dictionary = json.loads(text)
        #print(dictionary)
        handle_dict(dictionary)
    else:
        print(error)


if __name__ == "__main__":
    main()






