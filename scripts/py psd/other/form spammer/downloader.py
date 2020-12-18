import requests
from bs4 import BeautifulSoup as bs
import re
import json

# https://theconfuzedsourcecode.wordpress.com/2019/11/10/lets-auto-fill-google-forms-with-url-parameters/

SAVE_PATH = "index.html"

#BASE_URI = "https://docs.google.com/forms/d/{id}/viewform"
#ID = "1u91Hsd9dpHVGSe3eNY5JI_7mDSmYEukcCgh4HkFrRz4"

# same lol but link without /e/
# https://docs.google.com/forms/d/e/1FAIpQLSeMiR-wuMCmds2Leo_WRlsf8JRE1U_Sa4Z8iFyYF3bwYfoxnw/viewform

BASE_URI = "https://docs.google.com/forms/d/{id}/viewform"
#ID = "e/1FAIpQLSfcOxN-ZQsV_QWrmhLGMT_jSr161QB5AKnsYe41JaW1uvvVLg" # nupp (demo 5)
ID = "e/1FAIpQLSeMiR-wuMCmds2Leo_WRlsf8JRE1U_Sa4Z8iFyYF3bwYfoxnw" # 26 (2-4 all)

uri = BASE_URI.format(id = ID)

def download(uri, save = False):
    response = requests.get(uri)

    text = response.content

    if save:
        with open(SAVE_PATH, "wb") as f:
            f.write(text)

    return text

def read(path):

    with open(SAVE_PATH, encoding = "utf-8") as f:
        text = f.read()

    return text

def parse(html_text):

    html = bs(html_text, "html.parser")

    container = html.find("div", class_ = "freebirdFormviewerViewItemList")

    print("All Length:", len(container))
    print("#")

    result = []
    
    for element in container:
        #header = element.find("div", class_ = "freebirdFormviewerComponentsQuestionBaseTitle exportItemTitle freebirdCustomFont")
        header = element.find("div", class_ = "freebirdFormviewerComponentsQuestionBaseHeader")
        
        question = header.text
        data = None
    
        radioRoot = element.find("div", class_ = "freebirdFormviewerComponentsQuestionRadioRoot")
        checkboxRoot = element.find("div", class_ = "freebirdFormviewerComponentsQuestionCheckboxRoot")

        if radioRoot:
            data = handleRoot(radioRoot, "RadioButton")
        elif checkboxRoot:
            data = handleRoot(checkboxRoot, "Checkbox")
        else:
            pass

        e = (question, data)
        result.append(e)

    return result

# not used
def get_all_entries(text):

    soup = bs(text,"lxml")
    divs = soup.find_all("input")

    divs = [div for div in divs if "name" in div.attrs and div.attrs["name"].startswith("entry")]
    print(len(divs))
    
    for d in divs:
        print(d)

# not used
def shit_json(text):
    # https://stackoverflow.com/questions/63717073/how-to-extract-entry-id-from-google-form-using-beautiful-soup
    
    data = re.search(r'FB_PUBLIC_LOAD_DATA_ = (.*?);', text, flags=re.S)
    data = data.group(1)
    data = json.loads(data)

    #for i in get_ids(data):
    #    print(i)

# not used
def get_ids(d):
    if isinstance(d, dict):
        for k, v in d.items():
            yield from get_ids(v)
    elif isinstance(d, list):
        if len(d) > 1 and d[1] is None:
            yield d[0]
        else:
            for v in d:
                yield from get_ids(v)

    
def save(data):
    # tuple(title, tuple(entry_id, list, mode))

    entries = {}
    dictionary = {"id": ID, "entries": entries}
    
    
    for title, entry in data:
        if entry:
            entry_id = entry[0]
            answers = entry[1]
            mode = entry[2]

            entry_dictionary = {"title":title, "answers":answers, "mode":mode}
            
            
            entries[entry_id] = entry_dictionary


    ##for k in dictionary:
    ##    print(dictionary[k])

    ##json_object = json.dumps(dictionary, indent = 4)
    ##print(json_object)

    # https://stackoverflow.com/questions/33141120/python-how-to-save-dictionary-with-cyrillic-symbols-into-json-file

    filename = input("Enter filename: ")
    
    with open(filename, "w") as f:
        json.dump(dictionary, f, indent = 4, ensure_ascii = False)

    
        
            
def handleRoot(root, mode):

    # https://linuxhint.com/find_children_nodes_beautiful_soup/
    #first = root.contents[0]
    #print(first)
        
    #childrens = root.findChildren()
    #entry_id = childrens[0]["name"]
    entry_id = root.contents[0]["name"]
    entry_id = entry_id[:-9]
    answers = []
        
    elements = root.find_all("div", class_ = "docssharedWizToggleLabeledPrimaryText")

    for e in elements:
        answers.append(e.text)

    return (entry_id, answers, mode)
    
def handleInputContainer(container):
    pass

def main():
    
    #html = read(SAVE_PATH)
    html = download(uri)

    result = parse(html)
    save(result)

    print("\nDone")


if __name__ == "__main__":
    main()
