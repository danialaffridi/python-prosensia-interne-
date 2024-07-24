# QUESTION 01
def print_greeting():
    print("Hello, DANIAL")
print_greeting()

# QUESTION 02
def max_value(s):
    return max(s)
print(max_value("Hello DANIAL"))

# QUESTON 03
def convert_to_float(n):
    return float(n)
print(convert_to_float(42))

# QUESTION 04
def add_numbers(a, b):
    return a + b
print(add_numbers(10, 20))

# QUESTION 05
def greet(language_code):
    if language_code == 'en':
        print("Hello")
    elif language_code == 'es':
        print("Hola")
    elif language_code == 'fr':
        print("Bonjour")
    else:
        print("Language not supported")
greet('en')
greet('es')
greet('fr')

# QUESTION 06
def compute_pay(hours, rate):
    if hours > 40:
        overtime = hours - 40
        return (40 * rate) + (overtime * rate * 1.5)
    else:
        return hours * rate

print(compute_pay(45, 10))

# QUESTION 07
def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

print(is_integer("123"))
print(is_integer("hello"))

# QUESTION 08
def print_lyrics():
    print("DUNYA K A MUSAFIR")
    print("MANZIL TERI QABAR HA")
    print("JO KR RAHA HA TA TO")
    print("2 DIN KA YA SAFAR HA")
   
print_lyrics()

# QUESTION 09
def multiply_numbers(a, b):
    return a * b

print(multiply_numbers(7, 8))

# QUESTION 10
def calculate_expression():
    return 1 + 2 * float(3) / 4 - 5

print(calculate_expression())
