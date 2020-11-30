import locale
import subprocess
import chardet

class Entry:

    name: str
    password: str

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def __str__(self):
        return '{:<20} | {:<}'.format(self.name, self.password)

def getPasswords(dictionary):
    query_list = ['netsh', 'wlan', 'show', 'profiles']
    data = subprocess.check_output(query_list)

    encoding_format = chardet.detect(data).get('encoding', None)
    print(f'Encoding: {encoding_format}' + '\n')

    data = data.decode(encoding_format)
    data = data.split('\n')
    
    profiles = [line.split(':')[1][1:-1] for line in data if dictionary['USER_PROFILE'] in line]
    print(f'Found {len(profiles)} profiles')

    entries = []

    for profile in profiles:
        query_list = ['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']
        results = subprocess.check_output(query_list)
        results = results.decode(encoding_format)
        results = results.split('\n')
        results = [line.split(':')[1][1:-1] for line in results if dictionary['KEY_CONTENT'] in line]

        password = results[0] if results else '#NO_PASSWORD#'
        
        e = Entry(profile, password)
        entries.append(e)
        

    return entries

def load_CSV(filepath):

    with open(filepath) as f:
        content = f.read()
    
    separator = content[0]
    #print(separator) # ;
    grid = [line.split(separator) for line in content.split('\n') if line]

    localization = {}

    languages = grid[0]
    for i in range(1, len(languages)):
        
        language_dictionary = {}

        for k in range(1, len(grid)):
            key = grid[k][0]
            value = grid[k][i]
            #print(key + '=' + value)
            language_dictionary[key] = value
        
        localization[languages[i]] = language_dictionary

    return localization

def showInfo(entries):
    for e in entries:
        print(e)

def tryOtherLanguage(localization):
    for key in localization:
        language_dictionary = localization[key]
        entries = getPasswords(language_dictionary)
        
        if len(entries) > 0:
            print(f'Target language: {key}')
            showInfo(entries)
            break

def main():
    localization = load_CSV('localization_short.csv')
    #print(localization)

    # https://www.localeplanet.com/icu/

    print(f'Locale: {locale.getlocale()}')

    default_locale = locale.getdefaultlocale()
    system_language = default_locale[0]
    system_language_short = system_language[:2]

    print(f'Default locale: {default_locale}')
    print(f'System language: {system_language}')
    print(f'System language short: {system_language_short}')
    
    # for exception debugging: there is no exception, atleast on my computer
    #system_language_short = 'uk' 

    if system_language_short in localization:
        language_dictionary = localization[system_language_short]
        entries = getPasswords(language_dictionary)
        
        if len(entries) > 0:
            showInfo(entries)
        else:
            print(f'Not found: no entries for "{system_language_short}", iterating over all languages in global dictionary')
            tryOtherLanguage(localization)

    else:
        print(f'Not found: no language dictionary for "{system_language_short}", iterating over all languages in global dictionary')
        tryOtherLanguage(localization)


if __name__ == '__main__':
    main()