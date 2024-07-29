# Question 01
def string_to_integer(s):
    try:
        return int(s)
    except ValueError:
        return None
    
    # Question 02
def integer_to_string(n):
    return str(n)

    # Question 03
def float_to_integer(f):
    return int(f)  # Converts the float to an integer by truncating towards zero

    # Question 04
def list_strings_to_integers(strings):
    integers = []
    for s in strings:
        try:
            integers.append(int(s))
        except ValueError:
            continue
    return integers


    # Question 05
def add_two_numbers(a, b):
    return a + b

    # Question 06
def subtract_two_numbers(a, b):
    return a - b

    # Question 07
def multiply_two_numbers(a, b):
    return a * b

    # Question 08
def divide_two_numbers(a, b):
    if b == 0:
        return None  # or raise an exception, depending on your needs
    return a / b

    # Question 09
def concatenate_two_strings(s1, s2):
    return s1 + s2

    # Question 10
def reverse_string(s):
    return s[::-1]
