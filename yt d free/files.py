def printLines(file):
    for line in file:
        print(line.strip())

path = "../text.txt"
readAction = open(path, encoding='utf-8')

## first method

file = readAction
printLines(file)
file.close()

print('')

## second method

with open(path, encoding='utf-8') as file:
    printLines(file)
    

