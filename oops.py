class human:
    def __init__(self,balance  ):
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print("Deposit accepted. New balance is:", self.balance)
    def withdraw(self,amount):
        self.balance-=amount
        print("Withdrawal accepted. New balance is:", self.balance)

a=human(1000)
a.deposit(500)
a.withdraw(200)