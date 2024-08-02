# QUESTION 01
def complex_operations(c1_str, c2_str):
    c1 = complex(c1_str)
    c2 = complex(c2_str)
    addition = c1 + c2
    subtraction = c1 - c2
    multiplication = c1 * c2
    division = c1 / c2
    return addition, subtraction, multiplication, division

result = complex_operations("2+3j", "1+2j")
print(result)
 
# QUESTION 02
def binary_conversion(binary_str, length):
    integer = int(binary_str, 2)
    binary_str_converted = bin(integer)[2:].zfill(length)
    return binary_str_converted

result = binary_conversion("1010", 8)
print(result)

# QUESTION 03
import json
import logging

def dict_to_json_and_back(dictionary):
    try:
        json_str = json.dumps(dictionary)
        converted_dict = json.loads(json_str)
        return converted_dict
    except (TypeError, json.JSONDecodeError) as e:
        logging.error(f"Conversion error: {e}")
        return dictionary, str(e)

result = dict_to_json_and_back({"key": "value"})
print(result)

# QUESTION 04
class DimensionError(Exception):
    pass

def matrix_addition(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or any(len(row1) != len(row2) for row1, row2 in zip(matrix1, matrix2)):
        raise DimensionError("Matrices must have the same dimensions")
    result = [[elem1 + elem2 for elem1, elem2 in zip(row1, row2)] for row1, row2 in zip(matrix1, matrix2)]
    return result

result = matrix_addition([[1, 2], [3, 4]], [[5, 6], [7, 8]])
print(result)

# QUESTION 05
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def cumulative_product(lst):
    product = 1
    for num in lst:
        product *= num
    return product

def prime_factors_with_product(n):
    factors = prime_factors(n)
    product = cumulative_product(factors)
    return factors, product

result = prime_factors_with_product(28)
print(result)

# QUESTION 06
def interpolate_string(template, values):
    for key, value in values.items():
        template = template.replace(f"{{{key}}}", str(value))
    return template

result = interpolate_string("Hello, {name}! You are {age} years old.", {"name": "DANIAL", "age": 20})
print(result)

# QUESTION 07
from collections import Counter
import re

def is_anagram(s1, s2):
    s1_clean = re.sub(r'\W+', '', s1).lower()
    s2_clean = re.sub(r'\W+', '', s2).lower()
    return Counter(s1_clean) == Counter(s2_clean)

def anagram_frequencies(s1, s2):
    s1_clean = re.sub(r'\W+', '', s1).lower()
    s2_clean = re.sub(r'\W+', '', s2).lower()
    return Counter(s1_clean), Counter(s2_clean)

result = is_anagram("Listen", "Silent")
frequencies = anagram_frequencies("Listen", "Silent")
print(result)
print(frequencies)

# QUESTION 08
def flatten(nested_list):
    flat_list = []
    max_depth = [0]
    
    def _flatten(lst, depth):
        max_depth[0] = max(max_depth[0], depth)
        for item in lst:
            if isinstance(item, list):
                _flatten(item, depth + 1)
            else:
                flat_list.append(item)
                
    _flatten(nested_list, 1)
    return flat_list, max_depth[0]

result = flatten([1, [2, [3, 4]], [5, 6]])
print(result)

# QUESTION 09
def pattern_match(string, pattern):
    if len(string) != len(pattern):
        return False
    for s, p in zip(string, pattern):
        if p.isdigit() and not s.isdigit():
            return False
        if p.isalpha() and not s.isalpha():
            return False
    return True

result = pattern_match("a1b2", "a1b2")
print(result)

# QUESTION 10
import statistics

def normalize_data(data):
    if not all(isinstance(x, (int, float)) for x in data) or len(data) == 0:
        raise ValueError("Data must be a non-empty list of numbers")
    min_val, max_val = min(data), max(data)
    normalized = [(x - min_val) / (max_val - min_val) for x in data]
    mean = statistics.mean(normalized)
    median = statistics.median(normalized)
    variance = statistics.variance(normalized)
    return normalized, mean, median, variance

result = normalize_data([1, 2, 3, 4, 5])
print(result)
