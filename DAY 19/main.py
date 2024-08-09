# QUESTION 01
names = ('Alice', 'Bob', 'Charlie')
print(names[1])

# QUESTION 02
numbers = (4, 7, 1)
def max_in_tuple(t):
    return max(t)
print(max_in_tuple(numbers))

# QUESTION 03
fruits = ('apple', 'banana', 'cherry')
try:
    fruits[1] = 'orange'
except TypeError as e:
    print(e)

# QUESTION 04
lst = [1, 2, 3]
tup = (1, 2, 3)
lst.append(4)
try:
    tup.append(4)
except AttributeError as e:
    print(e)

# QUESTION 05
def swap(a, b):
    return b, a
a, b = swap(5, 10)
print(a, b)

# QUESTION 06
d = {'x': 1, 'y': 2, 'z': 3}
def dict_to_tuples(d):
    return list(d.items())
print(dict_to_tuples(d))

# QUESTION 07
d = {'a': 10, 'b': 1, 'c': 22}
def sort_by_value(d):
    return sorted(d.items(), key=lambda item: item[1], reverse=True)
print(sort_by_value(d))

# QUESTION 08
def compare_tuples(t1, t2):
    return [a == b for a, b in zip(t1, t2)]
print(compare_tuples((1, 2, 3), (3, 2, 1)))

# QUESTION 09
from collections import Counter
def top_n_words(filename, n):
    with open(filename, 'r') as file:
        words = file.read().split()
        count = Counter(words)
        return count.most_common(n)
print(top_n_words('romeo.txt', 3))

# QUESTION 10
d = {'a': 10, 'b': 1, 'c': 22}
def reversed_sorted_tuples(d):
    return sorted([(v, k) for k, v in d.items()])
print(reversed_sorted_tuples(d))
