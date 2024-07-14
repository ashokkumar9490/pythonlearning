class Account:

    def __init__(self, accno, name, balance):
        self.accno = accno
        self.name = name
        self.__balance = balance        # private instance attribute

    def __str__(self):
        return f"Accno = {self.accno} Name = {self.name} Balance = {self.__balance}"

    def deposit(self, money):           # method should be public - data should be private
        self.__balance += money

    def withdraw(self, money):
        if self.__balance >= money:
            self.__balance -= money
        else:
            print("No sufficient funds..")


acct1 = Account(1111, "AccHolder1", 10000)
acct1.deposit(50000)
acct1.withdraw(115000)
print(acct1)
