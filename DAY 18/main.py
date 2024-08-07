# QUESTION 01
my_dict = {}
my_dict['key1'] = 'value1'
my_dict['key2'] = 'value2'
my_dict['key3'] = 'value3'
print(my_dict)

# QUESTION 02
def get_value(dictionary, key):
    if key in dictionary:
        print(dictionary[key])
    else:
        print("Key not found")

sample_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
get_value(sample_dict, 'age')
get_value(sample_dict, 'country')

# QUESTION 03
sample_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
print("Before update:", sample_dict)
sample_dict['age'] = 30
print("After update:", sample_dict)

# QUESTION 04
text = input("Enter a line of text: ")
words = text.split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)

# QUESTION 05
def print_keys_and_values(dictionary):
    keys = list(dictionary.keys())
    values = list(dictionary.values())
    print("Keys:", keys)
    print("Values:", values)

sample_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
print_keys_and_values(sample_dict)

# QUESTION 06
sample_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
value = sample_dict.get('country', 0)
print(value)

# QUESTION 07
students = {
    'student1': {
        'name': 'Alice',
        'age': 20,
        'grades': {'math': 'A', 'science': 'B'}
    },
    'student2': {
        'name': 'Bob',
        'age': 22,
        'grades': {'math': 'C', 'science': 'A'}
    },
    'student3': {
        'name': 'Charlie',
        'age': 23,
        'grades': {'math': 'B', 'science': 'B'}
    }
}
print(students)

# QUESTION 08
def merge_dictionaries(dict1, dict2):
    result = dict1.copy()
    result.update(dict2)
    return result

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'd': 5}
merged_dict = merge_dictionaries(dict1, dict2)
print(merged_dict)

# QUESTION 09
sample_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
try:
    print(sample_dict['country'])
except KeyError:
    print("Custom Error: The key 'country' does not exist in the dictionary")

# QUESTION 10
filename = 'sample.txt'
with open(filename, 'r') as file:
    text = file.read()
words = text.split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
most_common_word = max(word_count, key=word_count.get)
print(f"The most common word is '{most_common_word}' with {word_count[most_common_word]} occurrences")
