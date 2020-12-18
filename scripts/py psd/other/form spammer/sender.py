import requests
import json
import random

# 1
#https://docs.google.com/forms/d/1xf1QSqhw0wuhMnA7xMQyu_KAPtnF5dDhL3Q7pDV2ZgY/edit

# 2-5
#https://docs.google.com/forms/d/1u91Hsd9dpHVGSe3eNY5JI_7mDSmYEukcCgh4HkFrRz4/edit


BASE_URI = "https://docs.google.com/forms/d/{id}/formResponse"
#ID = "e/1FAIpQLSfcOxN-ZQsV_QWrmhLGMT_jSr161QB5AKnsYe41JaW1uvvVLg" # nupp (demo 5)
#ID = "e/1FAIpQLSeMiR-wuMCmds2Leo_WRlsf8JRE1U_Sa4Z8iFyYF3bwYfoxnw" # 26 (2-4 all)

#uri = BASE_URI.format(id = ID)

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}

DICT_PATH = "result_nupp_bad.json"

class Entry:

    def __init__(self, entry_id, answers):
        self.entry_id = entry_id
        self.answers = answers

    def generate_answer(self):
        return random.choice(self.answers)

def get_input(text):

    value = None

    while not value:

        try:
            value = input(text)
            value = int(value)
        except ValueError:
            value = None

    return value


def send(uri, data):
    session = requests.Session()
    r = session.post(uri, headers = headers, data = data)
    print(r)

def main():
    
    with open(DICT_PATH) as f:
        dictionary = json.load(f)

    entries = []

    for e in dictionary["entries"]:
        entry = dictionary["entries"][e]
        entry = Entry(e, entry["answers"])
        entries.append(entry)

    uri = BASE_URI.format(id = dictionary["id"])

    count = get_input("Enter count: ")
    
    for i in range(count):
        data = {}
        for e in entries:
            data[e.entry_id] = e.generate_answer()

        print(data)
        send(uri, data)
    
    print("Done")

    


if __name__ == "__main__":
    main()
