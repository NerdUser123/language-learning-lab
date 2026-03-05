# constructor 

class Employee:
    company = "HP"

    def __init__(self, name, salary, bond):
        self.name = name
        self.salary = salary
        self.bond = bond 
        
    def get_salary(self):
        return 34000
    
    def get_info(self):
        print(f"name of the person is {self.name}, salary of the person is {self.salary}, and the bond are for {self.bond} years")

e1 = Employee("jhon", 34000, 4)
e1.get_info()