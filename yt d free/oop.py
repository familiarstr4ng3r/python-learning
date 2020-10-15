class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def getInfo(self):
        text = f"{self.name}, {self.age}"
        return text

class Programmer(Human):
    _kindaPrivateVariable = "secret"

    def __init__(self, name, age, **kwargs):
        self.name = name
        self.age = age

    def __someFunc(self):
        print("what the ..")

dima = Human("Dima", 20)
print(dima.getInfo())
print(dima.name)
print(dima.age)

p = Programmer("test", 1)
p._Programmer__someFunc()
print(p._kindaPrivateVariable)