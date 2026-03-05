# q1

class car:

    def drive(self):
        print("car is moving")

c = car()
c.drive()


#  q2

class Person:

    def __init__(self, name , age):
        self.name = name 
        self.age = age 

    def get_info(self):
        print(f"name of the person is {self.name}, age of the person is {self.age}")
    
p = Person("jhon", 19)
p.get_info()


# q3

class Animal:
    def sound(self):
        print("some sound")

class dog(Animal):
    def sound(self):
        super().sound()
        print("woof!!!")

d = dog()
d.sound()
