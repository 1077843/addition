digits = int(input("How many numbers would you like to add? "))

numbers = []
while digits > 0:
    i = int(input("Enter number: "))
    numbers.append(i)
    digits = digits - 1

total = 0
for number in numbers:
    total = total + number

print(total)