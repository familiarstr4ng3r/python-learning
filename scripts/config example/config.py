import configparser

filePath = 'config.ini'

config = configparser.ConfigParser()

readed = config.read(filePath)

if len(readed) == 0:
    print (f'File \'{filePath}\' does not exists. Quitting the program!')
    quit(0)

### START READING VALUES

readSection = 'Header'

if (config.has_section(readSection)):
    f = config.get(readSection, 'first')
    s = config.get(readSection, 'second')
    print(f)
    print(s)

### END READING VALUES

### START WRITING VALUES

writeSection = 'Example'

hasSection = config.has_section(writeSection)

if not hasSection:
    config.add_section(writeSection)
    config.set(writeSection, 'third', 3)
    config.set(writeSection, 'fourth', 4)

    with open(filePath, 'w') as f:
        config.write(f)
else:
    t = config[writeSection].getint('third')
    f = config[writeSection].getint('fourth')
    print(t)
    print(f)

### END WRITING VALUES
