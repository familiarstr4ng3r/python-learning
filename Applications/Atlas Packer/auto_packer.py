import os
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
    folders = dictionary["folders"]
    save_path = dictionary["save_path"]

    for folder in folders:
        images = atlas_packer.get_images(folder["path"])
        x, y = folder["grid_x"], folder["grid_y"]
        div = folder["divisibility"]
        result = atlas_packer.pack_grid(images, x, y)
        #atlas_packer.show(result, 0.2)

        path = os.path.join(save_path, folder["filename"])
        result.save(result, path)
        #print(path)


def main():

    path = "resources/prehistoric/trees.json"

    if path is None: path = input("Enter path to json: ")

    success, text, error = get_text(path)

    if success:
        dictionary = json.loads(text)
        print(dictionary)
        #handle_dict(dictionary)
    else:
        print(error)
        main()


if __name__ == "__main__":
    main()






