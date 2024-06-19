from menu import *

class Restuarant:
    def __init__(self, name):
        self.name = name
        self.employeeList = []
        self.menu = Menu()

    def add_employee(self, employee):
        self.employeeList.append(employee)
        print(f'\t{employee.name} is added')

    def view_employee(self):
        print(f"\t*****Employee List*****")
        for emp in self.employeeList:
            print(emp.name, emp.email, emp.phone, emp.address, emp.designation, emp.salary)
