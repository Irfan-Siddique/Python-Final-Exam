import random
var=None
class User:
    def __init__(self,name,email,age,account_type) -> None:
        self.name=name
        self.email=email
        self.age=age
        self.account_type=account_type
        self.account_no=random.randint(100000,999999)
        self.balance=0
        self.transactions=[]
        self.loan_count=0

    def deposit(self,amount,bank):
        self.balance +=amount
        bank.money_in_the_bank +=amount
        print(f"{amount} is deposited")
    
    def withdraw(self, amount,bank):
        if amount <= bank.money_in_the_bank:
            if amount <= self.balance:
                self.balance -= amount
                bank.money_in_the_bank -=amount
                print(f"{amount} withdrawed successfully")
            else:
                print("Withdrawal amount exceeded")
        else:
            print("The bank is BANKRUPT")
    
    def check_available_balance(self):
        print(f"your balance is: {self.balance}")
    
    def transaction_history(self):
        for item in self.transactions:
            print(item)
    
    def take_loan(self,amount,bank):
        if self.loan_count >=2:
            print("you already taken loan two times")
            return
        else:
            if amount > bank.money_in_the_bank:
                print("bank does not have that much money")
                return
            else:
                bank.money_in_the_bank -=amount
                self.balance +=amount
                bank.total_loan +=amount
                print(f"{amount} is taken as loan")
    
    def transfer_money(self,amount,account_no,bank):
        if amount > self.balance:
            print("insufficient balance")
            return
        
        flag=False
        for user in bank.account_list:
            if user.account_no ==account_no:
                self.balance -= amount
                user.balance +=amount
                self.transactions={f"{amount} transfered to {account_no}"}
                flag=True

        if flag==False:
            print("Account does not exist")

