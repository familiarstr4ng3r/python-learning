from bs4 import BeautifulSoup as bs

def get_text(path):
    try:
        with open(path, encoding = "utf-8") as f:
            text = f.read()
    except IOError:
        print("[IOError]")
        return False, None
    else:
        return True, text

def parse(text):
    soup = bs(text, "html.parser")
    soccer = soup.find("div", {"class": "sportName soccer"})

    # why this shit is None
    #soccer = soup.find("div", _class = "sportName soccer")

    # iteraring childs by index
    #e = soccer.contents[i]
    
    ids = []
    
    for i, element in enumerate(soccer):
        e_id = element.get("id")
        if not e_id is None: ids.append(e_id)

    return ids

def main():
    success, text = get_text("index.html")

    if success:
        ids = parse(text)
        print("Ids:", len(ids))
        print(ids)
    else:
        print("Not success!")


if __name__ == "__main__":
    main()

    











