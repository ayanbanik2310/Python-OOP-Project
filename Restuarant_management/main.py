from fooditem import *
from menu import *
from orders import *
from users import *
from restuarant import *

vater_hotel = Restuarant('mamar vater hotel')

def customer_menu():
    name = input('enter your name : ')
    email = input('enter your e-mail : ')
    phone = input('enter your phone : ')
    address = input('enter your address : ')
    customer = Customer(name = name, email = email, address=address, phone= phone)

    while True:
        print(f'\t*****Welcome {customer.name}*****')
        print('1 : View Menu')
        print('2 : Add Item to Cart')
        print('3 : View Cart')
        print('4 : Pay Bill')
        print('1 : Exit')

        choice = int(input('enter your choice : '))

        if choice == 1:
            customer.view_menu(vater_hotel)

        elif choice == 2:
            item_name = input('enter item name : ')
            item_quantity = int(input('enter item quantity : '))
            customer.add_to_cart(restuarant=vater_hotel, item_name=item_name, quantity=item_quantity)
            
        elif choice == 3:
            customer.view_cart()
        elif choice == 4:
            customer.pay_bill()
        elif choice == 5:
            break
        else:
            print(f'\tInvalid input')


def admin_menu():
    name = input('enter your name : ')
    email = input('enter your e-mail : ')
    phone = input('enter your phone : ')
    address = input('enter your address : ')
    salary = int(input('enter salary : '))
    admin = Admin(name = name, email = email, address=address, phone= phone, salary=salary)

    while True:
        print(f'\t*****Welcome {admin.name}*****')
        print('1 : Add New Item')
        print('2 : Add New Employee')
        print('3 : View Employee')
        print('4 : View Item')
        print('5 : Delete Item')
        print('6 : Exit')

        choice = int(input('enter your choice : '))

        if choice == 1:
            item_name = input('enter item name : ')
            item_price = float(input('enter item price : '))
            item_quantity = int(input('enter item quantity : '))
            item = FoodItem(item_name, item_price, item_quantity)
            admin.add_new_item(vater_hotel, item)

        elif choice == 2:
            name = input('enter employee name : ')
            email = input('enter employee e-mail : ')
            phone = input('enter employee phone : ')
            address = input('enter employee address : ')
            salary = int(input('enter employee salary : '))
            designation = input('enter employee designation')
            age = int(input('enter employee age = '))
            
            employee = Employee(name = name , email=email, phone= phone, address=address, designation= designation, age=age,salary=salary) 
            
            admin.add_employee(vater_hotel, employee)
            
        elif choice == 3:
            admin.view_employee(vater_hotel)
        elif choice == 4:
            admin.view_menu(vater_hotel)
        elif choice == 5:
            item_name = input('enter item name : ')
            admin.remove_item(vater_hotel, item_name)
        elif choice == 6:
            break
        else:
            print(f'\tInvalid input')

while True:
    print(f'welcome to {vater_hotel.name}')
    print('1 : Customer')
    print('2 : Admin')
    print('3 : Exit')

    choice = int(input('enter choice : '))

    if choice == 1:
        customer_menu()
    elif choice == 2:
        admin_menu()
    elif choice == 3:
        print(f'tata, good bye, abar jeno dekha pai')
        break