from bank import Bank
from user import User

# admin=Bank("abc")
# admin.money_in_the_bank=10000
# admin.total_balance()
# admin.create_account("sff","ssdfdf",34,"sfdff")
# admin.delete_account({"sff":34})

admin=Bank("fdf")
def admin_fun():
    while True:
        print("1. create an account for user")
        print("2. delete an user account")
        print("3. see all user accounts list")
        print("4. check the total available balance of the bank.")
        print("5. check the total loan amount.")
        print("6. on or off the loan feature of the bank.")
        print("7. Exit")

        option= int(input("enter option: "))
        if option==1:
            name= input("enter user name: ")
            email= input("enter user email: ")
            age= input("enter user age: ")
            account_type=input("enter account type: ")
            admin.create_account(name,email,age,account_type)
        elif option==2:
            account_no=int(input("enter account number: "))
            admin.delete_account(account_no,admin)
        elif option==3:
            admin.show_users()
        elif option==4:
            print(f"available money in the bank: {admin.money_in_the_bank}")
        elif option==5:
            admin.total_loan_amount()
        elif option==6:
            op=int(input("enter 1 to enable loan feature & 2 to disable: "))
            if op==1:
                admin.loan_feature(True)
            elif op==2:
                admin.loan_feature(False)
            else:
                print("invalid input")
        elif option==7:
            break
        else:
            print("invalid input")

def user_fun():
    name= input("enter your name: ")
    email= input("enter your email: ")
    age= input("enter your age: ")
    account_type=input("enter account type: ")
    user=User(name,email,age,account_type)

    while True:
        print("1. deposit money")
        print("2. withdraw money")                                                         
        print("3. check available balance")
        print("4. check transaction history")
        print("5. take loan")
        print("6. transfer money")
        print("7. Exit")

        option= int(input("enter option: "))
        if option==1:
            amm=int(input("enter ammount: "))
            user.deposit(amm,admin)
        elif option==2:
            amm=int(input("enter ammount: "))
            user.withdraw(amm,admin)
        elif option==3:
            user.check_available_balance()
        elif option==4:
            user.transaction_history()
        elif option==5:
            amm=int(input("enter loan ammount: "))
            user.take_loan(amm,admin)
        elif option==6:
            amm=int(input("enter ammount: "))
            acc_no=input("enter account number: ")
            user.transfer_money(amm,acc_no,admin)

        elif option==7:
            break
        else:
            print("invalid input")

while True:
        print("Welcome")
        print("1. Admin")
        print("2. User")
        print("3. Exit")

        option= int(input("enter option: "))
        if option==1:
            admin_fun()
        elif option==2:
            user_fun()
        elif option==3:
            break
        else:
            print("invalid input")