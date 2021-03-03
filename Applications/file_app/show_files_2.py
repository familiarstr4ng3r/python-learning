import os
import json
import datetime

def save_filepaths(files):
    with open("files.txt", "w") as f:
        lines = map(lambda x: x + "\n", files)
        f.writelines(lines)

def get_files(directory):
    stored_files = []

    for root, dirs, files in os.walk(directory):
        for filename in files:
            abs_path = os.path.join(root, filename)
            abs_path = abs_path.replace("\\", "/")

            file_object = {
                "path": abs_path,
                "size": os.path.getsize(abs_path),
                "m_time": int(os.path.getmtime(abs_path))
            }

            stored_files.append(file_object)
            if len(stored_files) % 10000 == 0:
                print(len(stored_files))

    return stored_files

DIRECTORY = "F:/книги"
SAVE_NAME = DIRECTORY.split("/")[-1] + ".json"

files = get_files(DIRECTORY)

size = sum([f["size"] for f in files])

now = datetime.datetime.now()

result = {
    "directory": DIRECTORY,
    "total_size": size,
    "ts": int(now.timestamp()),
    "date": now.strftime("%Y/%m/%d %H:%M:%S"),
    "length": len(files),
    "files": files
}

with open(SAVE_NAME, "w", encoding = "utf-8") as f:
    text = json.dumps(result, ensure_ascii = False, indent = 2)
    f.write(text)
