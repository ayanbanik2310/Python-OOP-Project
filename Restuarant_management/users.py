"""

Customer 
Employee
Admin

kichu common characteristics sobar moddhei ase like name, phone, email, address etc

common characteristics gula base class diye access korte pari
uncommon gula subclass diye

"""

from abc import ABC
from orders import *

class Users(ABC):
    def __init__(self, name, email, phone, address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

class Employee(Users):
    def __init__(self, name, email, phone, address, designation, age, salary):
        super().__init__(name, email, phone, address) 
        self.designation = designation
        self.age = age
        self.salary = salary

class Admin(Users):
    def __init__(self, name, email, phone, address, salary):
        super().__init__(name, email, phone, address) 
        self.salary = salary
    
    def add_employee(self, restuarant, employee):
        restuarant.add_employee(employee)
    
    def view_employee(self, restuarant):
        restuarant.view_employee()
    
    def add_new_item(self, restuarant, item):
        restuarant.menu.add_menu_item(item)

    def remove_item(self, restuarant, item):
        restuarant.menu.remove_item(item)
    
    def view_menu(self, restuarant):
        restuarant.menu.show_menu()



class Customer(Users):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)
        self.cart = Order()
    

    def view_menu(self, restuarant):
        restuarant.menu.show_menu()
    
    def add_to_cart(self, restuarant, item_name, quantity):
        item = restuarant.menu.find_item(item_name)

        if item:
            if quantity > item.quantity:
                print(f'\titem quantity exceed')
            else:
                item.quantity = quantity
                self.cart.add_item(item)
                print(f'\t{item_name} : added to cart')
        else:
            print(f'\t{item_name} : item not found')
    
    def view_cart(self):
        print('\t*****Your Cart*****')
        print(f'\tItem\tQuantity\tPrice')
        for item,  quantity in self.cart.items.items():
            print(f'\t{item.name}\t{quantity}\t{item.price}')
        
        print(f'\ttotal = ${self.cart.total_price()}')
    
    def pay_bill(self):
        
        print(f'\t Total ${self.cart.total_price()} paid successfully')
        self.cart.clear()
    







