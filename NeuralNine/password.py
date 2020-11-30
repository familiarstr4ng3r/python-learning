# https://www.youtube.com/watch?v=J_qQuxdnfTE

import subprocess
import chardet # pip
import locale
import os

#print(localization['ru']['KEY_CONTENT'])

# TO DO:
#If password contains  spaces in it's name you should input the name with " "
# (like this - netsh wlan show profile "TP LINK" key=clear)

localization = {
    'ru': {
        'USER_PROFILE': 'Все профили пользователей',
        'KEY_CONTENT': 'Содержимое ключа'
    },
    'en': {
        'USER_PROFILE': 'All User Profile',
        'KEY_CONTENT': 'Key Content'
    }
}

def getPasswords(dictionary):
    query_list = ['netsh', 'wlan', 'show', 'profiles']
    data = subprocess.check_output(query_list)
    # https://ru.stackoverflow.com/questions/1012024/python-не-хочет-декодить-в-utf-8
    encoding_format = chardet.detect(data).get('encoding', None)
    print(encoding_format)

    data = data.decode(encoding_format)
    data = data.split('\n')
    #print(data)
    
    ##desired = 'Все профили пользователей' # 'All User Profile'
    profiles = [line.split(':')[1][1:-1] for line in data if dictionary['USER_PROFILE'] in line]
    #print(profiles)

    ##desired_password = 'Содержимое ключа' # 'Key Content'

    for profile in profiles:
        query_list = ['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']
        results = subprocess.check_output(query_list)
        results = results.decode(encoding_format)
        results = results.split('\n')
        results = [line.split(':')[1][1:-1] for line in results if dictionary['KEY_CONTENT'] in line]

        password = results[0] if results else '#NO_PASSWORD#'
        #if not results: print(f'{profile}:#EMPTY#')
        #else: print(f'{profile}:{results[0]}')
        print('{:<20} | {:<}'.format(profile, password))


def main():
    #print(os.getcwd())
    print(locale.getlocale())
    default_locale = locale.getdefaultlocale()
    system_language = default_locale[0][:2]
    print(default_locale)
    print(system_language)
    
    getPasswords(localization[system_language])
    input()

if __name__ == '__main__':
    main()
