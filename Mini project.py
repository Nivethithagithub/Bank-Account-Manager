# Bank Account Manager - Create a class called Account which will be an abstract class for three other classes called CheckingAccount, SavingsAccount and BusinessAccount. Manage credits and debits from these accounts through an ATM style program.
from abc import ABC,abstractmethod
class Account(ABC):
    def __init__(self,balance):
        self.balance=balance
        def deposit(self,amount):
            pass
        def withdraw(self,amlount):
            pass
class CheckingAccount(Account):
    def __init__(self,balance):
        super().__init__(balance)
    def deposit(self,amount):
        self.balance+=amount
        return self.balance
    def withdraw(self,amount):
        if amount>self.balance:
            return"Insufficient funds"
        else:
            self.balance-=amount
            return self.balance
class SavingsAccount(Account):
    def __init__(self,balance):
        super().__init__(balance)
    def deposit(self,amount):
        self.balance+=amount
        return self.balance
    def withdraw(self,amount):
        if amount>self.balance:
            return"Insufficient balance"
        else:
            self.balance-=amount
            return self.balance
class BusinessAccount(Account):
    def __init__(self,balance):
        super().__init__(balance)
    def deposit(self,amount):
        self.balance+=amount
        return self.balance
    def withdraw(self,amount):
        if amount>self.balance:
            return"Insufficient balance"
        else:
            self.balance-=amount
            return self.balance
class ATM:
    def __init__(self,account):
        self.account=account
    def deposit(self,amount):
        return self.account.deposit(amount)    
    def withdraw(self,amount):
        return self.account.withdraw(amount)

checking=CheckingAccount(100)
atm=ATM(checking)
print(atm.deposit(50))        
print(atm.withdraw(75))
print(atm.withdraw(100))
"Innsufficient funds"

