import json

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

    for folder in folders[1:]:
        grid = folder["grid"]
        pivot = folder["pivot"]

        print(grid, type(grid))
        print(pivot, type(pivot))

        x, y = grid
        size = x, y
        print(type(size))

def main():
    path = "Resources/demo.json"

    success, text, error = get_text(path)

    if success:
        dictionary = json.loads(text)
        #print(dictionary)
        handle_dict(dictionary)
    else:
        print(error)


if __name__ == "__main__":
    main()
    print("Done")
