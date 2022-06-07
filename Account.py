from Bank import Bank
from Owner import Owner

class Account(Bank):
    def __init__(self, id, balance, open_date):
        self.id = id
        if balance < 0:
            raise Exception("We apologize, an account cannot be set up with a negative balance.")
        else:
            self.balance = balance
        self.open_date = open_date
        self.test = 'd'
        
        with open("/Users/evangarcia/code-platoon/week3/day2/oop-bank-accounts/support/account_owners.csv") as owners:
            for row in owners.readlines():
                line = row.strip().split(",")
                if line[0] == str(self.id):
                    self.owner_id = line[1]

        self.owner = Owner.find_owner(self.owner_id)


    def withdraw(self, withdraw_amount):
        self.withdraw_amount = withdraw_amount
        if withdraw_amount > self.balance:
            raise Exception("We apologize, this account does not have enough funds to complete this transaction.")
        else:
            self.balance -= withdraw_amount
        return self.balance

    def deposit(self, deposit_amount):
        self.deposit_amount = deposit_amount
        self.balance += deposit_amount
        return self.balance


test = Account(1212,1235667,"1999-03-27 11:30:09 -0800")

print(test.owner)

    
        


