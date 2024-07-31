# QUESTION 01
def str_to_int_with_fallback(s: str, fallback: int) -> int:
    try:
        return int(s)
    except ValueError:
        return fallback

# QUESTION 02
def int_to_str_with_format(num: int, format_spec: str) -> str:
    return format(num, format_spec)

# QUESTION 03
import math

def float_to_int_with_rounding(f: float, strategy: str) -> int:
    if strategy == "up":
        return math.ceil(f)
    elif strategy == "down":
        return math.floor(f)
    elif strategy == "nearest":
        return round(f)
    else:
        raise ValueError("Invalid rounding strategy. Use 'up', 'down', or 'nearest'.")

# QUESTION 04
def list_str_to_int_with_errors(strings: list[str]) -> tuple[list[int], list[str]]:
    integers = []
    errors = []
    for s in strings:
        try:
            integers.append(int(s))
        except ValueError:
            errors.append(s)
    return integers, errors

# QUESTION 05
def add_numbers(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Both inputs must be numbers.")
    return a + b


# QUESTION 06
def add_numbers(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Both inputs must be numbers.")
    return a + b

# QUESTION 06
def cumulative_subtraction(numbers: list[float]) -> float:
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements.")
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise TypeError("All elements in the list must be numbers.")
    
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

# QUESTION 07
def exponentiation_table(base: int, exponent_range: int) -> list[str]:
    if exponent_range < 1:
        raise ValueError("Exponent range must be at least 1.")
    return [f"{base}^{i} = {base**i}" for i in range(1, exponent_range + 1)]

# QUESTION 08
class DivisionByZeroError(Exception):
    def __init__(self, message: str):
        super().__init__(message)

def safe_division(a: float, b: float, precision: int) -> float:
    if b == 0:
        raise DivisionByZeroError("Cannot divide by zero.")
    return round(a / b, precision)

# QUESTION 09
def advanced_split_and_join(s: str, delimiter1: str, delimiter2: str) -> str:
    parts = s.split(delimiter1)
    filtered_parts = [part for part in parts if len(part) > 3]
    return delimiter2.join(filtered_parts)

# QUESTION 10
from collections import Counter

def enhanced_palindrome_check(s: str) -> tuple[bool, dict[str, int]]:
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    is_palindrome = cleaned == cleaned[::-1]
    frequency = dict(Counter(cleaned))
    return is_palindrome, frequency
