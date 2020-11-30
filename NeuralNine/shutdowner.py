import os

#SHIT START

with open(__file__) as f:
    lines = f.readlines()

delimiter = '#SHIT'
started = False
shittyCode = []

for line in lines:
    if not started and line.startswith(delimiter):
        started = True
        shittyCode.append(line)
        continue

    if started:
        shittyCode.append(line)

        if line.startswith(delimiter):
            break

goodCode = [x for x in lines if x not in shittyCode]

with open(__file__, 'w') as f:
    f.writelines(goodCode)

# SOME THINGS HERE, EXAMPLE:
# os.system('shutdown -s')

#SHIT END

print('Hello World')