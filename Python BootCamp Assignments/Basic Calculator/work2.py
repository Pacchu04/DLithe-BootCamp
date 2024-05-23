bank_acc={}

def create_acc(cus_name,acc_no,initial_bal):
    if acc_no in bank_acc:
        print(f"Account number {acc_no} already exists.")
    else:
        bank_acc[acc_no]={
            'customer_name':cus_name,
            'balance':initial_bal
        }
        print(f"Account created for {cus_name} with account number {acc_no}")

def deposit(acc_no,amount):
    if amount>0:
        bank_acc[acc_no]['balance'] +=amount
        print(f"{amount} is Deposited sucessfully to Account Number: {acc_no}")
    else:
        print("Invalid amount:")

def withdraw(acc_no,amount):
    if acc_no in bank_acc:
        if amount>0 and amount <=bank_acc[acc_no]['balance']:
            bank_acc[acc_no]['balance'] -=amount
        else:
            print("Withdraw not possible: ")

def view_balance(acc_no):
    if acc_no in bank_acc:
        print(f"Customer Name: {bank_acc[acc_no]['customer_name']}\nAccount number: {acc_no} \nbalance: {bank_acc[acc_no]['balance']}\n")
    else:
        print("Not Found")

create_acc("Jhon",100,0)
create_acc("Sunny",101,0)
create_acc("Pramodh",102,0)

print()
view_balance(100)
deposit(100,10000)