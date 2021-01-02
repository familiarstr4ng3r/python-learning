import json
import time
import requests
from bs4 import BeautifulSoup as bs

# try it
# https://github.com/JakeHarrison11/ChangeOrgSignBot
# https://www.youtube.com/watch?v=Xjv1sY630Uc
# https://sites.google.com/a/chromium.org/chromedriver/downloads
# https://www.1secmail.com/api/

SITE_LINK = "https://www.change.org/p/26627345"
POST_LINK = "https://www.change.org/api-proxy/graphql/signPetition/26627345"

# "совет-федерации-внесите-правки-в-закон-о-цифровых-финансовых-активах-который-блокирует-кошелек-steam"
# "https://www.change.org/su/p/{}/f?source_location=psf_petitions"

RANDOM_MAIL_LINK = "https://www.1secmail.com/api/v1/?action=genRandomMailbox&count={count}"
GET_MESSAGES_LINK = "https://www.1secmail.com/api/v1/?action=getMessages&login={login}&domain={domain}"
READ_MESSAGE_LINK = "https://www.1secmail.com/api/v1/?action=readMessage&login={login}&domain={domain}&id={id}"

session = requests.Session()

def get_json_data(email, firstName, lastName):
    data = {}
    data["operationName"] = None

    variables = {}
    variables["shouldRewardShareBandit"] = False
    variables["rewardShareBanditInput"] = {"banditId":"", "variantName":""}
    data["variables"] = variables

    signatureInput = {}
    signatureInput["petitionId"] = "26627345"
    signatureInput["pageContext"] = "petitions_show"
    signatureInput["trafficMetadata"] = {}
    signatureInput["isMobile"] = False
    signatureInput["recentlySeenMembershipRequest"] = False
    signatureInput["sourceLocation"] = None
    signatureInput["algorithm"] = None
    signatureInput["inviteRecruiterUuid"] = None
    signatureInput["userSawSignInterrupt"] = False
    signatureInput["firstName"] = firstName
    signatureInput["lastName"] = lastName
    signatureInput["email"] = email
    signatureInput["city"] = "Novi Sanzhary"
    signatureInput["stateCode"] = "18"
    signatureInput["postalCode"] = "39300"
    signatureInput["countryCode"] = "UA"
    signatureInput["public"] = True
    signatureInput["shareInfoWithOrganization"] = False
    signatureInput["marketingCommsConsent"] = None
    data["signatureInput"] = signatureInput

    with open("Resources/query.txt", encoding = "utf-8") as f:
        data["query"] = f.read()

    data = json.dumps(data, ensure_ascii = False)
    return data


def send_mail(session, email):
    link = SITE_LINK
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
    data = get_json_data(email, "Саша", "Белый")
    
    response = session.post(POST_LINK, json = data, headers = headers)
    #response = session.get(POST_LINK, headers = headers)

    code = response.status_code

    print("Code:", code)
    print(response.text)
    
    if code == 403 or code == 400:
        quit("quit!")


def get_mails(session, count):
    link = RANDOM_MAIL_LINK.format(count = count)
    response = session.get(link)
    mails = response.json()
    return mails


def get_messages(session, login, domain):
    link = GET_MESSAGES_LINK.format(login = login, domain = domain)
    response = session.get(link)
    messages = response.json()
    #print("Found {} messages".format(len(messages)))
    return messages


def read_message(session, login, domain, message_id):
    link = READ_MESSAGE_LINK.format(login = login, domain = domain, id = message_id)
    response = session.get(link)
    data = response.json()
    body = data["body"]
    return body


def proceed_body(body):
    soup = bs(body, "html.parser")
    
    container = soup.find("p", {"class" : "type-break-word"})
    uri = container.text.strip()
    return uri

### Public

def get_email():
    email = get_mails(session, 1)[0]
    return email

def check_email(email):
    login, domain = email.split("@")
    messages = get_messages(session, login, domain)

    if (len(messages)) == 0:
        return False, None
    else:
        message = messages[0]
        message_id = message["id"]
        body = read_message(session, login, domain, message_id)
        uri = proceed_body(body)
        return True, uri

def close():
    session.close()

###

def load(session):
    mails = get_mails(session, 2)
    email = mails[0]
    print("Email:", email)
    login, domain = email.split("@")
    #print("Login:", login)
    #print("Domain:", domain)

    send_mail(session, email)
        
    #login = "8bzxpr6f79"
    #domain = "1secmail.com"
    
    messages = get_messages(session, login, domain)

    times = 0
    while(len(messages) == 0):
        time.sleep(2)
            
        messages = get_messages(session, login, domain)
        times += 1
            
        if times == 10:
            print("No messages at:", email)
            quit()
        
    message = messages[0]
    message_id = message["id"]
    #print("Id:", message_id)

    body = read_message(session, login, domain, message_id)
    uri = proceed_body(body)

    # to do: proceed uri
    print(email)
    print(uri)


def read():
    with open("Resources/body demo.txt", encoding = "utf-8") as f:
        body = f.read()

    uri = proceed_body(body)
    print(uri)


if __name__ == "__main__":
    load()
    #read()


