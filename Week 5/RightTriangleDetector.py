side1 = int(input("Enter the length of the first side of your triangle: "))
side2 = int(input("Enter the length of the second side of your triangle: "))
side3 = int(input("Enter the length of the third side of your triangle: "))

if side1 ** 2 == side2 + side3 or side2 ** 2 == side1 + side3 or side3 ** 2 == side1 + side2:
    print("This triangle is a right triangle.")
else:
    print("This triangle is not a right triangle.")
