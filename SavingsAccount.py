from Account import Account

class SavingsAccount(Account):
    def __init__(self, id, balance, open_date):
        super().__init__(id, balance, open_date)
        if self.balance < 10:
            raise Exception("We apologize, a savings account cannot have a balance of less than $10.")

    def withdraw(self, withdraw_amount):
        self.withdraw_amount = withdraw_amount
        if (withdraw_amount + 10) > (self.balance):
            raise Exception(f"We apologize, this account does not have enough funds to complete this transaction. Your current balance is ${self.balance}. ")
        else:
            self.balance -= withdraw_amount
        return self.balance

    def add_interest(self, rate):
        old_balance = self.balance
        self.rate = rate
        self.balance += int(self.balance * (rate/100))
        return f"Your savings have increased ${self.balance - old_balance}!"


        


test = SavingsAccount(1212, 10000, "1999-03-27 11:30:09 -0800")
print(test.add_interest(0.25))