# https://sites.google.com/a/chromium.org/chromedriver/downloads
# https://www.youtube.com/watch?v=Xjv1sY630Uc
# https://github.com/JakeHarrison11/ChangeOrgSignBot

import time
import random
import json
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import mail_sender


DRIVER_PATH = r"D:\dev\Selenium\chromedriver.exe"
LINK = "https://www.change.org/p/26627345"

driver = webdriver.Chrome(DRIVER_PATH)
driver.get(LINK)

def load_json(path):
    with open(path) as f:
        data = json.loads(f.read())
        return data

def get_names():
    fname = random.choices(fnames)
    lname = random.choices(lnames)
    return fname, lname


fnames = load_json("Resources/fnames.json")
lnames = load_json("Resources/lnames.json")


def make_delay(count, console = False):
    for i in list(range(count))[::-1]:
        if console: print(i + 1)
        time.sleep(1)


def driver_exit():
    driver.delete_all_cookies()
    driver.quit()
    print("Driver closed")

def run():
    #make_delay(2)

    found_form = EC.presence_of_element_located((By.NAME, "sign-form"))
    sign_form = WebDriverWait(driver, 5).until(found_form)
    
    fnameBox = driver.find_element_by_name("firstName")
    lnameBox = driver.find_element_by_name("lastName")
    emailBox = driver.find_element_by_name("email")
    publicCheck = driver.find_element_by_name("public")

    try:
        # from github
        #xpath = """//*[@id="page"]/div[1]/div[3]/div[2]/div/div/div/div[2]/div[2]/form/button[2]"""

        # page
        # div 2 = container xs-pan
        # div 3 = row mbxxl xs-mbn xs-mhn
        # div 2 = hidden-xs
        # divs
        # div 2 = sc-AxheI nPYYb
        # div 2 = sc-AxheI iDtiqJ
        
        xpath = """//*[@id="page"]/div[2]/div[3]/div[2]/div/div/div/div[2]/div[2]/form/button"""
        signButton = driver.find_element_by_xpath(xpath)

        """
        text = signButton.get_attribute("innerHTML")
        with open("button.html", "w", encoding = "utf-8") as f:
            f.write(text)
        """
        
    except:
        print("except")
        driver_exit()
        quit()

    fname, lname = get_names()
    email = mail_sender.get_email()
    print("Email:", email)

    publicCheck.click()
    time.sleep(1)
    
    fnameBox.send_keys(fname)
    time.sleep(1)
    lnameBox.send_keys(lname)
    time.sleep(1)
    emailBox.send_keys(email)
    time.sleep(1)

    signButton.click()
    time.sleep(1)

    print("Waiting for message..")
    time.sleep(2)
    print("Checking email..")

    for i in range(5):
        success, uri = mail_sender.check_email(email)
        if success:
            print(i, "Found")
            break
        else:
            print(i, "Not found")
            time.sleep(5)

    print("Uri:", uri)
    driver.get(uri)

    print("Loaded")
    time.sleep(2)
    print("Done!")


run()
driver_exit()

