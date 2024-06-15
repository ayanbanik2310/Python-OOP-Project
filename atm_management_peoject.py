"""

functionalities: 

section 1 : login, registration

section 2 : balance check, withdraw, deposit, transaction statement, logout

"""

from datetime import datetime

class User:
    def __init__(self, name, age, phone , uniqueID, password):
        self.name = name
        self.age = age
        self.phone = phone
        self.uniqueID = uniqueID
        self.password = password
        self.balance = 0
        self.transaction = []

class Recond:
    def __init__(self, now,transaction_type ,balance, currentBalance) :
        self.Date = now
        self.transactiontype = transaction_type
        self.balance = balance
        self.currentBalance = currentBalance

class Atm:
    def __init__(self, name):
        self.name = name
        self.__atmBalance = 5000
        self.userList = []
    
    def addUser(self, name, age, phone , uniqueID, password):
        user = User(name, age, phone , uniqueID, password)
        self.userList.append(user)
        return user


    def checkbalance(self,user):
        print(f'\n\tyour cuurent balance is {user.balance}\n')
    
    def getTime(self):
        noww = datetime.now()
        now = noww.strftime("%Y-%m-%d %H:%M")
        return now

    def deposit(self, user, balance):
        self.__atmBalance += balance
        user.balance += balance
        print(f"\n\tdeposit successfull.")
        self.checkbalance(user)
        now = self.getTime()
        transation_type = "Deposit"
        record = Recond(now, transation_type , balance, user.balance)
        user.transaction.append(record)


    def withdraw(self, user, balance):
        if self.__atmBalance >= balance and user.balance >= balance:
            self.__atmBalance -= balance
            user.balance -= balance

            print(f"\n\withdraw successfull. Collect your money")
            self.checkbalance(user)

            now = self.getTime()
            transation_type = "withdraw"
            record = Recond(now, transation_type , balance, user.balance)
            user.transaction.append(record)
            return
        
        print(f'\n\tinsufficient balance\n')
        return
    
    def checkTransaction(self,user):
        
        if len(user.transaction) == 0:
            print("\n\tNo transaction has made yet\n")
            return
        no = 1
        print(f"\t\t|-----------------------------|")
        print(f"\t\t| --- Transaction History --- |")
        print(f"\t\t|-----------------------------|")
        for record in user.transaction :
            print(f"\t{no} :\t{record.Date}\t{record.transactiontype} {record.balance}\t{record.currentBalance}")
            no+=1


phitron_atm = Atm("phitron atm management demo")
user = phitron_atm.addUser("ayan", 23, "01700000000", 1234, "ayan1234")
currentUser = None

while True:
    if currentUser == None:
        print(f"\t|------------------------------------------------|")
        print(f"\t| --- welcome to {phitron_atm.name} --- |")
        print(f"\t|------------------------------------------------|")

        print("options: ")
        print("1. Login")
        print("2. Registration")
        print("3. Sorry galti se ageya")

        choice = int(input("select an option : "))
        
        if choice == 1: 
            id = int(input("\tenter your unique id : "))
            password = input("\tenter your password : ")

            match = False
            for user in phitron_atm.userList:
                if user.uniqueID == id and user.password == password:
                    currentUser = user
                    match = True
                    break
            if match == False:
                print("\n\tNo user found\t")
        
        elif choice == 2:
            name = input('\tenter your name : ')
            age = int(input('\tenter your age : '))
            phone = input('\tenter your phone number : ')
            uniqueID = int(input('\tenter your unique id : '))
            password = input('\tenter password : ')

            user = phitron_atm.addUser(name, age, phone, uniqueID, password)
            
            print("\n\tsuccesfully register. Now you can do transaction.\n")

            currentUser = user


        elif choice == 3:
            print("\n\tok! get out from here. \n")
            break  

    else:

        print(f"\n\t| --- welcome {currentUser.name} --- |\n")

        
        print("options: ")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transaction Statement")
        print("5. Logout")

        choice = int(input("select an option : "))
        
        if choice == 1:
            phitron_atm.checkbalance(user)


        elif choice == 2:
            balance = int(input("\tenter balance : "))
            phitron_atm.deposit(user, balance)


        elif choice == 3:
            balance = int(input("\tenter balance : "))
            phitron_atm.withdraw(user, balance)

        elif choice == 4:
            phitron_atm.checkTransaction(user)

        elif choice == 5:
            currentUser = None 
        
