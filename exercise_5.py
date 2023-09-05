class BankAccount:
    def __init__(self,account_name,balance):
        self.account_name = account_name
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
    def withdraw(self,amount):
        self.balance -= amount
    def get_balance(self):
        s = self.account_name + ' has a balance of $' + str(self.balance) 
        return s
    
acc = BankAccount('Kiana', 100.0)
acc.withdraw(50.15)
acc.deposit(350)
print(acc.get_balance())