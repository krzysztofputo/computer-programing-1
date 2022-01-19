class Bank():
    
    def __init__(self, b_nr, ):
        self.b_nr = b_nr
        self.balance = 0
        
    def deposit(self, pln):
        self.balance += pln
        
    def withdraw(self, pln):
        if self.balance > pln:
            self.balance -= pln
        else:
            print("Insufficient funds on the account")                    

bank = Bank("12 3456 5555 9090 1111 0000 7722")
print(bank.balance)
bank.deposit(25.30)
print(bank.balance)
bank.withdraw(31.70)
print(bank.balance)
bank.withdraw(14)
print(bank.balance)