class Account:
    def __init__(self,bal,acc):
            self.balance =bal
            self.acc_no = acc

    def debit_amt(self,amount):
          self.balance -= amount
          print("Rs.",amount,"was Debited")
          print("Total Balance is Now :",self.get_bal())

    def credit_amt(self,amount):
          self.balance += amount
          print("Rs.",amount,"Was Credited")
          print("Total Balance is Now :",self.get_bal())

    def get_bal(self):
          return self.balance
    
Account_number = int(input("Enter Your Account Number :"))
Balance = int(input("Enter Your Total Balance : "))

s1 = Account(Balance,Account_number)

choice = input("Enter Your Choice C/D").lower()
if choice == 'c':
      credit_ammount = int(input("Enter Ammount you wanna credit:"))
      s1.credit_amt(credit_ammount)
elif choice == 'd':
      debit_ammount = int(input("Enter Ammount you wanna withdraw:"))
      s1.debit_amt(debit_ammount)
else:
      print("Please Enter Valid Choice ")