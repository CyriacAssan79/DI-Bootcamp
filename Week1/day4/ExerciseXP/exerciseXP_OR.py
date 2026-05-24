#Part I

#Account class 
class BankAccount :
    def __init__(self, balance,username, password):
        self.balance = balance
        self.username = username
        self.password = password
        self.authenticated = False #Verfy user authentification

    def deposit(self,money):
        if self.authenticated : #User can deposit if it's connected (authenticated == Tue)
            if money > 0: #We verify if amount of depot is superior that 0
                self.balance += money
                return self.balance
            else :
                raise Exception("The amount seized is less than 1 FCFA")
        else :
            raise Exception ('You are not connected')
    
    def withdraw (self,money): #This method verify if user is connected and money withdraw is inferior that balance, if it's ok, we can do the withdrawal
        if(self.authenticated):
            if money > 0:
                if money <= self.balance :
                    self.balance -= money
                else :
                    raise Exception("Insufficient funds to make a withdrawal !")
            else :
                raise Exception("The amount seized is less than 1 FCFA")
        else :
            raise Exception ("You are not connected")
    
    def authenticate(self,username, password) :
        if username == self.username and password == self.password :
            self.authenticated = True
            print('You are connected !')
        else :
            raise Exception ('Username or password is incorrect')


class MinimumBalanceAccount(BankAccount) :
    def __init__(self, balance,username, password, minimum_balance = 0):
        super().__init__(balance,username, password)
        self.minimum_balance = minimum_balance
    
    def withdraw(self, money):
        if self.authenticated :
            if money > 0:
                #Vérification funds
                if self.balance - money >= self.minimum_balance :
                    self.balance -= money
                    print(self.balance)
                else :
                    raise Exception("Insufficient funds to make a withdrawal !")
            else :
                raise Exception("The amount seized is less than 1 FCFA")
        else :
            raise Exception ('You are not connected')


# class ATM :
#     def __init__(self, account_list,try_limit):
#         self.account_list = account_list
#         self.try_limit = try_limit
    
#     def log_in(self):
#         print("DO YOU WANT TO CONNECTED ? ENTER YOU INFORMATIONS")
#         name = input("Name : ")
#         password = input("Password : ")

#         for account in self.account_list :
#             if MinimumBalanceAccount.authenticate(name,password) :



#     def show_main_menu(self) :
#         print("*************** DO YOU WANT TO DO OPERATION ? : *****************")
#         print('1 - Connexion \n2 - Exit')
#         user_choice = 0
#         while True :
#             choice = input("Select : ")
#             if choice == "1" or choice == "2" :
#                 user_choice = choice
#                 break
        
#         if user_choice == "2" :
#             return print('Thank\'s, see you soon !')
#         else :
#             self.log_in()
            
        


account = MinimumBalanceAccount(
    100,
    "Cyriac79",
    "azerty",
    minimum_balance=20
)

account.authenticate("Cyriac79", "azerty")

account.deposit(50)

account.withdraw(110)