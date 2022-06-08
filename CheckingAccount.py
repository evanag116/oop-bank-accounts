from Account import Account


class CheckingAccount(Account):
    def __init__(self, id, balance, open_date):
        super().__init__(id, balance, open_date)
        if balance < 0:
            raise Exception("We apologize, a checking account cannot be set up with a negative balance.")
        else:
            self.balance = balance
        self.checks_remaining = 3



    def withdraw(self, withdraw_amount):
        if (withdraw_amount + 1) > self.balance: 
            raise Exception(f"We apologize, this account does not have enough funds to complete this transaction. Withdrawing incurs a fee of $1. Your current balance is ${self.balance}. ")
        else:
            self.balance -= withdraw_amount + 1
        return self.balance

    def withdraw_using_check(self, amount):
        if self.checks_remaining < 1:
            amount += 2
        if self.balance - amount < -10: 
            raise Exception(f"We apologize, this account does not have enough funds to complete this transaction. Your current balance is ${self.balance}. ")
        else:
            self.balance -= amount
        self.checks_remaining -= 1
        return self.balance


    def reset_checks(self):
        self.checks_remaining = 3
            

    