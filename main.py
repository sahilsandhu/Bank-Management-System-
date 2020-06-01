class Bank_account:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
    def deposit(self,app):
        self.balance=self.balance+app
        print("deposit accepted")
    def withdraw(self,money):
        if money>self.balance:
            print('transaction cannot be made')
        else:
            print('transaction completed')
            self.balance=self.balance-money
            print('now the remaining money is')
            print(self.balance)
name=input('please enter the name')
amount=int(input('please enter the amount to be saved'))
d=Bank_account(name)
d.deposit(amount)
amu=int(input('enter the amount to be withdrawl'))
d.withdraw(amu)


        