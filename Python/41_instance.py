# instance

class Employee:
    company = "HP"

    def __init__(self, name, salary, bond, company):
        self.name = name
        self.salary = salary
        self.bond = bond 
        self.company = company
        
    def get_salary(self):
        return 34000
    
    def get_info(self):
        print(f"name of the person is {self.name}, salary of the person is {self.salary}, and the bond are for {self.bond} years, company is {self.company}")

e1 = Employee("jhon", 34000, 4, "tesla")
e1.get_info()
print(Employee.company)

# object instropection 

print(dir(e1))