UserInput = list(map(float, input("Enter a series of numbers, and press enter to compute sum and average: ") .split()))
def Average(UserInput):
    return sum(UserInput) / len(UserInput)
print ("Average of the list =", round(Average(UserInput)))
print ("Sum of the list =", sum(UserInput))