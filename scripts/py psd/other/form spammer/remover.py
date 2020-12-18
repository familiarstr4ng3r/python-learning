import urllib
import requests

#http://ddecode.com/hexdecoder/

def main():
    with open("text.txt") as f:
        text = f.read()

    #print(text)

    text = text.replace("^", "")
    #print(text)

    text = requests.utils.unquote(text)
    print(text)

    #text = urllib.parse.unquote(text)
    #print(text)

    print("#")

    lines = text.split("&")

    for l in lines:
        print(l)


    


if __name__ == "__main__":
    main()
