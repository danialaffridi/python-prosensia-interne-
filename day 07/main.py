# Question 01
number = int(input("Enter an integer: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

# QUESTION 02
x = 5
if x > 2:
    print('Bigger than 2')
    print('Still bigger')
    print('Done with 2')
elif x < 2:
    print('Number is too small')

# QUESTION 03
x = 5
if x > 2:
    print('Bigger than 2')
    print('Still bigger')
print('Done with 2')

# QUESTION 04
number = int(input("Enter an integer: "))

if 10 <= number <= 20:
    print("Within range")
else:
    print("Out of range")

# QUESTION 05
x = 4

if x > 2:
    print('Bigger')
elif x == 2:
    print('Equal')
else:
    print('Smaller')

print('All done')

# QUESTION 06
number = int(input("Enter an integer: "))

if number < 10:
    print("Small")
elif 10 <= number <= 20:
    print("Medium")
else:
    print("Large")

# QUESTION 07
rawstr = input('Enter a number: ')

try:
    ival = int(rawstr)
    if ival > 0:
        print('Nice work')
    else:
        print('Not a number')
except ValueError:
    print('Not a number')

# QUESTION 08
hours = float(input("Enter hours worked: "))
rate = float(input("Enter hourly rate: "))

if hours > 40:
    overtime_hours = hours - 40
    overtime_pay = overtime_hours * (rate * 1.5)
    gross_pay = (40 * rate) + overtime_pay
else:
    gross_pay = hours * rate

print("Gross pay: $", gross_pay)

# QUESTION 09
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

if num1 > 0 and num2 > 0:
    print("Both are positive")
elif num1 > 0 or num2 > 0:
    print("One is positive")
else:
    print("None are positive")

# QUESTION 10
number = int(input("Enter an integer: "))

if number > 0:
    if number % 2 == 0:
        print("Positive and even")
    else:
        print("Positive but odd")
else:
    print("Negative")
