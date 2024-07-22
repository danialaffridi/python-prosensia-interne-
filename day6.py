# question 01
def calculate_gross_pay(hours_worked, hourly_wage):
    return hours_worked * hourly_wage
hours_worked = float(input("Enter the number of hours worked: "))
hourly_wage = float(input("Enter the hourly wage rate: "))
total_pay = calculate_gross_pay(hours_worked, hourly_wage)
print(f"Total pay: {total_pay:.2f}")

# QUESTION 02
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"Temperature in Fahrenheit: {fahrenheit:.2f}")

# QUESTION 03
number = float(input("Enter a number: "))
if number > 0:
    result = "positive"
elif number < 0:
    result = "negative"
else:
    result = "zero"
print(f"The number is {result}.")

# QUESTION 04
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    result = "a leap year"
else:
    result = "not a leap year"
print(f"The year {year} is {result}.")

# QUESTION 05 
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
sum_result = num1 + num2
difference_result = num1 - num2
product_result = num1 * num2
quotient_result = num1 / num2
print(f"Sum: {sum_result}")
print(f"Difference: {difference_result}")
print(f"Product: {product_result}")
print(f"Quotient: {quotient_result}")

# QUESTION 06
import math

num = int(input("Enter a number: "))
factorial = math.factorial(num)
print(f"The factorial of {num} is {factorial}")

# QUESTION 07
user_string = input("Enter a string: ")
reversed_string = user_string[::-1]
print(f"Reversed string: {reversed_string}")

# QUESTION 08
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
result = num1 * num2
print(f"The result of multiplication is: {result}")

# QUESTION 09
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print(f"The result of multiplication is: {num1 * num2}")

# QUESTION 10
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if num2 != 0:
    result = num1 / num2
    print(f"The result of division is: {result}")
else:
    print("Error: Division by zero is not allowed.")

