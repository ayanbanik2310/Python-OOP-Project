from abc import ABC
import uuid
from datetime import datetime

class Recond:
    def __init__(self, now, transaction_type ,balance, currentBalance) :
        self.Date = now
        self.transactiontype = transaction_type
        self.balance = balance
        self.currentBalance = currentBalance


class Bank:
    def __init__(self, name) -> None:
        self.name = name
        self.transaction = []
        self.userList = []
        self.adminList = []
        self.__bank_balance = 500000
        self.loanList = []
        self.loan_accress = True
    
    def check_bank_balance (self):
        return self.__bank_balance


    def add_admin(self, admin):
        self.adminList.append(admin)
        print()
        print(f'\taccount created succesfully')
        print(f'\tyour account number is : {admin.account_number}')
        print(f'\tdon\'t forgot it')
        print()

    def add_user(self, user):
        self.userList.append(user) 
        print()
        print(f'\taccount created succesfully')
        print(f'\tyour account number is : {user.account_number}')
        print(f'\tdon\'t forgot it') 
        print()
    
    def admin_login(self, ac_no, password):
        for admin in self.adminList:
            if admin.account_number == ac_no and admin.password == password:
                return admin 
        return None
    
    def user_login(self, ac_no, password):
        for user in self.userList:
            if user.account_number == ac_no and user.password == password:
                return user 
        return None
    
    def getTime(self):
        noww = datetime.now()
        now = noww.strftime("%Y-%m-%d %H:%M:%S")
        return now

    def deposit(self, user, balance):
        self.__bank_balance += balance
        user.balance += balance
        print(f"\n\tdeposit successfull.")
        print(f'\tYour Current balance is {user.balance}/= Taka')
        print()
        now = self.getTime()
        transation_type = "Deposit     "
        record = Recond(now, transation_type , balance, user.balance)
        user.user_transaction.append(record)
        self.transaction.append(record)
    
    def withdraw(self, user, balance):
        self.__bank_balance -= balance
        user.balance -= balance
        print(f"\n\twithdraw successfull.")
        print(f'\tYour Current balance is {user.balance}/= Taka')
        print()
        now = self.getTime()
        transation_type = "Withdraw   "
        record = Recond(now, transation_type , balance, user.balance)
        user.user_transaction.append(record)
        self.transaction.append(record)
    
    def transfer_balance(self, user, ac_no, balance):
        user2 = self.find_acount(ac_no)
        if user2:
            user.balance -= balance
            user2.balance += balance
            now = self.getTime()
            user_record = Recond(now, "SendMoney" , balance, user.balance)
            user2_record = Recond(now, "RecievedMoney" , balance, user.balance) 
            user.user_transaction.append(user_record)
            user2.user_transaction.append(user2_record)
            print()
            print(f'\t Transaction successfull from account no : {user.account_number} to account no : {user2.account_number}')
            print(f'\t Your current balance is {user.balance}/= Taka')
            print()

        else:
            print()
            print(f'\tTransfer fail. Account Not Found.')
            print()

    def transaction_history(self, user):
        print()
        print(f'\t***** Transaction History *****')
        print()
        no = 1
        print(f'SL No\tDate             \tTransactionType\tActionBalance\tCurrentBalance')
        for record in user.user_transaction:
            print(f'   {no} :  {record.Date}\t{record.transactiontype}\t{record.balance}\t{record.currentBalance}')
            no+=1
 


    def see_all_user(self):
        print()
        print(f'\t***** user list *****')
        print()
        print(f'\tac_no\tname\tbalance\tac_type\tphone\taddress')
        for user in self.userList:
            print(f'\t{user.account_number}\t{user.name}\t{user.balance}\t{user.account_type}\t{user.phone}\t{user.address}') 
        print()


    def find_acount(self, ac_no):
        for user in self.userList:
            if user.account_number == ac_no:
                return user
        return None
            

    def delete_user(self, ac_no):
        user = self.find_acount(ac_no)
        if user :
            self.userList.remove(user)
            print()
            print(f'\t{user.account_number} : {user.name} deleted successfully')
            print()
        else:
            print()
            print(f'\t No account found')
            print()
    
    def total_loan(self):
        total = 0
        for loan in self.loanList:
            total += loan.amount
        
        return total
    
    def loan_control(self):
        if self.loan_accress :
            choice = input('Do you want to stop loan provide (yes/no): ')
            if choice == 'yes' :
                self.loan_accress = False
                print()
                print(f'\tloan provide stopped')
                print()
            else:
                self.loan_accress = True
        else:
            choice = input('Do you want to start loan provide (yes/no): ')
            if choice == 'yes' :
                self.loan_accress = True
                print()
                print(f'\tloan provide started')
                print()
            else:
                self.loan_accress = False

    
    def loan(self, user, amount):
        if self.__bank_balance < amount:
            print()
            print(f'\tBank Has not that much money')
            print()
        else:
            user.balance += amount
            self.__bank_balance -= amount
            loan_record = (user.account_number, amount)
            user.user_loan.append(loan_record)
            print(f'\tloan size{len(user.user_loan)}')

        
    

  



class Common(ABC):
    def __init__(self, name, email, phone, address, password) :
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.password = password
        

class Admin(Common):
    def __init__(self, account_number , name, email, phone, address, password, designation) :
        self.account_number = account_number
        self.designation = designation
        super().__init__(name, email, phone, address, password)
    




class User(Common):
    def __init__(self, account_number, name, email, phone, address, password, ocupation, account_type) :
        self.ocupation = ocupation
        self.account_type = account_type
        self.account_number = account_number
        super().__init__(name, email, phone, address, password)
        self.balance = 0
        self.user_loan = []
        self.user_transaction = []



def admin_menu(admin):

    while admin : 
        print(f'***** Admin Menu *****')
        print('options......... ')
        print('1 : See All Users')
        print('2 : Delete Users')
        print('3 : Total Loan')
        print('4 : Bank Balance')
        print('5 : Loan Control')
        print('6 : Exit')
        
        choice = int(input('enter an option : '))

        if choice == 1:
            bank.see_all_user()

        elif choice == 2:
            ac_no = int(input('Enter The user account number : '))
            bank.delete_user(ac_no)
        
        elif choice == 3:
            total = bank.total_loan()
            print()
            print(f'\ttotal loan ammount = {total}')
            print()

        elif choice == 4:
            balance = bank.check_bank_balance()
            print()
            print(f'\ttotal bank balance {balance}')
            print()
            
        elif choice == 5:
            bank.loan_control()

        elif choice == 6:
            admin = None
        
        else:
            print()
            print('\tji bhai case handle korsi, error dibo na')
            print()
    

def user_menu(user):
    while user :
        print(f'***** User Menu *****')
        print('options......... ')
        print('1 : Balance Inquiry')
        print('2 : Transaction History')
        print('3 : Take loan')
        print('4 : Transfer Balance')
        print('5 : Deposit')
        print('6 : Withdraw')
        print('7 : Exit')
        
        choice = int(input('enter an option : '))

        if choice == 1 : 
            print()
            print(f'\tYour Current balance is {user.balance}/= Taka')
            print()

        if choice == 2 : 
            bank.transaction_history(user)
            print()

        if choice == 3 : 
            pass

        if choice == 4 : 
            ac_no = int(input('Enter Account No : '))
            balance = int(input('Enter Amount of money : '))
            if balance < user.balance:
                bank.transfer_balance(user, ac_no, balance)
            else:
                print()
                print(f'\tInsufficient Balance')
                print()

        if choice == 5 : 
            balance = int(input('Enter amount : '))
            bank.deposit(user, balance)
           

        if choice == 6 : 
            balance = int(input('Enter amount : '))

            if balance > user.balance: 
                print()
                print(f'\Insufficient Balance')
                print()
            else:
                bank.withdraw(user, balance)

        
        elif choice == 7 : 
            user = None



def create_admin():
    name = input('enter your name : ')
    email = input('enter your email address : ')
    phone = input('enter your phone number : ')
    address = input('enter your address : ')
    password = input('enter your password : ')
    designation = input('enter your designation : ')
    account_number = 10000 + int(uuid.uuid4())%1000
    admin = Admin(account_number, name, email, phone, address, password, designation)
    bank.add_admin(admin)

def create_user():
    name = input('enter your name : ')
    email = input('enter your email address : ')
    phone = input('enter your phone number : ')
    address = input('enter your address : ')
    password = input('enter your password : ')
    ocupation = input('enter your ocupation : ')
    account_type = input('enter your account type : ')
    account_number = 20000 + int(uuid.uuid4())%1000
    user = User(account_number, name, email, phone, address, password, ocupation, account_type)
    bank.add_user(user)

def login_admin():
    print(f'***** Admin Login *****')
    ac_no = int(input(f'Enter Your Account Number : '))
    password = input(f'Enter your password : ')
    admin = bank.admin_login(ac_no, password)

    if admin :
        print()
        print(f'\t***** Welcome {admin.name} *****')
        print()
        admin_menu(admin)

    else:
        print()
        print(f'\tNo Admin Found')
        print()

def login_user():
    print(f'***** User Login *****')
    ac_no = int(input(f'Enter Your Account Number : '))
    password = input(f'Enter your password : ')
    user = bank.user_login(ac_no, password)

    if user :
        print()
        print(f'\t***** Welcome {user.name} *****')
        print()
        user_menu(user)

    else:
        print()
        print(f'\tno user found')
        print()


bank = Bank('Banik Bank')
# user = User(10001, 'ayan', 'ayan@gmail.com', '012345', 'sylhet', 'ayan0123', 'student', 'savings')
# user2 = User(10002, 'ayan', 'ayan@gmail.com', '012345', 'sylhet', 'ayan0123', 'student', 'savings')
# admin = Admin(1005, 'antar', 'antar@gmail.com', '014725', 'dhaka', 'antar1234', 'officer')
# bank.add_admin(admin)
# bank.add_user(user)
# bank.add_user(user2)
run = True
while run :
    print()
    print(f'\t***** welcome to {bank.name} *****')
    print(f'options.......')
    print(f'1 : Create Admin Acount')
    print(f'2 : Create User Acount')
    print(f'3 : Login')
    print(f'4 : Exit')

    choice = int(input('enter an option : '))

    if choice == 1:
        create_admin()

    elif choice == 2:
        create_user()

    elif choice == 3:
        print()
        print('options.........')
        print(f'1 : admin login')
        print(f'2 : user login')
        print(f'3 : exit')
        choice = int(input('enter an option : '))
        
        if choice == 1 : 
            login_admin()
        
        elif choice == 2 :
            login_user()
        
        elif choice == 3 :
            continue
        
        else:
            print(f'ki sir check korte aisen, case handle korsi kina, jaan thik input den gia :/')
            continue

    elif choice == 4:
        run = False

    else:
        print(f'ki sir check korte aisen, case handle korsi kina, jaan thik input den gia :/')

