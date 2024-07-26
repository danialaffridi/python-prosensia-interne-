# QUESTION 01
def concat_and_convert(s1, s2):
    result = s1 + s2
    if result.isdigit():
        return int(result)
    return result

print(concat_and_convert("123", "456"))  
print(concat_and_convert("abc", "123")) 

# QUESTION 02
def char_at_index(s, index):
    if 0 <= index < len(s):
        return s[index]
    return "Index out of bounds"

print(char_at_index("hello", 1))  # Output: e
print(char_at_index("hello", 10))  # Output: Index out of bounds


# QUESTION 03
def string_lengths(lst):
    return [len(s) for s in lst]

print(string_lengths(["apple", "banana", "cherry"]))  


# QUESTION 04
def print_chars_with_index(s):
    for index, char in enumerate(s):
        print(f"{index}: {char}")

print_chars_with_index("hello")

# QUESTION 05
def count_char(s, char):
    return s.count(char)
print(count_char("hello world", "o")) 

# QUESTION 06
def slice_string(s, start, end):
    start = max(0, start)
    end = min(len(s), end)
    return s[start:end]
print(slice_string("hello world", 2, 8)) 
print(slice_string("hello world", -1, 50))  

# QUESTION 07
def compare_strings(s1, s2):
    if s1 < s2:
        return "First string comes before the second string"
    elif s1 > s2:
        return "First string comes after the second string"
    return "Both strings are equal"
print(compare_strings("apple", "banana"))  
print(compare_strings("banana", "apple"))  
print(compare_strings("cherry", "cherry"))  

# QUESTION 08
def string_methods(s):
    return {
        "lowercase": s.lower(),
        "uppercase": s.upper(),
        "titlecase": s.title()
    }
print(string_methods("Hello World"))

# QUESTION 09
def search_and_replace(s, search_term, replacement_term):
    return s.replace(search_term, replacement_term)

print(search_and_replace("hello world", "world", "there"))

# QUESTION 10
def remove_whitespace(s):
    return ' '.join(s.strip().split())
print(remove_whitespace("  hello   world  "))

