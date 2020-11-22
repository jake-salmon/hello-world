data = [] # Creates an empyt list to store the numbers in
print("This proram will make mean, median, and mode calculations very easy!")
print("First, we need to enter some numbers!")

numbers = input("Type your first number: ")
while numbers:
    data.append(float(numbers))
    print("\n", data)
    numbers = input("Add another number, or press enter to move on.")

# Puts the numbers in order
data.sort()
print("Here is the list in numerical order:\n", data)

# Mean
total = sum(data)
length = len(data)
print("\n\nThe Mean Is", total/length)

# Median
odd = length % 2
half = length // 2
if odd == 1:
    print("The median is:\n", data[half])
else:
    low = float(data[half-1])
    high = float(data[half])
    print("The median is half way between", low, "and", high)
    print("That makes it: ", low+(high - low) / 2)

# Mode
hits = []
for item in data:
    tally =  data.count(item)
    # Makes a tuple that is the number of hits paired with the relevant number
    values = (tally, item)
    # Only add one entery for each number in the set
    if values not in hits:
        hits.append(values)
hits.sort(reverse = True)
if hits[0][0] > hits[1][0]:
    print("\n\nThe mode is: ", hits[0][1], "hit appeared", hits[0][0], "times.")
else:
    print("There is not a mode"

)