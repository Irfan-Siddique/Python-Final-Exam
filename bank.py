from user import User

class Bank:
    def __init__(self,name) -> None:
        self.name=name
        self.account_list=[]
        self.money_in_the_bank=0
        self.total_loan=0
        self.loan_status=None

    def create_account(self,name,email,age,account_type):
        user=User(name,email,age,account_type)
        self.account_list.append(user)
        print(f"account created successfully for {name}")
    
    def delete_account(self,account_no,user):
        removable=None
        for user in self.account_list:
            if user.account_no == account_no:
                removable=user
                break
        if removable:
            self.account_list.remove(removable)
            print(f"{user.name} removed successfully")
        else:
            print("account unavailable")

    def show_users(self):
        for item in self.account_list:
            print(f"Name: {item.name} age: {item.age} Account Number: {item.account_no}")
    
    def total_balance(self):
        print(f"total bank balance is: {self.money_in_the_bank}")

    def total_loan_amount(self):
        print(f"total loan taken: {self.total_loan}")

    def loan_feature(self,value):
        self.loan_status=value
        if self.loan_status==1:
            print("Loan can be taken")
        else:
            print("currently loan can't be taken")

    # def total_money_of_bank(self):
        