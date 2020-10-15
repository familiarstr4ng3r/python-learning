from datetime import datetime
import math
import time
import os
import random as r

try:
    import mondi
    from mondi import sayBye as bye
except ImportError:
    print("'mondi module doesn't exists")


## ! time
"""
now = datetime.now()
print(now)
print(math.pi)

seconds = time.time()
now = time.localtime(seconds)
utcNow = time.gmtime(seconds)

print(seconds)
print(now)
#print(type(now))
print(utcNow)

year = now[0]
print(year)
"""

path = os.getcwd()
print(path)
print(r.random())

text = mondi.sayHello()
print(text)

bye()