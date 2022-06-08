from Account import Account

class MoneyMarketAccount(Account):
    def __init__(self, id, balance, open_date):
        super().__init__(id, balance, open_date)
        if balance < 10000:
            raise Exception("We apologize, a Money Market account cannot be set up with a balance of less than $10,000.")
        else:
            self.balance = balance
        self.transactions = 0


    def withdraw(self, withdraw_amount):
        if self.transactions >= 6:    
            self.transactions += 1
            if self.balance < 10000:
                raise Exception(f"We apologize, this account does not have enough funds to complete this transaction. Your current balance is ${self.balance}.")
            if (self.balance - withdraw_amount) < 10000: 
                self.balance -= withdraw_amount + 100
            else:
                self.balance -= withdraw_amount
            return self.balance
        else:
            raise Exception("Maximum number of transactions have been reached for this month.")


    def add_interest(self, rate):
        old_balance = self.balance
        self.rate = rate
        self.balance += int(self.balance * (rate/100))
        return f"Your Money Market account balance has increased ${self.balance - old_balance}!"

    def reset_transactions(self):
        self.checks_transactions = 6

    def deposit(self, deposit_amount):
        if self.transactions < 6: 
            self.transactions += 1
            self.deposit_amount = deposit_amount
            if self.balance < 10000:
                if self.balance + deposit_amount >= 10000:
                    self.transactions = 6
            self.balance += deposit_amount

            return self.balance
        else:
            raise Exception("Maximum number of transactions have been reached for this month.")
    
    

