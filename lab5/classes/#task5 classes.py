#task5 classes
class account:
    def __init__(self, owner, balance=0):
        self.owner=owner
        self.balance=balance
    
    def deposite(self, dep):
        self.balance+=dep
        print(f"New balance after deposite: {self.balance}")
        # print(self.balance)
    
    def withdraw(self, wd):
        if self.balance>=wd:
            self.balance-=wd
            print(f"New balance after withdraw: {self.balance}")
            # print(self.balance)
        else:
            print("Not a available")


acc=account('John', 200)
print(f"\nAccount owner: {acc.owner}, \nBalance: {acc.balance}")
acc.deposite(50)
acc.withdraw(75)
acc.withdraw(300)
