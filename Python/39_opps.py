# abstraction - showing only what is needed and hiding how it works inside.

# encapsulation - keeping data and the code that works on that data together, and protecting it from direct access.

# inheritence - means a child class gets properties and methods from a parent class.

# Polymorphism - means “one thing, many forms.

class Employee:
    company = "hp" 

    def get_salary(self):
        return 34000
    
e = Employee()
print(e.get_salary())