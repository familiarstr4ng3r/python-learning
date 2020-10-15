import json
from time import sleep

#http://rutracker.org./forum/viewtopic.php?t=5896368 udemy
#https://rutracker.org/forum/viewtopic.php?t=5662165 dudar


# next video is 
# https://www.youtube.com/watch?v=NaA2H25gxN4&list=PL0lO_mIqDDFXgfuxOEDTCwsWmKezOaDTu&index=10

## ! user input
"""
message = input("write here: ")
print("message is:", message)
del message
"""

## ! loops
"""
message = "hello"
maxLength = 10

for letter in message:
	if (len(message) > maxLength):
		break
	print(letter * 2, end = '')
else:
	## if break was not executed this block occures, same way in while loop
	## string interpolation
	print(f"\nlength is less than {maxLength}")
"""

## ! ternary operator
"""
a = 11
msg = "even" if a % 2 == 0 else "not even"
print(msg)
"""

## ! lists
"""
array1 = [1, 2]
array2 = [3, 4]
array1.extend(array2)
array1.append(4)
print(array1)
array1.insert(0, 0.99)
print(array1)
print(array1.index(4))
print(f"array length is {len(array1)}")

number = 4
print(f"array contains {number}: {array1.count(number)} times")

print(array1.__sizeof__())
print(array2.__sizeof__())

a = [*range(10, 20)]
print(a)				## [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
"""

## ! json
"""
class Human(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age

human = {
	"name": "gena",
	"age": "15"
}

h = Human("sasha", 20)

jsonString = json.dumps(human)
print(jsonString)
jsonString = json.dumps(h.__dict__)
print(jsonString)
"""

## ! dictionaries
"""
d = {
	'key': 'value',
	2 : "two"
}

print(d)							## {'key': 'value', 2: 'two'}
print(d['key'])						## value
print(d[2])							## two

d = dict(myKey = 'myValue')
print(d)							## {'myKey': 'myValue'}

d = dict.fromkeys(['a', 'b'], 146)
print(d)							## {'a': 146, 'b': 146}

d = { a : a ** 2 for a in range(5)}	## {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
print(d)
"""

## ! set & fronzenset
"""
a = set("hello")
print(a)

a = {'a', 'b'}			## 'set' too
a.add('c')
print(a)
print('c' in a)			## True

b = frozenset("word")	## cant add
print(a.isdisjoint(b))	## True if doesnt contains same elements

a.update(b)				## adds all elements from 'b' to 'a'
print(a)

a.remove('a')			## if contains element then delete it, otherwise error
a.discard('j')			## if contains element then delete it
"""

## ! functions
"""
def printFunc():
	print("function executed")

def stringFunction():
	return "hello"

printFunc()
print(stringFunction())

## замыкания
def func(a):
	def add(b):
		return a + b
	return add

funcInstance = func(10)
result = funcInstance(20)
print(result)

def addAction(a, b, c = 3):
	return a + b + c

result = addAction(1, 2)
print(result)				## 6

def someAction():
	global result
	result += 10

someAction()				## result = 6 + 10
print(result)

def tupleFunc(*args):
	return args

def dictFunc(**args):
	return args

print(tupleFunc(5, 7))			## (5, 7)
print(dictFunc(a = 5, b = 7))	## {'a': 5, 'b': 7}

## lambda functions (anonymous)
addFuncInstance = lambda a, b: a + b
print(addFuncInstance(1, 4))	# 5
"""

## ! try

a = 5
b = 0

try:
	result = a / b
	print(result)
except ZeroDivisionError:
	print("dividing by zero")
except Exception:
	pass
else:
	pass
finally:
	pass