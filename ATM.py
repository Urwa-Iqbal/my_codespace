username = "urwaiqbal4"
password = "123456"
t_amount = 5000
import pwinput as pw
import pymongo
def display():
                print(f"Your Current balance is = {t_amount}\nTHANK YOU")

def deposit():
            global t_amount
            amount=input("Enter Amount for Deposit: ")
            while True:
                if amount.isdigit() :
                    amount =int(amount)
                    t_amount = t_amount + amount
                    print(f"---------------------------------------------\nDeposit Successful of RS: {amount}")
                    break
                else:
                    amount = input("\n INVALID INPUT\nEnter Amount Again: ")

def withdraw ():
            global t_amount
            amount=input("Enter Amount for Withdrawal: ")
            while True:
                if amount.isdigit() :
                    amount =int(amount)
                    if amount <= 50000 and amount>0:
                        if amount <= t_amount:
                            t_amount = t_amount - amount
                            print(f"----------------------------------------------\nWithdrawal Successful of RS: {amount}")
                            break
                    else:
                        amount = input("\n Larger Amount! Please enter less than 50,000\nEnter Amount Again: ")
                else:
                    amount = input("\n INVALID INPUT\nEnter Amount Again: ")

def transfer():
    global t_amount
    n_username = input("Enter Username of Account you want to transfer money: ")
    amount=input("Enter Amount for Transfer: ")
    while True:
                if amount.isdigit() :
                    amount =int(amount)
                    if amount <= 50000 and amount>0:
                        if amount <= t_amount:
                            t_amount = t_amount - amount
                            print(f"------------------------------------\nTransfer Successful of RS: {amount} to {n_username}")
                            break
                    else:
                        amount = input("\n Larger Amount! Please enter less than 50,000\nEnter Amount Again: ")
                else:
                    amount = input("\n INVALID INPUT\nEnter Amount Again: ")



usern = input("Enter your Username: ")
passw = pw.pwinput("Enter your Password: ",mask="*")
while True:
        if usern == username and passw == password:
            print("\nWELCOME TO ATM \n--------------------------------------------\n1.Display Account Information\n2.Deposit Amount\n3.Withdraw Amount\n4.Transfer Amount\n5.EXIT\n Select any operation")
            operation = input("Enter Operation: ")
            while True:
                if operation.isdigit():
                    operation =int(operation)
                    break
                else:
                    operation = input("\n INVALID INPUT\nChoose operation Again: ")
            if operation == 1:
                display()
            elif operation == 2:
                deposit()
            elif operation == 3:
                withdraw()
            elif operation == 4:
                transfer()
            elif operation == 5:
                break
        else:
            usern = input("\nEnter your Username Again : ")
            passw = pw.pwinput("Enter your Password Again : ",mask="*")   
         
