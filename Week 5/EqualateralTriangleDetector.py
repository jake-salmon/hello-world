side1 = int(input("Enter the first side of your triangle: "))
side2 = int(input("Enter the second side of your triangle: "))
side3 = int(input("Enter the third side of your triangle: "))

if side1 != side2 and side1 != side3:
    print("This triangle is not an equilateral triangle.")
else:
    print("This triangle is an equilateral triangle.")
