TAX_RATE = 0.20
STANDARD_DEDUCTION = 10000.00
DEPENDENT_REDUCTION = 3000.00

grossIncome = float(input("Enter the gross income: "))
numDependents = int(input("Enter the number of dependents: "))

taxableIncome = grossIncome - STANDARD_DEDUCTION - DEPENDENT_REDUCTION * numDependents
incomeTax = taxableIncome - TAX_RATE

incomeTax = str(round(incomeTax, 2))

print("The income tax is $" + str(incomeTax))