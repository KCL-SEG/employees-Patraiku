"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, outputString, contractType, monthlyPay = 0, commissionType="none", workHours=0, hourlyWage=0,
                 contractsLanded=0, commissionpc = 0, bonus=0):
        self.name = name
        self.outputString = outputString
        if contractType == "salary":
            self.pay = monthlyPay
        elif contractType == "hourly":
            self.pay = hourlyWage*workHours
        if commissionType == "bonus":
            self.pay += bonus
        elif commissionType == "contract":
            self.pay += contractsLanded*commissionpc
        print(self.pay)






    def get_pay(self):
        pass

    def __str__(self):
        return self.name


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', "Billie works on a monthly salary of 4000.  Their total pay is 4000.", "salary", monthlyPay=4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', "Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.", "hourly", workHours=100, hourlyWage=25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', "Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.",
                 "salary", monthlyPay=3000, commissionType="contract", contractsLanded=4, commissionpc=200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', "Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.",
               "hourly", workHours=150, hourlyWage=25, commissionpc=220, contractsLanded=3, commissionType="contract")

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', "Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.",
                  "salary", monthlyPay=2000, commissionType="bonus", bonus=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', "Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.",
                 "hourly", workHours=120, hourlyWage=30, commissionType="bonus", bonus=600)
