# QUESTION 01
def complex_operations(c1_tuple, c2_tuple):
    try:
        c1 = complex(*c1_tuple)
        c2 = complex(*c2_tuple)
        addition = c1 + c2
        subtraction = c1 - c2
        multiplication = c1 * c2
        division = c1 / c2 if c2 != 0 else 'Division by zero error'
        return addition, subtraction, multiplication, division
    except (ValueError, TypeError) as e:
        return f"Invalid input: {e}"

result = complex_operations((2, 3), (1, 2))
print(result)

# QUESTION 02
def evaluate_polynomial(coeffs, x):
    degree = len(coeffs) - 1
    if degree == 0:
        return coeffs[0]
    elif degree == 1:
        return coeffs[0] * x + coeffs[1]
    elif degree == 2:
        return coeffs[0] * x**2 + coeffs[1] * x + coeffs[2]
    elif degree == 3:
        return coeffs[0] * x**3 + coeffs[1] * x**2 + coeffs[2] * x + coeffs[3]
    else:
        return "Polynomial degree not supported"

result = evaluate_polynomial([1, 0, -4, 4], 2)
print(result)

# QUESTION 03
def fibonacci(n, depth_limit, current_depth=0):
    if current_depth > depth_limit:
        return "Depth limit reached"
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1, depth_limit, current_depth+1) + fibonacci(n-2, depth_limit, current_depth+1)

result = fibonacci(10, 10)
print(result)

# QUESTION 04
from scipy.integrate import quad

def adaptive_integration(func, a, b, tol=1e-6):
    result, error = quad(func, a, b, epsabs=tol)
    return result, error

result = adaptive_integration(lambda x: x**2, 0, 1)
print(result)

# QUESTION 05
def prime_generator(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for start in range(2, int(limit**0.5) + 1):
        if sieve[start]:
            for multiple in range(start*start, limit + 1, start):
                sieve[multiple] = False
    primes = [num for num, is_prime in enumerate(sieve) if is_prime]
    return primes

result = prime_generator(50)
print(result)

# QUESTION 06
def memoized_fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    if len(memo) > 1000:
        return iterative_fibonacci(n)
    memo[n] = memoized_fibonacci(n-1, memo) + memoized_fibonacci(n-2, memo)
    return memo[n]

def iterative_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

result = memoized_fibonacci(10)
print(result)

# QUESTION 07
import re

def extract_dates(string):
    pattern = r'\b(\d{4})[-/](\d{2})[-/](\d{2})\b'
    dates = re.findall(pattern, string)
    valid_dates = [f"{year}-{month}-{day}" for year, month, day in dates if int(month) <= 12 and int(day) <= 31]
    return valid_dates

result = extract_dates("These are the dates: 2023-01-25, 2024/02/30, and 2023-13-01.")
print(result)

# QUESTION 08
def transform_string(s):
    words = s.split()
    transformed_words = []
    for word in words:
        transformed_word = word
        if word.isdigit():
            transformed_word = str(int(word))
        if len(word) > 5:
            transformed_word = word[::-1]
        transformed_words.append(transformed_word)
    return " ".join(transformed_words).title()

result = transform_string("123 apple banana 4567 grapes")
print(result)

# QUESTION 09
def evaluate_expression(expression, variables):
    try:
        for var, value in variables.items():
            expression = expression.replace(var, str(value))
        result = eval(expression)
        return result
    except NameError as e:
        return f"Undefined variable: {e}"
    except Exception as e:
        return f"Error: {e}"

result = evaluate_expression("a + b * c", {"a": 1, "b": 2, "c": 3})
print(result)

# QUESTION 10
import re

def validate_data(data_entries):
    report = []
    for entry in data_entries:
        entry_report = {"entry": entry, "valid": True, "errors": []}
        if len(entry) < 5 or len(entry) > 50:
            entry_report["valid"] = False
            entry_report["errors"].append("Invalid length")
        if not re.match("^[a-zA-Z0-9@.-]+$", entry):
            entry_report["valid"] = False
            entry_report["errors"].append("Invalid characters")
        if "@" in entry and not re.match(r"[^@]+@[^@]+\.[^@]+", entry):
            entry_report["valid"] = False
            entry_report["errors"].append("Invalid email format")
        if "-" in entry and not re.match(r"\d{4}-\d{2}-\d{2}", entry):
            entry_report["valid"] = False
            entry_report["errors"].append("Invalid date format")
        report.append(entry_report)
    return report

result = validate_data(["john.doe@example.com", "2024-12-31", "invalid-email@", "short", "ThisIsAValid123"])
print(result)
    