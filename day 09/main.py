# QUESTION 1
numbers = []
while True:
    user_input = input("Enter a number (or 'done' to finish): ")  # input: 10
    if user_input == 'done':
        break
    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter a number.")

    user_input = input("Enter a number (or 'done' to finish): ")  #input: 20
    if user_input == 'done':
        break
    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter a number.")

    user_input = input("Enter a number (or 'done' to finish): ")  #input: 30
    if user_input == 'done':
        break
    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter a number.")

    user_input = input("Enter a number (or 'done' to finish): ")  #input: done
    if user_input == 'done':
        break
    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter a number.")

if numbers:
    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    print(f"Sum: {total_sum}, Average: {average}")
else:
    print("No numbers entered.")
# QUESTION 2
numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]
threshold = int(input("Enter the threshold: "))
filtered_numbers = [num for num in numbers if num > threshold]
print(f"Numbers greater than {threshold}: {filtered_numbers}")

# QUESTION 3
numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]

if numbers:
    largest = numbers[0]
    smallest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    for num in numbers:
        if num < smallest:
            smallest = num

    print(f"Largest number: {largest}")
    print(f"Smallest number: {smallest}")
else:
    print("No numbers entered.")


# QUESTION 4
numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]
unique_numbers = list(set(numbers))
print(f"Unique numbers: {unique_numbers}")


# QUESTION 5
while True:
    line = input("Enter a line of text (or 'done' to finish): ")
    if line == 'done':
        break
    if line.startswith('#'):
        continue
    print(line)

# QUESTION 6
predefined_number = 42
attempts = 0
while attempts < 10:
    guess = int(input("Guess the number: "))
    if guess == predefined_number:
        print("Correct!")
        break
    else:
        print("Try again.")
    attempts += 1
if attempts == 10:
    print("Out of attempts.")

# QUESTION 7
N = int(input("Enter a number: "))
sum_of_squares = sum(i**2 for i in range(1, N+1))
print(f"Sum of squares: {sum_of_squares}")

# QUESTION 8
input_string = input("Enter a string: ")
reversed_string = ""
for char in input_string:
    reversed_string = char + reversed_string
print(f"Reversed string: {reversed_string}")


# QUESTION 9
N = int(input("Enter the number of Fibonacci numbers to generate: "))
fib_sequence = [0, 1]
for i in range(2, N):
    next_fib = fib_sequence[-1] + fib_sequence[-2]
    fib_sequence.append(next_fib)
print(f"First {N} numbers in Fibonacci sequence: {fib_sequence[:N]}")
