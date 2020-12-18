import requests

# 1
#https://docs.google.com/forms/d/1xf1QSqhw0wuhMnA7xMQyu_KAPtnF5dDhL3Q7pDV2ZgY/edit

# 2-5
#https://docs.google.com/forms/d/1u91Hsd9dpHVGSe3eNY5JI_7mDSmYEukcCgh4HkFrRz4/edit

TEST_ID = "1oeGDNdMcUjrKyrqCFMLDsNsX4k_3laYXEeBlcIhYG4I"

BASE_URI = "https://docs.google.com/forms/d/e/{id}/formResponse"
BASE_URI = "https://docs.google.com/forms/d/{id}/formResponse"

def main():
    uri = BASE_URI.format(id = TEST_ID)

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }
    
    data = {
        "entry.1204442546": "4 курс",                           # 1
        "entry.1844174236": "на мою думку, переваги відсутні",  # 2
        "entry.1031937997": "Категорично не задоволений",       # 3
        "entry.147028783" : "Answer 7",
        "entry.1041039465": "Answer 25"
    }

    print(uri)

    session = requests.Session()
    r = session.post(uri, headers = headers, data = data)
    print(r)
    print("done")


if __name__ == "__main__":
    main()
