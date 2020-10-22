wage = float(input("What is the employee's hourly wage? "))
regular = float(input("How many total regular hours did the employee work this week? "))
overtime = float(input("How many total overtime hours did the employee work this week? "))

weeklypay = (regular * wage) + (overtime * (wage * 1.5))

weeklypay = str(round(weeklypay, 2))

print("The employee's gross pay for the week is $", weeklypay)