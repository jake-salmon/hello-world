import random

UserNumber = int(input("Enter the number you want the computer to guess: "))
smaller = int(input("Enter the bottom end of the guessing range: "))
larger = int(input("Enter top end of the guessing range: "))
ComputerGuess = random.randint(smaller, larger)
count = 1

print("The computer's guess is", ComputerGuess)

while ComputerGuess != UserNumber:
    count = count + 1
    if ComputerGuess < UserNumber:
        print("Too low")
        ComputerGuess = random.randint(ComputerGuess + 1, larger)
    elif ComputerGuess > UserNumber:
        print("Too high")
        ComputerGuess = random.randint(smaller, ComputerGuess - 1)
    print("The computer's guess is", ComputerGuess)

if count == 1:
    print("The computer guessed it in", count, "try!")
elif count > 1:
    print("The computer guessed it in", count, "tries!")

