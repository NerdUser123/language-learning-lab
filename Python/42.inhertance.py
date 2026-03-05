# inhertance 

class Animal:

    def __init__(self, name):
        self.name = name

    def speak(self):
        print("generic animal sound")

class Dog(Animal):
    
    def speak(self):
        super().speak()
        print("woof!!")

d = Dog("bruno")
d.speak()
print(d.name)